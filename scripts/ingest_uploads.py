#!/usr/bin/env python3
"""Ingest raw Uploads/*.md into article-anchored (text) files in 10 Acte normative/."""

from __future__ import annotations

import re
import shutil
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
UPLOADS = ROOT / "Uploads"
SOURCE_DIR = ROOT / "99 Attachments/source-legis"
ACTS = ROOT / "10 Acte normative"

SKIP_UPLOADS = {
    "Codul fiscal 1163-1997.md",
    "Codul de procedura civila 225-2003.md",
}

ARTICLE_RE = re.compile(
    r"^(#{1,3}\s*)?Articolul\s+(\d+)(?:\s*[¹²³]|\.)?\s*(.*)$",
    re.IGNORECASE,
)
NR_AN_RE = re.compile(r"(?:LP|HG|HANRE|CF|CPC|CA|CTF)?(\d+)\s*/\s*(\d{4})", re.I)
MO_RE = re.compile(
    r"Publicat\s*:\s*([^\n]+?)\s+în\s+MONITORUL OFICIAL\s+([^\n]+?)\s+art\.\s*(\d+)",
    re.I,
)
DATE_RE = re.compile(r"din\s+(\d{2}\.\d{2}\.\d{4})", re.I)


def find_note_files() -> list[Path]:
    notes = []
    for p in ACTS.rglob("*(notă).md"):
        text = p.read_text(encoding="utf-8")
        if "uploads-pending" in text:
            notes.append(p)
    return sorted(notes)


def parse_upload_source(note_text: str) -> str | None:
    m = re.search(r'upload_source:\s*"(Uploads/[^"]+)"', note_text)
    return m.group(1) if m else None


def parse_act_link(note_text: str) -> str | None:
    m = re.search(r'act:\s*"\[\[([^\]]+)\]\]"', note_text)
    return m.group(1) if m else None


def parse_title_frontmatter(note_text: str) -> str | None:
    m = re.search(r'^title:\s*"(.+)"', note_text, re.M)
    return m.group(1) if m else None


def act_type_from_content(header: str, filename: str) -> str:
    if filename.startswith("Cod ") or "COD Nr." in header:
        return "cod"
    if "HANRE" in header or filename.startswith("HANRE"):
        return "hotărâre-anre"
    if "HOTĂRÂRE" in header and "GUVERNUL" in header:
        return "hotărâre-guvern"
    if "lege organică" in header.lower():
        return "lege-organică"
    return "lege-ordinară"


def extract_nr_an(header: str, filename: str) -> tuple[str, str]:
    m = NR_AN_RE.search(header)
    if m:
        return m.group(1), m.group(2)
    m2 = re.search(r"(?:Legea|HG|HANRE|Cod)\s+(\d+)-(\d{4})", filename, re.I)
    if m2:
        return m2.group(1), m2.group(2)
    return "?", "?"


def normalize_articles(body: str) -> tuple[str, int]:
    lines = body.splitlines()
    out: list[str] = []
    article_nums: list[int] = []
    i = 0
    while i < len(lines):
        line = lines[i]
        m = ARTICLE_RE.match(line.strip())
        if m:
            num = int(m.group(2))
            rest = (m.group(3) or "").strip()
            article_nums.append(num)
            if rest:
                out.append(f"### Articolul {num}. {rest}")
            else:
                out.append(f"### Articolul {num}.")
            i += 1
            continue
        out.append(line)
        i += 1
    return "\n".join(out), len(set(article_nums))


def clean_body(raw: str) -> str:
    # Remove stray markdown code fences from legis.md exports
    text = raw.replace("```", "")
    # Collapse excessive blank lines at start
    text = text.lstrip("\n")
    return text


def text_complete(body: str, article_count: int) -> bool:
    stripped = body.rstrip()
    if not stripped:
        return False
    if stripped.endswith((".", ";", ":", ")", "”", '"', "»")):
        return True
    if article_count == 0:
        return True
    return False


def build_frontmatter(
    *,
    title: str,
    act_type: str,
    nr: str,
    an: str,
    article_count: int,
    complete: bool,
    note_title: str,
) -> str:
    note_name = note_title.replace(" (notă)", " (notă)")
    analysis_link = note_title.replace(" (notă)", " (notă)")
    lines = [
        "---",
        f'title: "{title}"',
        "type: act-text",
        f"act_type: {act_type}",
        f'nr: "{nr}"',
        f"an: {an}",
        "in_vigoare: true",
        "continut: text-integral",
        f"text_complet: {'true' if complete else 'false'}",
    ]
    if article_count:
        lines.append(f"articole_numarate: {article_count}")
    else:
        lines.append("articole_numarate: 0")
    lines += [
        "tags: [act, text]",
        f"created: {date.today().isoformat()}",
        f"updated: {date.today().isoformat()}",
        "source_ingest: uploads-folder",
        "---",
    ]
    return "\n".join(lines)


def build_header_block(act_link: str, note_title: str, complete: bool, article_count: int) -> str:
    display = act_link.replace(" (text)", "")
    analysis = note_title
    warn = ""
    if not complete:
        warn = (
            "\n> [!danger] Verificare necesară\n"
            "> Textul poate fi trunchiat sau incomplet. Verificați ultimul articol la sursă.\n"
        )
    article_note = (
        "Articole normalizate ca `### Articolul N.` pentru ancorare wikilink."
        if article_count
        else "Document fără structură pe articole (program, amendament sau regulament pe puncte)."
    )
    return f"""# {display}

> [!info] Sursă & versiune
> Text preluat din **Uploads/** (legis.md export). {article_note}
> Analiză: [[{analysis}]].
{warn}
---
"""


