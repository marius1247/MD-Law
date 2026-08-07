#!/usr/bin/env python3
"""Ingest 2026-08-07 energy PDF batch (OCR from legis.md image PDFs)."""

from __future__ import annotations

import re
import shutil
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
UPLOADS = ROOT / "uploads"
SOURCE = ROOT / "99 Attachments/source-legis"
AUTH = ROOT / "10 Legislation/Authority Acts"
TODAY = date.today().isoformat()

# Source PDFs live in Cursor uploads path until copied
CURSOR_UPLOADS = Path("/home/ubuntu/.cursor/projects/workspace/uploads")

ACTS = [
    {
        "pdf": "124161_4d55.pdf",
        "ocr": "124161_4d55.ocr.txt",
        "legis_id": "124161",
        "nr": "94",
        "an": 2019,
        "slug": "dezvoltarea retelelor electrice de distributie",
        "title": "HANRE 94-2019 — dezvoltarea retelelor electrice de distributie",
        "mo": "MO 171-177/24.05.2019 art. 851",
        "domeniu": ["energetică", "electricitate", "rețele"],
        "enabling_act": "[[Legea 164-2025 — energia electrica (text)|L164/2025]] · issued under L107/2016",
        "amended_by": "[[HANRE 414-2020 — modificare HANRE 94-2019 dezvoltare retele distributie EE (notă)|414/2020]]",
        "complete": True,
    },
    {
        "pdf": "124090_c3b8.pdf",
        "ocr": "124090_c3b8.ocr.txt",
        "legis_id": "124090",
        "nr": "414",
        "an": 2020,
        "slug": "modificare HANRE 94-2019 dezvoltare retele distributie EE",
        "title": "HANRE 414-2020 — modificare HANRE 94-2019 dezvoltare retele distributie EE",
        "mo": "MO 313-317/27.11.2020 art. 1241",
        "domeniu": ["energetică", "electricitate", "rețele"],
        "enabling_act": "[[HANRE 94-2019 — dezvoltarea retelelor electrice de distributie (text)|94/2019]]",
        "complete": True,
    },
    {
        "pdf": "112162_6888.pdf",
        "ocr": "112162_6888.ocr.txt",
        "legis_id": "112162",
        "nr": "316",
        "an": 2018,
        "slug": "dirijare dispecerat sistem electroenergetic",
        "title": "HANRE 316-2018 — dirijare dispecerat sistem electroenergetic",
        "mo": "MO 29/29.01.2019 art. 225",
        "domeniu": ["energetică", "electricitate", "dispecerat"],
        "enabling_act": "[[Legea 164-2025 — energia electrica (text)|L164/2025]] · issued under L107/2016",
        "complete": True,
    },
    {
        "pdf": "110790_901d.pdf",
        "ocr": "110790_901d.ocr.txt",
        "legis_id": "110790",
        "nr": "138",
        "an": 2018,
        "slug": "dezvoltarea retelelor de distributie gaze",
        "title": "HANRE 138-2018 — dezvoltarea retelelor de distributie gaze",
        "mo": "MO 235-244/29.06.2018 art. 1055",
        "domeniu": ["energetică", "gaze", "rețele"],
        "enabling_act": "[[Legea 108-2016 — gazele naturale (text)|L108/2016]]",
        "complete": True,
    },
    {
        "pdf": "135421_18e5.pdf",
        "ocr": "135421_18e5.ocr.txt",
        "legis_id": "135421",
        "nr": "8",
        "an": 2023,
        "slug": "modificare racordare gaze si masurare gaze",
        "title": "HANRE 8-2023 — modificare racordare gaze si masurare gaze",
        "mo": "MO 31-34/03.02.2023 art. 137",
        "domeniu": ["energetică", "gaze", "racordare", "metrologie"],
        "enabling_act": "[[HANRE 112-2019 — racordarea la retelele de gaze (text)|112/2019]] · HANRE 297/2022",
        "complete": False,  # annexes 5''/5''' referenced but OCR may truncate annex tables
    },
]


def load_ocr(path: Path) -> str:
    text = path.read_text(encoding="utf-8")
    return clean_ocr(text)


def clean_ocr(raw: str) -> str:
    text = raw.replace("--- page break ---", "\n\n")
    text = re.sub(r"^\s*x\s*$", "", text, flags=re.M)
    text = text.replace("\x0c", "\n")
    # Normalize common OCR spacing in HANRE numbers
    text = re.sub(r"HANRE\s*(\d+)\s*/\s*(\d{4})", r"HANRE\1/\2", text)
    text = re.sub(r"\n{4,}", "\n\n\n", text)
    return text.strip() + "\n"


