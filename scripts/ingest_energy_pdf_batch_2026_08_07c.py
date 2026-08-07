#!/usr/bin/env python3
"""Ingest 2026-08-07 energy PDF batch 3 (pdftotext from legis.md PDFs)."""

from __future__ import annotations

import re
import shutil
import subprocess
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
UPLOADS = ROOT / "uploads"
SOURCE = ROOT / "99 Attachments/source-legis"
HG = ROOT / "10 Legislation/Government Decisions"
AUTH = ROOT / "10 Legislation/Authority Acts"
TODAY = date.today().isoformat()
CURSOR_UPLOADS = Path("/home/ubuntu/.cursor/projects/workspace/uploads")

ACTS = [
    {
        "kind": "hanre",
        "pdf": "145047_2db0.pdf",
        "legis_id": "145047",
        "nr": "355",
        "an": 2021,
        "title": "HANRE 355-2021 — preturi reglementate furnizare gaze",
        "mo": "MO 249-253/15.10.2021 art. 1214",
        "domeniu": ["energetică", "gaze", "tarife"],
        "enabling_act": "[[Legea 108-2016 — gazele naturale (text)|L108/2016]] art. 7(2)(a), art. 99(2)",
        "amended_by": "[[HANRE 540-2024 — modificare Metodologie preturi furnizare gaze (notă)|540/2024]]",
        "complete": False,
        "continut": "doar-dispozitiv",
    },
    {
        "kind": "hanre",
        "pdf": "145000_2231.pdf",
        "legis_id": "145000",
        "nr": "540",
        "an": 2024,
        "title": "HANRE 540-2024 — modificare Metodologie preturi furnizare gaze",
        "mo": "MO 392-394/12.09.2024 art. 715",
        "domeniu": ["energetică", "gaze", "tarife"],
        "enabling_act": "[[Legea 108-2016 — gazele naturale (text)|L108/2016]] art. 7(2)",
        "enables": "[[HANRE 355-2021 — preturi reglementate furnizare gaze (text)|355/2021]]",
        "complete": True,
    },
    {
        "kind": "hg",
        "pdf": "145173_1ee0.pdf",
        "legis_id": "145173",
        "nr": "621",
        "an": 2024,
        "title": "HG 621-2024 — certificare performanta energetica cladiri",
        "mo": "MO 408-410/26.09.2024 art. 772",
        "domeniu": ["energetică", "eficiență", "clădiri"],
        "enabling_act": "Legea nr. 282/2023 privind performanța energetică a clădirilor art. 5(1)(4)",
        "complete": True,
    },
    {
        "kind": "hg",
        "pdf": "145229_4d0e.pdf",
        "legis_id": "145229",
        "nr": "622",
        "an": 2024,
        "title": "HG 622-2024 — calificare evaluatori energetici",
        "mo": "MO 414-417/03.10.2024 art. 782",
        "domeniu": ["energetică", "eficiență", "clădiri"],
        "enabling_act": "Legea nr. 282/2023 privind performanța energetică a clădirilor art. 5(1)(3)",
        "complete": True,
    },
    {
        "kind": "hg",
        "pdf": "143426_d0f6.pdf",
        "legis_id": "143426",
        "nr": "364",
        "an": 2024,
        "title": "HG 364-2024 — modificare stocuri securitate gaze",
        "mo": "MO 236-237/31.05.2024 art. 483",
        "domeniu": ["energetică", "gaze", "securitate"],
        "enabling_act": "[[Legea 108-2016 — gazele naturale (text)|L108/2016]] art. 4(21), art. 108¹ · L249/2022",
        "amends": "HG 668/2022 stocuri securitate gaze naturale",
        "complete": True,
    },
    {
        "kind": "hg",
        "pdf": "145465_fdd5.pdf",
        "legis_id": "145465",
        "nr": "677",
        "an": 2024,
        "title": "HG 677-2024 — plan sezon incalzire 2024-2025",
        "mo": "MO 437-439/18.10.2024 art. 825",
        "domeniu": ["energetică", "gaze", "securitate", "criză"],
        "enabling_act": "[[Legea 174-2017 — energetica (text)|L174/2017]] art. 4(1)(e) · [[Legea 108-2016 — gazele naturale (text)|L108/2016]] art. 108²(3)-(4)",
        "complete": False,
        "continut": "doar-dispozitiv",
    },
]


def extract_pdf_text(pdf_path: Path) -> str:
    proc = subprocess.run(
        ["pdftotext", str(pdf_path), "-"],
        capture_output=True,
        text=True,
        check=True,
    )
    return clean_text(proc.stdout)


def clean_text(raw: str) -> str:
    text = raw.replace("\x0c", "\n\n")
    text = re.sub(r"\n{4,}", "\n\n\n", text)
    return text.strip() + "\n"


