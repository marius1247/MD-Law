#!/usr/bin/env python3
"""Add uniform Dataview-ready frontmatter to vault notes."""

from __future__ import annotations

import re
from datetime import date
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
TODAY = "2026-07-28"

DOMAIN_DENUMIRE = {
    "energie_electrica": ["energie electrică", "piață", "energetică"],
    "racordare_acces": ["racordare", "acces", "infrastructură"],
    "tarife_metodologii": ["tarife", "metodologii", "energetică"],
    "energie_regenerabila": ["energie regenerabilă", "energetică"],
    "piata_energiei": ["piața energiei", "energetică"],
    "general_reglementat": ["general reglementat", "energetică"],
    "tarife": ["tarife", "energetică"],
}

CONCEPT_FILES: dict[str, dict] = {
    "Producător Eligibil.md": {
        "title": "Producător Eligibil",
        "domain": "energie_regenerabila",
        "domeniu": ["energie regenerabilă", "energetică"],
        "status": "definit",
        "tags": ["concept", "regenerabile", "statut_legal"],
    },
    "Loc de Consum.md": {
        "title": "Loc de Consum",
        "domain": "general_reglementat",
        "domeniu": ["general reglementat", "racordare", "energetică"],
        "status": "definit",
        "tags": ["concept", "racordare", "consumator"],
    },
    "Tarif de Transport.md": {
        "title": "Tarif de Transport",
        "domain": "tarife",
        "domeniu": ["tarife", "transport", "energetică"],
        "status": "definit",
        "tags": ["concept", "tarife", "transport"],
    },
    "Punct de Delimitare.md": {
        "title": "Punct de Delimitare",
        "domain": "general_reglementat",
        "domeniu": ["general reglementat", "racordare", "energetică"],
        "status": "definit",
        "tags": ["concept", "racordare", "proprietate", "retea"],
    },
    "Baza Activelor Reglementate.md": {
        "title": "Baza Activelor Reglementate",
        "domain": "tarife",
        "domeniu": ["tarife", "metodologii", "energetică"],
        "status": "definit",
        "tags": ["concept", "tarife", "metodologie", "active_reglementate", "anre"],
    },
    "Furnizor de Ultimă Opțiune.md": {
        "title": "Furnizor de Ultimă Opțiune",
        "domain": "piata_energiei",
        "domeniu": ["piața energiei", "furnizare", "energetică"],
        "status": "definit",
        "tags": ["concept", "furnizare", "protectie_consumatori", "anre"],
    },
    "Devieri Financiare.md": {
        "title": "Devieri Financiare",
        "domain": "tarife",
        "domeniu": ["tarife", "metodologii", "energetică"],
        "status": "definit",
        "tags": ["concept", "tarife", "metodologie", "devieri", "anre"],
    },
    "Capacitate Rezervată.md": {
        "title": "Capacitate Rezervată",
        "domain": "racordare_acces",
        "domeniu": ["racordare", "acces", "transport", "energetică"],
        "status": "definit",
        "tags": ["concept", "acces", "transport", "retea", "capacitate"],
    },
    "Aviz de Racordare.md": {
        "title": "Aviz de Racordare",
        "domain": "racordare_acces",
        "domeniu": ["racordare", "acces", "energetică"],
        "status": "definit",
        "tags": ["concept", "racordare", "aviz", "autorizare"],
    },
    "Parte Responsabilă de Echilibrare.md": {
        "title": "Parte Responsabilă de Echilibrare",
        "domain": "piata_energiei",
        "domeniu": ["piața energiei", "echilibrare", "energetică"],
        "status": "definit",
        "tags": ["concept", "echilibrare", "piata_energiei", "operare"],
    },
    "Loc de Măsurare.md": {
        "title": "Loc de Măsurare",
        "domain": "general_reglementat",
        "domeniu": ["general reglementat", "măsurare", "energetică"],
        "status": "definit",
        "tags": ["concept", "masurare", "retea", "contorizare"],
    },
    "Tarif de Distribuție.md": {
        "title": "Tarif de Distribuție",
        "domain": "tarife",
        "domeniu": ["tarife", "distribuție", "energetică"],
        "status": "definit",
        "tags": ["concept", "tarife", "distributie", "retea"],
    },
}