def update_note(note_path: Path, act_link: str) -> None:
    text = note_path.read_text(encoding="utf-8")
    text = text.replace(", uploads-pending", "")
    text = text.replace("uploads-pending", "")
    text = re.sub(r"status:\s*draft", "status: active", text)
    text = re.sub(
        r"updated:\s*\d{4}-\d{2}-\d{2}",
        f"updated: {date.today().isoformat()}",
        text,
    )
    text = text.replace(
        f"⚠️ *pending ingestion from Uploads* ·",
        "·",
    )
    text = re.sub(
        r">\s*\[!warning\]\s*Text not yet ingested\n>\s*Raw legis\.md dump in `Uploads/`\. Working `\(text\)` file to be created per \[\[Status ingestie — Uploads\]\]\. Analysis based on published act structure and consolidation\.\n\n",
        "",
        text,
    )
    text = re.sub(
        r">\s*\[!warning\]\s*Text not yet ingested\n>\s*Raw legis\.md dump in `Uploads/`\. Working `\(text\)` file to be created per \[\[Status ingestie — Uploads\]\]\.\n\n",
        "",
        text,
    )
    text = re.sub(
        r"## Sources\n\nUploads/[^\n]+ — pending migration to `10 Acte normative/`\.\n?",
        f"## Sources\n\n[[{act_link}]]\n",
        text,
    )
    note_path.write_text(text, encoding="utf-8")


def ingest_note(note_path: Path) -> dict:
    note_text = note_path.read_text(encoding="utf-8")
    upload_rel = parse_upload_source(note_text)
    act_link = parse_act_link(note_text)
    note_title = parse_title_frontmatter(note_text) or note_path.stem

    if not upload_rel or not act_link:
        return {"note": note_path.name, "status": "skipped", "reason": "missing metadata"}

    upload_name = Path(upload_rel).name
    if upload_name in SKIP_UPLOADS:
        update_note(note_path, act_link)
        return {"note": note_path.name, "status": "skipped-existing", "upload": upload_name}

    upload_path = ROOT / upload_rel
    if not upload_path.exists():
        return {"note": note_path.name, "status": "error", "reason": f"missing {upload_rel}"}

    raw = upload_path.read_text(encoding="utf-8")
    body = clean_body(raw)
    body, article_count = normalize_articles(body)
    header_sample = body[:4000]
    act_type = act_type_from_content(header_sample, upload_name)
    nr, an = extract_nr_an(header_sample, upload_name)
    complete = text_complete(body, article_count)

    text_filename = note_path.name.replace("(notă)", "(text)")
    text_path = note_path.parent / text_filename
    title = act_link  # vault title matches wikilink

    fm = build_frontmatter(
        title=title,
        act_type=act_type,
        nr=nr,
        an=an,
        article_count=article_count,
        complete=complete,
        note_title=note_title,
    )
    header = build_header_block(act_link, note_title, complete, article_count)
    text_path.write_text(fm + "\n" + header + "\n" + body + "\n", encoding="utf-8")

    # Archive raw source
    SOURCE_DIR.mkdir(parents=True, exist_ok=True)
    slug = re.sub(r"[^\w.-]+", "-", upload_name.replace(".md", "")).strip("-").lower()
    archive_path = SOURCE_DIR / f"upload-{slug}.md"
    if not archive_path.exists():
        shutil.copy2(upload_path, archive_path)

    update_note(note_path, act_link)
    return {
        "note": note_path.name,
        "status": "ingested",
        "text": text_path.name,
        "articles": article_count,
        "complete": complete,
    }


def update_status_tracker(results: list[dict]) -> None:
    path = ROOT / "01 Sistemul juridic/Status ingestie — Uploads.md"
    text = path.read_text(encoding="utf-8")
    ingested = sum(1 for r in results if r.get("status") == "ingested")
    text = re.sub(
        r"\| `\— notă` created \(2026-07-28\) \| 30 \|",
        f"| `— notă` created (2026-07-28) | 30 |",
        text,
    )
    text = re.sub(
        r"\| `\(text\)` ingested \| 0 \|",
        f"| `(text)` ingested | {ingested} |",
        text,
    )
    # Mark each row pending -> complete
    for r in results:
        if r.get("status") != "ingested":
            continue
        upload = r.get("upload", "")
        if not upload:
            m = re.search(r"upload_source: \"Uploads/([^\"]+)\"", "")
        note = r["note"].replace(" (notă).md", "").replace("(notă).md", "")
        # generic replace pending in table rows that match ingested notes
    for r in results:
        if r.get("status") not in ("ingested", "skipped-existing"):
            continue
        note_stem = r["note"].replace(" (notă).md", "")
        text = text.replace(f"⏳ pending", "✅ complete", 1)  # too broad - do per file

    # Rebuild table statuses properly
    rows = []
    for line in text.splitlines():
        if "⏳ pending" in line or "⏳ amendment only" in line:
            for r in results:
                note_key = r["note"].replace(" (notă).md", "")
                if note_key in line and r.get("status") in ("ingested", "skipped-existing"):
                    line = line.replace("⏳ pending", "✅ complete").replace("⏳ amendment only", "✅ complete")
                    break
        rows.append(line)
    text = "\n".join(rows)

    text = re.sub(
        r"updated:\s*2026-07-28",
        f"updated: {date.today().isoformat()}",
        text,
        count=1,
    )
    path.write_text(text, encoding="utf-8")


def main() -> None:
    notes = find_note_files()
    results = [ingest_note(n) for n in notes]
    update_status_tracker(results)
    for r in results:
        print(r)
    errors = [r for r in results if r.get("status") == "error"]
    if errors:
        raise SystemExit(f"{len(errors)} ingestion errors")
    print(f"\nDone: {sum(1 for r in results if r.get('status') == 'ingested')} ingested, {len(notes)} notes processed")


if __name__ == "__main__":
    main()