def normalize_points(body: str) -> tuple[str, int]:
    lines = body.splitlines()
    out: list[str] = []
    point_nums: set[str] = set()
    for line in lines:
        s = line.strip()
        m = re.match(r"^CAPITOLUL\s+([IVXLCDM]+|\d+)\s*$", s, re.I)
        if m:
            out.append(f"## Capitolul {m.group(1)}")
            continue
        m = re.match(r"^Capitolul\s+([IVXLCDM]+|\d+)\s*$", s, re.I)
        if m:
            out.append(f"## Capitolul {m.group(1)}")
            continue
        m = re.match(r"^Secţiunea\s+(\d+)\s*$", s, re.I)
        if m:
            out.append(f"### Secțiunea {m.group(1)}")
            continue
        m = re.match(r"^Sectiunea\s+(\d+)\s*$", s, re.I)
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


def dest_dir(act: dict) -> Path:
    return AUTH if act["kind"] == "hanre" else HG


def write_text(act: dict, body: str, count: int) -> Path:
    title = f"{act['title']} (text)"
    note = f"{act['title']} (notă)"
    path = dest_dir(act) / f"{title}.md"
    domain_yaml = "\n".join(f"- {d}" for d in act["domeniu"])
    complete = act["complete"]
    continut = act.get("continut", "text-integral" if complete else "partial")

    if act["kind"] == "hanre":
        instrument = "instrument: act-anre\nact_type: hotărâre-anre"
        count_field = f"puncte_numarate: {count}"
        puncte = "articole_numarate: 0"
        extra = "forta_juridica: 8\nissuer: ANRE"
    else:
        instrument = "act_type: hotărâre-guvern"
        count_field = f"puncte_numarate: {count}"
        puncte = "articole_numarate: 0"
        extra = "issuer: Guvern"

    fm = [
        "---",
        f'title: "{title}"',
        "type: act-text",
        instrument,
        f'nr: "{act["nr"]}"',
        f"an: {act['an']}",
        "domeniu:",
        domain_yaml,
        f"domain: [{', '.join(act['domeniu'])}]",
        extra,
        "in_force: true",
        "in_vigoare: true",
        f'mo_publicare: "{act["mo"]}"',
        f'legis_id: "{act["legis_id"]}"',
        f'legis_url: "https://www.legis.md/cautare/getResults?lang=ro&doc_id={act["legis_id"]}"',
        f"version_date: {TODAY}",
        f"versiune_text: {TODAY}",
        f"continut: {continut}",
        f"text_complet: {'true' if complete else 'false'}",
        count_field,
        puncte,
        "tags: [act, text, acte_normative, energetică]",
        f"created: {TODAY}",
        f"updated: {TODAY}",
        "source_ingest: pdf-upload-pdftotext",
        "legal_status: in_vigoare",
    ]
    if act.get("enabling_act"):
        fm.append(f'enabling_act: "{act["enabling_act"]}"')
    for key in ("amended_by", "enables", "amends"):
        if act.get(key):
            fm.append(f'{key}: "{act[key]}"')
    if not complete and act["kind"] == "hanre":
        fm.append("status_ingestie: DECIZIE ONLY — metodologia/anexa absentă din PDF")
    if not complete and act["kind"] == "hg":
        fm.append("status_ingestie: dispozitiv complet — anexele lipsesc")
    fm.append("---")

    warn = ""
    if not complete:
        if act["kind"] == "hanre":
            warn = (
                "\n> [!danger] Anexa / metodologia lipsește\n"
                "> PDF conține **doar dispozitivul** hotărârii. Metodologia (anexă) nu este inclusă.\n"
            )
        else:
            warn = (
                "\n> [!warning] Anexele lipsesc\n"
                "> PDF conține dispozitivul hotărârii; anexele nr. 1–2 (componență comisie + plan măsuri) "
                "nu sunt incluse.\n"
            )

    header = f"""# {act['title'].replace(' (text)', '')}

> [!info] Sursă & versiune
> Text preluat din **legis.md** PDF (doc_id [{act['legis_id']}](https://www.legis.md/cautare/getResults?lang=ro&doc_id={act['legis_id']})), pdftotext + structură ușoară.
> Analiză: [[{note}]].
{warn}
---
"""
    path.write_text("\n".join(fm) + "\n" + header + "\n" + body + "\n", encoding="utf-8")
    return path


def archive_sources(act: dict, body: str) -> None:
    SOURCE.mkdir(parents=True, exist_ok=True)
    UPLOADS.mkdir(exist_ok=True)
    pdf_src = CURSOR_UPLOADS / act["pdf"]
    if pdf_src.exists():
        shutil.copy2(pdf_src, SOURCE / f"{act['legis_id']}-{act['pdf']}")
        shutil.copy2(pdf_src, UPLOADS / act["pdf"])
        (SOURCE / f"{act['legis_id']}.txt").write_text(body, encoding="utf-8")


def main() -> None:
    for act in ACTS:
        pdf_path = CURSOR_UPLOADS / act["pdf"]
        if not pdf_path.exists():
            raise SystemExit(f"Missing PDF: {pdf_path}")
        body = extract_pdf_text(pdf_path)
        body, count = normalize_points(body)
        path = write_text(act, body, count)
        archive_sources(act, body)
        print({"ingested": path.name, "kind": act["kind"], "count": count, "complete": act["complete"]})


if __name__ == "__main__":
    main()