MOC_FILES: dict[str, dict] = {
    "MOC Piața de Energie Electrică.md": {
        "title": "MOC Piața de Energie Electrică",
        "domain": "energie_electrica",
        "domeniu": ["energie electrică", "piață", "energetică"],
        "status": "draft",
        "tags": ["moc", "piata_energiei", "anre"],
    },
    "MOC Racordare și Acces la Rețele.md": {
        "title": "MOC Racordare și Acces la Rețele",
        "domain": "racordare_acces",
        "domeniu": ["racordare", "acces", "infrastructură"],
        "status": "draft",
        "tags": ["moc", "racordare", "infrastructura"],
    },
    "MOC Tarife și Metodologii ANRE.md": {
        "title": "MOC Tarife și Metodologii ANRE",
        "domain": "tarife_metodologii",
        "domeniu": ["tarife", "metodologii", "energetică"],
        "status": "draft",
        "tags": ["moc", "tarife", "metodologii", "anre"],
    },
}

DASHBOARD_META = {
    "title": "00 Index Concepte",
    "type": "dashboard",
    "tags": ["index", "concepte", "dataview"],
    "created": TODAY,
    "updated": TODAY,
}


def split_frontmatter(text: str) -> tuple[dict | None, str]:
    if not text.startswith("---\n"):
        return None, text
    end = text.find("\n---\n", 4)
    if end == -1:
        return None, text
    meta = yaml.safe_load(text[4:end]) or {}
    body = text[end + 5 :]
    return meta, body


def render_frontmatter(meta: dict) -> str:
    return "---\n" + yaml.safe_dump(meta, allow_unicode=True, sort_keys=False).rstrip() + "\n---\n"


def ensure_list(value) -> list:
    if value is None:
        return []
    if isinstance(value, list):
        return value
    return [value]


def infer_domain(meta: dict, filename: str) -> str | None:
    domeniu = [str(x).lower() for x in ensure_list(meta.get("domeniu"))]
    name = filename.lower()
    if "metodologie" in name or "tarife" in domeniu:
        return "tarife_metodologii"
    if "racordare" in domeniu or "racordare" in name:
        return "racordare_acces"
    if "regenerabile" in domeniu:
        return "energie_regenerabila"
    if "gaze-naturale" in domeniu or "gaze naturale" in name:
        if "tarife" in domeniu or "metodologie" in name:
            return "tarife_metodologii"
        if "racordare" in domeniu or "racordare" in name:
            return "racordare_acces"
        return "gaze_naturale"
    if "energie-electrică" in domeniu or "energia electrica" in name:
        if "tarife" in domeniu:
            return "tarife_metodologii"
        return "energie_electrica"
    if "energetică" in domeniu or "energetica" in name:
        return "energie_electrica"
    return None


def infer_issuer(meta: dict, filename: str) -> str:
    act_type = str(meta.get("act_type", "")).lower()
    name = filename.upper()
    if "HANRE" in name or act_type == "act-anre":
        return "ANRE"
    if act_type.startswith("lege") or name.startswith("LEGEA"):
        return "Parlament"
    if act_type == "hg" or "HG " in name:
        return "Guvern"
    if "CONSTITU" in name:
        return "Parlament"
    return "Autoritate"


def infer_legal_status(meta: dict, path: Path | None = None) -> str:
    tags = [str(t).lower() for t in ensure_list(meta.get("tags"))]
    if meta.get("in_vigoare") is False or "abrogat" in tags:
        return "abrogat"
    if meta.get("in_vigoare") is True:
        return "in_vigoare"
    if path and meta.get("type") == "act-note":
        text_name = path.name.replace("(notă)", "(text)")
        text_path = path.parent / text_name
        if text_path.exists():
            text_meta, _ = split_frontmatter(text_path.read_text(encoding="utf-8"))
            if text_meta:
                return infer_legal_status(text_meta)
    if "abrogat" not in tags:
        return "in_vigoare"
    return "necunoscut"


