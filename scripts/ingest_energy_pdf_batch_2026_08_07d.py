#!/usr/bin/env python3
"""Ingest 2026-08-07 energy PDF batch 4 (pdftotext from legis.md PDFs)."""

from __future__ import annotations

import re
import shutil
import subprocess
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
UPLOADS = ROOT / "uploads"
SOURCE = ROOT / "99 Attachments/source-legis"
LAWS = ROOT / "10 Legislation/Laws"
HG = ROOT / "10 Legislation/Government Decisions"
TODAY = date.today().isoformat()
CURSOR_UPLOADS = Path("/home/ubuntu/.cursor/projects/workspace/uploads")

ACTS = [
    {
        "kind": "law",
        "pdf": "145809_e017.pdf",
        "legis_id": "145809",
        "nr": "241",
        "an": 2022,
        "title": "Legea 241-2022 — Fond reducere vulnerabilitate energetica",
        "mo": "MO 246-250/05.08.2022 art. 498",
        "domeniu": ["energetică", "vulnerabilitate", "social"],
        "enabling_act": "Framework for Energy Vulnerability Reduction Fund",
        "amended_by": "[[Legea 255-2024 — modificare Legea 241-2022 Fond vulnerabilitate energetica (notă)|255/2024]]",
        "complete": True,
    },
    {
        "kind": "law",
        "pdf": "145800_6bec.pdf",
        "legis_id": "145800",
        "nr": "255",
        "an": 2024,
        "title": "Legea 255-2024 — modificare Legea 241-2022 Fond vulnerabilitate energetica",
        "mo": "MO 477-480/20.11.2024 art. 643",
        "domeniu": ["energetică", "vulnerabilitate", "social"],
        "enabling_act": "[[Legea 241-2022 — Fond reducere vulnerabilitate energetica (text)|241/2022]]",
        "complete": True,
    },
    {
        "kind": "hg",
        "pdf": "145466_995c.pdf",
        "legis_id": "145466",
        "nr": "365",
        "an": 2024,
        "title": "HG 365-2024 — obligatie stocare gaze naturale",
        "mo": "MO 238-240/06.06.2024 art. 486",
        "domeniu": ["energetică", "gaze", "securitate"],
        "enabling_act": "[[Legea 108-2016 — gazele naturale (text)|L108/2016]] art. 4(21), art. 108²-108³",
        "amended_by": "[[HG 677-2024 — plan sezon incalzire 2024-2025 (notă)|677/2024]] (pt. 4)",
        "complete": True,
    },
    {
        "kind": "hg",
        "pdf": "146623_0d0d.pdf",
        "legis_id": "146623",
        "nr": "829",
        "an": 2024,
        "title": "HG 829-2024 — audit energetic intreprinderi mari",
        "mo": "MO 1-4/03.01.2025 art. 1",
        "domeniu": ["energetică", "eficiență", "audit"],
        "enabling_act": "[[Legea 139-2018 — eficienta energetica (text)|L139/2018]] art. 9(1)(g)",
        "complete": True,
    },
    {
        "kind": "hg",
        "pdf": "146906_1935.pdf",
        "legis_id": "146906",
        "nr": "26",
        "an": 2025,
        "title": "HG 26-2025 — PSO acces retea producatori regenerabile pret fix",
        "mo": "MO 22-24/30.01.2025 art. 34",
        "domeniu": ["energetică", "regenerabile", "racordare"],
        "enabling_act": "[[Legea 10-2016 — surse regenerabile (text)|L10/2016]] art. 10(2) · [[Legea 107-2016 — energia electrica (text)|L107/2016]] art. 11(2)-(3)",
        "complete": True,
    },
    {
        "kind": "hg",
        "pdf": "147068_ffdc.pdf",
        "legis_id": "147068",
        "nr": "53",
        "an": 2025,
        "title": "HG 53-2025 — durabilitate biocarburanti emisii GES",
        "mo": "MO 43-46/11.02.2025 art. 68",
        "domeniu": ["energetică", "regenerabile", "transport", "climat"],
        "enabling_act": "[[Legea 10-2016 — surse regenerabile (text)|L10/2016]] art. 10(k2), art. 12(a), art. 33(2)",
        "complete": True,
    },
    {
        "kind": "hg",
        "pdf": "147296_a54f.pdf",
        "legis_id": "147296",
        "nr": "74",
        "an": 2025,
        "title": "HG 74-2025 — calcul consum energie regenerabila",
        "mo": "MO 100-103/28.02.2025 art. 98",
        "domeniu": ["energetică", "regenerabile", "statistică"],
        "enabling_act": "[[Legea 10-2016 — surse regenerabile (text)|L10/2016]] art. 10(k1)",
        "complete": False,
        "continut": "doar-dispozitiv",
    },
    {
        "kind": "hg",
        "pdf": "147150_341b.pdf",
        "legis_id": "147150",
        "nr": "76",
        "an": 2025,
        "title": "HG 76-2025 — cotizatii organizatii internationale 2025",
        "mo": "MO 6/20.02.2025 art. 78",
        "domeniu": ["buget", "internațional"],
        "enabling_act": "Legea bugetului de stat 310/2024 art. 3(a)",
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
    text = proc.stdout.replace("\x0c", "\n\n")
    text = re.sub(r"\n{4,}", "\n\n\n", text)
    return text.strip() + "\n"


def normalize_law(body: str) -> tuple[str, int]:
    lines = body.splitlines()
    out: list[str] = []
    art_nums: set[str] = set()
    for line in lines:
        s = line.strip()
        m = re.match(r"^Articolul\s+(\d+[¹²³]?\d*)\.\s*(.*)$", s, re.I)
        if m:
            num = m.group(1)
            rest = m.group(2)
            art_nums.add(num)
            if rest:
                if len(rest) > 120:
                    out.append(f"### Articolul {num}.")
                    out.append(rest)
                else:
                    out.append(f"### Articolul {num}. {rest}")
            else:
                out.append(f"### Articolul {num}.")
            continue
        m = re.match(r"^Art\.\s*([IVXLCDM]+|\d+[¹²³]?\d*)\.\s*[-–]?\s*(.*)$", s, re.I)
        if m:
            num = m.group(1)
            rest = m.group(2)
            art_nums.add(num)
            if rest:
                if len(rest) > 120:
                    out.append(f"### Articolul {num}.")
                    out.append(rest)
                else:
                    out.append(f"### Articolul {num}. {rest}")
            else:
                out.append(f"### Articolul {num}.")
            continue
        m = re.match(r"^Capitolul\s+([IVXLCDM]+|\d+)\s*$", s, re.I)
        if m:
            out.append(f"## Capitolul {m.group(1)}")
            continue
        out.append(line)
    return "\n".join(out), len(art_nums)


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
    return LAWS if act["kind"] == "law" else HG


def write_text(act: dict, body: str, count: int) -> Path:
    title = f"{act['title']} (text)"
    note = f"{act['title']} (notă)"
    path = dest_dir(act) / f"{title}.md"
    domain_yaml = "\n".join(f"- {d}" for d in act["domeniu"])
    complete = act["complete"]
    continut = act.get("continut", "text-integral" if complete else "partial")

    if act["kind"] == "law":
        instrument = "act_type: lege-organică"
        count_field = f"articole_numarate: {count}"
        puncte = "puncte_numarate: 0"
        extra = "forta_juridica: 3\nissuer: Parlament"
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
    for key in ("amended_by", "amends", "enables"):
        if act.get(key):
            fm.append(f'{key}: "{act[key]}"')
    if not complete:
        fm.append("status_ingestie: dispozitiv complet — anexa/listă lipsă")
    fm.append("---")

    warn = ""
    if not complete:
        if act["legis_id"] == "147296":
            warn = "\n> [!warning] Anexa lipsește\n> Regulamentul privind calculul consumului de energie din surse regenerabile (anexă) nu este în PDF.\n"
        elif act["legis_id"] == "147150":
            warn = "\n> [!note] Anexa listă lipsă\n> Lista organizațiilor internaționale (anexă) nu este în PDF. Act bugetar periferic față de cascada energetică.\n"
    if "L107" in act.get("enabling_act", ""):
        warn += (
            "\n> [!danger] L107 currency\n"
            "> Enabling cite references **L107/2016**. Map to [[Legea 164-2025 — energia electrica (text)|L164/2025]] for 2026 advice.\n"
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
        if act["kind"] == "law":
            body, count = normalize_law(body)
        else:
            body, count = normalize_points(body)
        path = write_text(act, body, count)
        archive_sources(act, body)
        print({"ingested": path.name, "kind": act["kind"], "count": count, "complete": act["complete"]})


if __name__ == "__main__":
    main()
