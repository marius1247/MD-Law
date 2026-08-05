#!/usr/bin/env python3
"""Extract PDF uploads into source-legis archives and normalized (text) files."""

from __future__ import annotations

import re
import shutil
from datetime import date
from pathlib import Path

from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[1]
SOURCE_DIR = ROOT / "99 Attachments/source-legis"
UPLOADS_DIR = Path("/home/ubuntu/.cursor/projects/workspace/uploads")

ARTICLE_RE = re.compile(
    r"^Articolul\s+(\d+)(?:\s*[¹²³]|\.)?\s*(.*)$",
    re.IGNORECASE,
)
CAPITOL_RE = re.compile(r"^Capitolul\s+", re.IGNORECASE)


def extract_pdf_text(pdf_path: Path) -> str:
    reader = PdfReader(str(pdf_path))
    parts = []
    for page in reader.pages:
        parts.append(page.extract_text() or "")
    return "\n".join(parts)


def normalize_body(raw: str) -> tuple[str, int]:
    lines = raw.splitlines()
    out: list[str] = []
    article_nums: list[int] = []
    for line in lines:
        stripped = line.strip()
        if CAPITOL_RE.match(stripped):
            out.append(f"## {stripped}")
            continue
        m = ARTICLE_RE.match(stripped)
        if m:
            num = int(m.group(1))
            rest = (m.group(2) or "").strip()
            article_nums.append(num)
            if rest:
                out.append(f"### Articolul {num}. {rest}")
            else:
                out.append(f"### Articolul {num}.")
            continue
        out.append(line)
    return "\n".join(out), len(set(article_nums))


def ingest_lp325() -> dict:
    pdf = UPLOADS_DIR / "152974_86e0.pdf"
    raw = extract_pdf_text(pdf)
    SOURCE_DIR.mkdir(parents=True, exist_ok=True)
    archive = SOURCE_DIR / "152974.md"
    archive.write_text(raw, encoding="utf-8")

    body, article_count = normalize_body(raw)
    # Statutory text ends before annex listing stub on last page
    annex_stub = re.search(r"\nanexa nr\.1\n", body)
    if annex_stub:
        body = body[:annex_stub.start()].rstrip()

    complete = article_count >= 91 and "Articolul 91" in body

    fm = f"""---
title: "Legea 325-2025 — achizitii publice (text)"
type: act-text
act_type: lege-organică
nr: "325"
an: 2025
domeniu:
- achiziții
in_vigoare: true
legis_id: '152974'
legis_url: https://www.legis.md/cautare/getResults?lang=ro&doc_id=152974
continut: text-statut
text_complet: {'true' if complete else 'false'}
articole_numarate: {article_count}
tags:
- act
- text
- acte_normative
- achiziții
created: {date.today().isoformat()}
updated: {date.today().isoformat()}
source_ingest: manual-pdf-upload
domain: achiziții
issuer: Parlament
legal_status: in_vigoare
last_amended: '{date.today().isoformat()}'
effective_from: '2027-01-01'
supersedes: '[[Legea 131-2015 — achizitii publice (text)]]'
---
"""

    header = """# Legea 325/2025 — achiziții publice

> [!info] Sursă & versiune
> Text preluat din **PDF upload** (legis.md doc_id [152974](https://www.legis.md/cautare/getResults?lang=ro&doc_id=152974)), MO 76–79/12.02.2026 art. 39.
> **Intră în vigoare:** 01.01.2027 · **Abrogă:** Legea nr. 131/2015 (art. 90 alin. (4)).
> Articole normalizate ca `### Articolul N.` pentru ancorare wikilink.
> Analiză: [[Legea 325-2025 — achizitii publice (notă)]].

> [!warning] Anexe neincluse în PDF
> Anexele nr. 1–14 (formulare UE, liste CPV/servicii) nu apar în documentul uploadat — doar referințe în text. Descărcați consolidarea completă de pe legis.md înainte de citarea conținutului anexelor.

---

"""

    text_path = ROOT / "10 Acte normative/Legi organice & ordinare/Legea 325-2025 — achizitii publice (text).md"
    text_path.write_text(fm + header + body + "\n", encoding="utf-8")

  # Copy PDF to attachments
    pdf_dest = SOURCE_DIR / "152974_86e0.pdf"
    if not pdf_dest.exists():
        shutil.copy2(pdf, pdf_dest)

    return {
        "act": "LP325/2025",
        "articles": article_count,
        "complete": complete,
        "chars": len(body),
    }


def archive_hanre423() -> dict:
    pdf = UPLOADS_DIR / "151929_6852.pdf"
    raw = extract_pdf_text(pdf)
    archive = SOURCE_DIR / "151929-pdf-upload.md"
    archive.write_text(raw, encoding="utf-8")
    pdf_dest = SOURCE_DIR / "151929_6852.pdf"
    if not pdf_dest.exists():
        shutil.copy2(pdf, pdf_dest)
    pages = len(PdfReader(str(pdf)).pages)
    return {"act": "HANRE423/2019", "pages": pages, "chars": len(raw)}


def main() -> None:
    r1 = ingest_lp325()
    r2 = archive_hanre423()
    print(r1)
    print(r2)


if __name__ == "__main__":
    main()
