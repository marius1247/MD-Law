#!/usr/bin/env python3
"""Align MD Law vault folder skeleton with the EU / cross-jurisdiction model."""

from __future__ import annotations

import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# Folder moves (old relative → new relative)
FOLDER_MOVES: list[tuple[str, str]] = [
    ("00 Meta", "00 Inbox"),
    ("01 Sistemul juridic", "01 Legal system"),
    ("10 Acte normative", "10 Legislation"),
    ("20 Domenii", "20 Domains"),
    ("30 Concepte", "30 Concepts"),
    ("60 Autorități & Instituții", "60 Authorities"),
    ("Uploads", "uploads"),
]

LEGISLATION_SUBFOLDERS: list[tuple[str, str]] = [
    ("Constituție", "Constitution"),
    ("Coduri", "Codes"),
    ("Legi organice & ordinare", "Laws"),
    ("Hotărâri de Guvern", "Government Decisions"),
    ("Acte ANRE & autorități", "Authority Acts"),
]

# Note renames (basename → basename), applied after folder moves
NOTE_RENAMES: dict[str, str] = {
    "Constituția RM — text.md": "Constituția RM (text).md",
    "Constituția RM — notă.md": "Constituția RM (notă).md",
    "Template — Autoritate.md": "Template — Authority.md",
    "Convenții vault.md": "Conventions.md",
    "Energetică — sinteza sectorului.md": "Energetică — synthesis.md",
    "Societăți & guvernanță — sinteza.md": "Societăți & guvernanță — synthesis.md",
    "Fiscalitate — sinteza sistemului fiscal.md": "Fiscalitate — synthesis.md",
    "Contabilitate & raportare financiară — sinteza.md": "Contabilitate & raportare financiară — synthesis.md",
    "Drept comercial — sinteza.md": "Drept comercial — synthesis.md",
}

# Old energy concepts in 20 Concepte → Concept — naming in 30 Concepts
# Value None means duplicate of an existing Concept — note; drop after link rewrite
LEGACY_CONCEPTS: dict[str, str | None] = {
    "Aviz de Racordare.md": "Concept — Aviz de racordare.md",
    "Baza Activelor Reglementate.md": "Concept — Baza activelor reglementate.md",
    "Capacitate Rezervată.md": "Concept — Capacitate rezervată.md",
    "Devieri Financiare.md": "Concept — Devieri financiare.md",
    "Loc de Consum.md": "Concept — Loc de consum.md",
    "Loc de Măsurare.md": "Concept — Loc de măsurare.md",
    "Punct de Delimitare.md": "Concept — Punct de delimitare.md",
    "Tarif de Distribuție.md": "Concept — Tarif de distribuție.md",
    "Tarif de Transport.md": "Concept — Tarif de transport.md",
    "Furnizor de Ultimă Opțiune.md": None,  # → Concept — Furnizor de ultimă opțiune
    "Parte Responsabilă de Echilibrare.md": None,
    "Producător Eligibil.md": None,
    "00 Index Concepte.md": "00 Index Concepts.md",
}

LEGACY_MOCS: dict[str, str] = {
    "MOC Piața de Energie Electrică.md": "MOC — Piața de energie electrică.md",
    "MOC Racordare și Acces la Rețele.md": "MOC — Racordare și acces la rețele.md",
    "MOC Tarife și Metodologii ANRE.md": "MOC — Tarife și metodologii ANRE.md",
}