def normalize_structure(body: str) -> tuple[str, int]:
    """Light structure pass: Capitolul headers + punct anchors."""
    lines = body.splitlines()
    out: list[str] = []
    point_nums: set[str] = set()
    for line in lines:
        s = line.strip()
        m = re.match(r"^Capitolul\s+(\d+)\s*$", s, re.I)
        if m:
            out.append(f"## Capitolul {m.group(1)}")
            continue
        m = re.match(r"^Sectiunea\s+(\d+)\s*$", s, re.I)
        if m:
            out.append(f"### Secțiunea {m.group(1)}")
            continue
        m = re.match(r"^Secţiunea\s+(\d+)\s*$", s, re.I)
        if m:
            out.append(f"### Secțiunea {m.group(1)}")
            continue
        m = re.match(r"^(\d{1,3})\.\s+(.+)$", s)
        if m and len(m.group(2)) > 3:
            num = m.group(1)
            point_nums.add(num)
            rest = m.group(2)
            if len(rest) > 120:
                out.append(f"### Punctul {num}.")
                out.append(rest)
            else:
                out.append(f"### Punctul {num}. {rest}")
            continue
        out.append(line)
    return "\n".join(out), len(point_nums)


def write_text(act: dict, body: str, point_count: int) -> Path:
    title = f"{act['title']} (text)"
    note = f"{act['title']} (notă)"
    text_path = AUTH / f"{title}.md"
    domain_yaml = "\n".join(f"- {d}" for d in act["domeniu"])
    complete = act["complete"]
    fm = [
        "---",
        f'title: "{title}"',
        "type: act-text",
        "instrument: act-anre",
        "act_type: hotărâre-anre",
        f'nr: "{act["nr"]}"',
        f"an: {act['an']}",
        "domeniu:",
        domain_yaml,
        f"domain: [{', '.join(act['domeniu'])}]",
        "forta_juridica: 8",
        "in_force: true",
        "in_vigoare: true",
        f'mo_publicare: "{act["mo"]}"',
        f'legis_id: "{act["legis_id"]}"',
        f'legis_url: "https://www.legis.md/cautare/getResults?lang=ro&doc_id={act["legis_id"]}"',
        f"version_date: {TODAY}",
        f"versiune_text: {TODAY}",
        f"continut: {'text-integral' if complete else 'partial'}",
        f"text_complet: {'true' if complete else 'false'}",
        f"puncte_numarate: {point_count}",
        "articole_numarate: 0",
        "tags: [act, text, acte_normative, energetică]",
        f"created: {TODAY}",
        f"updated: {TODAY}",
        "source_ingest: pdf-ocr-upload",
        "issuer: ANRE",
        "legal_status: in_vigoare",
    ]
    if act.get("enabling_act"):
        fm.append(f'enabling_act: "{act["enabling_act"]}"')
    fm.append("---")

    warn = ""
    if not complete:
        warn = (
            "\n> [!warning] OCR / annex check\n"
            "> Text from scanned legis.md PDF via OCR. Verify annex tables and formulas at source before citing.\n"
        )
    if "L107" in act.get("enabling_act", ""):
        warn += (
            "\n> [!danger] L107 currency\n"
            "> Issued under repealed [[Legea 107-2016 — energia electrica (text)|L107/2016]]. "
            "Check whether ANRE re-adopted under [[Legea 164-2025 — energia electrica (text)|L164/2025]].\n"
        )

    header = f"""# {act['title'].replace(' (text)', '')}

> [!info] Sursă & versiune
> Text preluat din **legis.md** PDF (doc_id [{act['legis_id']}](https://www.legis.md/cautare/getResults?lang=ro&doc_id={act['legis_id']})), OCR + structură ușoară.
> Puncte normalizate ca `### Punctul N.` unde OCR permite. Analiză: [[{note}]].
{warn}
---
"""
    text_path.write_text("\n".join(fm) + "\n" + header + "\n" + body + "\n", encoding="utf-8")
    return text_path


def archive_sources(act: dict) -> None:
    SOURCE.mkdir(parents=True, exist_ok=True)
    pdf_src = CURSOR_UPLOADS / act["pdf"]
    ocr_src = CURSOR_UPLOADS / act["ocr"]
    if pdf_src.exists():
        shutil.copy2(pdf_src, SOURCE / f"{act['legis_id']}-{act['pdf']}")
        shutil.copy2(pdf_src, UPLOADS / act["pdf"])
    if ocr_src.exists():
        shutil.copy2(ocr_src, SOURCE / f"{act['legis_id']}.ocr.txt")


def main() -> None:
    UPLOADS.mkdir(exist_ok=True)
    for act in ACTS:
        ocr_path = CURSOR_UPLOADS / act["ocr"]
        if not ocr_path.exists():
            raise SystemExit(f"Missing OCR: {ocr_path}")
        body = load_ocr(ocr_path)
        body, points = normalize_structure(body)
        path = write_text(act, body, points)
        archive_sources(act)
        print({"ingested": path.name, "points": points, "complete": act["complete"]})


if __name__ == "__main__":
    main()