def infer_last_amended(meta: dict) -> str:
    if meta.get("updated"):
        return str(meta["updated"])[:10]
    if meta.get("an"):
        return f"{meta['an']}-01-01"
    return TODAY


def augment_act_tags(meta: dict, filename: str) -> list[str]:
    tags = [str(t) for t in ensure_list(meta.get("tags"))]
    if "acte_normative" not in tags:
        tags.append("acte_normative")
    domeniu = [str(x).lower() for x in ensure_list(meta.get("domeniu"))]
    name = filename.lower()
    if "racordare" in domeniu or "racordare" in name:
        for tag in ("racordare", "acces"):
            if tag not in tags:
                tags.append(tag)
    if "tarife" in domeniu or "tarife" in name or "metodologie" in name:
        for tag in ("tarife", "metodologie"):
            if tag not in tags:
                tags.append(tag)
    if "piață" in domeniu or "piata" in name or "pietei" in name:
        if "piata_energiei" not in tags:
            tags.append("piata_energiei")
    return tags


def update_concepts_and_mocs() -> int:
    changed = 0
    for fname, spec in CONCEPT_FILES.items():
        path = ROOT / "30 Concepts" / fname
        if not path.exists():
            continue
        _, body = split_frontmatter(path.read_text(encoding="utf-8"))
        meta = {
            "title": spec["title"],
            "type": "concept",
            "domain": spec["domain"],
            "domeniu": spec["domeniu"],
            "status": spec["status"],
            "tags": spec["tags"],
            "created": TODAY,
            "updated": TODAY,
        }
        path.write_text(render_frontmatter(meta) + body, encoding="utf-8")
        changed += 1

    for fname, spec in MOC_FILES.items():
        path = ROOT / "50 MOCs" / fname
        if not path.exists():
            continue
        _, body = split_frontmatter(path.read_text(encoding="utf-8"))
        meta = {
            "title": spec["title"],
            "type": "moc",
            "domain": spec["domain"],
            "domeniu": spec["domeniu"],
            "status": spec["status"],
            "tags": spec["tags"],
            "created": TODAY,
            "updated": TODAY,
        }
        path.write_text(render_frontmatter(meta) + body, encoding="utf-8")
        changed += 1

    dashboard = ROOT / "30 Concepts/00 Index Concepte.md"
    if dashboard.exists():
        _, body = split_frontmatter(dashboard.read_text(encoding="utf-8"))
        dashboard.write_text(render_frontmatter(DASHBOARD_META) + body, encoding="utf-8")
        changed += 1
    return changed


def migrate_acts() -> int:
    changed = 0
    acts_root = ROOT / "10 Legislation"
    for path in sorted(acts_root.rglob("*.md")):
        text = path.read_text(encoding="utf-8")
        meta, body = split_frontmatter(text)
        if not meta:
            continue
        note_type = meta.get("type")
        if note_type not in {"act-text", "act-note"}:
            continue
        domain = meta.get("domain") or infer_domain(meta, path.name)
        meta["domain"] = domain
        meta["issuer"] = meta.get("issuer") or infer_issuer(meta, path.name)
        meta["legal_status"] = infer_legal_status(meta, path)
        meta["last_amended"] = infer_last_amended(meta)
        meta["tags"] = augment_act_tags(meta, path.name)
        if "updated" not in meta:
            meta["updated"] = meta["last_amended"]
        path.write_text(render_frontmatter(meta) + body, encoding="utf-8")
        changed += 1
    return changed


def main() -> None:
    concept_moc_count = update_concepts_and_mocs()
    act_count = migrate_acts()
    print(f"Updated {concept_moc_count} concept/MOC/dashboard notes")
    print(f"Updated {act_count} act notes in 10 Legislation/")


if __name__ == "__main__":
    main()