# Wikilink / prose title replacements (order matters — longer first)
TITLE_REPLACEMENTS: list[tuple[str, str]] = [
    ("Constituția RM — text", "Constituția RM (text)"),
    ("Constituția RM — notă", "Constituția RM (notă)"),
    ("Convenții vault", "Conventions"),
    ("Template — Autoritate", "Template — Authority"),
    ("Energetică — sinteza sectorului", "Energetică — synthesis"),
    ("Societăți & guvernanță — sinteza", "Societăți & guvernanță — synthesis"),
    ("Fiscalitate — sinteza sistemului fiscal", "Fiscalitate — synthesis"),
    ("Contabilitate & raportare financiară — sinteza", "Contabilitate & raportare financiară — synthesis"),
    ("Drept comercial — sinteza", "Drept comercial — synthesis"),
    ("MOC Piața de Energie Electrică", "MOC — Piața de energie electrică"),
    ("MOC Racordare și Acces la Rețele", "MOC — Racordare și acces la rețele"),
    ("MOC Tarife și Metodologii ANRE", "MOC — Tarife și metodologii ANRE"),
    ("00 Index Concepte", "00 Index Concepts"),
    # legacy concept titles → Concept — form
    ("Furnizor de Ultimă Opțiune", "Concept — Furnizor de ultimă opțiune"),
    ("Parte Responsabilă de Echilibrare", "Concept — Parte responsabilă de echilibrare"),
    ("Producător Eligibil", "Concept — Producător eligibil"),
    ("Aviz de Racordare", "Concept — Aviz de racordare"),
    ("Baza Activelor Reglementate", "Concept — Baza activelor reglementate"),
    ("Capacitate Rezervată", "Concept — Capacitate rezervată"),
    ("Devieri Financiare", "Concept — Devieri financiare"),
    ("Loc de Consum", "Concept — Loc de consum"),
    ("Loc de Măsurare", "Concept — Loc de măsurare"),
    ("Punct de Delimitare", "Concept — Punct de delimitare"),
    ("Tarif de Distribuție", "Concept — Tarif de distribuție"),
    ("Tarif de Transport", "Concept — Tarif de transport"),
]

PATH_REPLACEMENTS: list[tuple[str, str]] = [
    ("00 Meta/MOCs", "50 MOCs"),
    ("00 Meta", "00 Inbox"),
    ("01 Sistemul juridic", "01 Legal system"),
    ("10 Acte normative/Constituție", "10 Legislation/Constitution"),
    ("10 Acte normative/Coduri", "10 Legislation/Codes"),
    ("10 Acte normative/Legi organice & ordinare", "10 Legislation/Laws"),
    ("10 Acte normative/Hotărâri de Guvern", "10 Legislation/Government Decisions"),
    ("10 Acte normative/Acte ANRE & autorități", "10 Legislation/Authority Acts"),
    ("10 Acte normative", "10 Legislation"),
    ("20 Domenii", "20 Domains"),
    ("20 Concepte", "30 Concepts"),
    ("30 Concepte", "30 Concepts"),
    ("60 Autorități & Instituții", "60 Authorities"),
    ("Uploads/", "uploads/"),
    ("`Uploads`", "`uploads`"),
    ("Uploads folder", "uploads folder"),
    ("`source/`", "`99 Attachments/source-legis/`"),
]


def move_path(src: Path, dst: Path) -> None:
    dst.parent.mkdir(parents=True, exist_ok=True)
    if dst.exists():
        raise FileExistsError(f"Target exists: {dst}")
    shutil.move(str(src), str(dst))
    print(f"MOVE  {src.relative_to(ROOT)} → {dst.relative_to(ROOT)}")


def main() -> None:
    # 1. Top-level folder moves
    for old, new in FOLDER_MOVES:
        src, dst = ROOT / old, ROOT / new
        if src.exists() and not dst.exists():
            move_path(src, dst)
        elif not src.exists() and dst.exists():
            print(f"SKIP  {old} (already at {new})")
        else:
            print(f"WARN  unexpected state for {old} → {new}")

    # 2. Legislation subtypes
    legis = ROOT / "10 Legislation"
    for old, new in LEGISLATION_SUBFOLDERS:
        src, dst = legis / old, legis / new
        if src.exists() and not dst.exists():
            move_path(src, dst)

    # Remove empty placeholder under legislation
    empty_dir = legis / "Empty"
    if empty_dir.exists() and not any(empty_dir.iterdir()):
        empty_dir.rmdir()
        print("RMDIR 10 Legislation/Empty")

    # 3. Create Position Papers + ensure Inbox
    (ROOT / "20 Position Papers").mkdir(exist_ok=True)
    readme_pp = ROOT / "20 Position Papers" / "README.md"
    if not readme_pp.exists():
        readme_pp.write_text(
            "---\n"
            "title: \"20 Position Papers\"\n"
            "type: reference\n"
            "tags: [meta, position-papers]\n"
            "---\n\n"
            "# 20 Position Papers\n\n"
            "Soft law / regulator guidance for Moldova (ANRE guidance, ministry circulars, "
            "soft-law instruments). Naming: `<Issuer> — <short title> (notă)`.\n"
            "Industry still lives in `20 Domains` + `50 MOCs` — not as the primary filing system under `10 Legislation`.\n",
            encoding="utf-8",
        )
        print("CREATE 20 Position Papers/README.md")

    inbox = ROOT / "00 Inbox"
    inbox.mkdir(exist_ok=True)

    # 4. Move Roadmap into Inbox
    roadmap = ROOT / "Roadmap.md"
    if roadmap.exists():
        move_path(roadmap, inbox / "Roadmap.md")

    # 5. Move legacy MOCs from 00 Inbox/MOCs → 50 MOCs with rename
    legacy_moc_dir = ROOT / "00 Inbox" / "MOCs"
    moc_dir = ROOT / "50 MOCs"
    if legacy_moc_dir.exists():
        for old_name, new_name in LEGACY_MOCS.items():
            src = legacy_moc_dir / old_name
            if src.exists():
                move_path(src, moc_dir / new_name)
        # remove empty MOCs dir
        if legacy_moc_dir.exists() and not any(legacy_moc_dir.iterdir()):
            legacy_moc_dir.rmdir()
            print("RMDIR 00 Inbox/MOCs")

    # 6. Migrate legacy concepts from 20 Concepte
    legacy_concepts = ROOT / "20 Concepte"
    concepts = ROOT / "30 Concepts"
    concepts.mkdir(exist_ok=True)
    if legacy_concepts.exists():
        for old_name, new_name in LEGACY_CONCEPTS.items():
            src = legacy_concepts / old_name
            if not src.exists():
                continue
            if new_name is None:
                src.unlink()
                print(f"DROP  20 Concepte/{old_name} (duplicate of Concept — note)")
            else:
                dst = concepts / new_name
                if dst.exists():
                    src.unlink()
                    print(f"DROP  20 Concepte/{old_name} (target exists: {new_name})")
                else:
                    move_path(src, dst)
        # leftover files?
        for leftover in legacy_concepts.iterdir():
            if leftover.is_file():
                dst = concepts / leftover.name
                if not dst.exists():
                    move_path(leftover, dst)
                else:
                    leftover.unlink()
                    print(f"DROP  leftover {leftover.name}")
        if legacy_concepts.exists() and not any(legacy_concepts.iterdir()):
            legacy_concepts.rmdir()
            print("RMDIR 20 Concepte")

    # 7. Root orphan concept
    orphan = ROOT / "Concept — Lege organică vs lege ordinară.md"
    if orphan.exists():
        move_path(orphan, concepts / orphan.name)

    # 8. Note renames (by basename walk)
    for path in ROOT.rglob("*.md"):
        if ".git" in path.parts:
            continue
        new_name = NOTE_RENAMES.get(path.name)
        if new_name and path.name != new_name:
            dst = path.with_name(new_name)
            if not dst.exists():
                move_path(path, dst)

    # 9. Remove empty stub
    empty_file = ROOT / "empty"
    if empty_file.exists() and empty_file.stat().st_size <= 1:
        empty_file.unlink()
        print("RM empty")

    # 10. Text replacements across markdown (skip immutable dumps in 99 and uploads)
    skip_parts = {".git", "99 Attachments", "uploads"}
    for path in ROOT.rglob("*.md"):
        if any(p in path.parts for p in skip_parts):
            continue
        text = path.read_text(encoding="utf-8")
        original = text
        for old, new in PATH_REPLACEMENTS:
            text = text.replace(old, new)
        for old, new in TITLE_REPLACEMENTS:
            # avoid double-prefixing Concept — Concept —
            if old.startswith("Concept —"):
                text = text.replace(old, new)
            else:
                # Replace inside wikilinks and bare titles, but not if already Concept — prefixed
                text = re.sub(
                    rf"(?<!Concept — ){re.escape(old)}",
                    new,
                    text,
                )
        if text != original:
            path.write_text(text, encoding="utf-8")
            print(f"EDIT  {path.relative_to(ROOT)}")

    # 11. Update scripts path constants
    for script_name in ("ingest_uploads.py", "migrate_frontmatter.py"):
        script = ROOT / "scripts" / script_name
        if not script.exists():
            continue
        text = script.read_text(encoding="utf-8")
        original = text
        for old, new in PATH_REPLACEMENTS:
            text = text.replace(old, new)
        text = text.replace('ROOT / "Uploads"', 'ROOT / "uploads"')
        text = text.replace('ROOT / "10 Acte normative"', 'ROOT / "10 Legislation"')
        text = text.replace('"20 Concepte"', '"30 Concepts"')
        if text != original:
            script.write_text(text, encoding="utf-8")
            print(f"EDIT  scripts/{script_name}")

    print("\nDone.")


if __name__ == "__main__":
    main()
