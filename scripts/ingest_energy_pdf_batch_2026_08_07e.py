#!/usr/bin/env python3
"""Ingest 2026-08-07 energy PDF batch 5 (pdftotext from legis.md PDFs)."""

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
        "kind": "hg",
        "pdf": "147685_943f.pdf",
        "legis_id": "147685",
        "nr": "86",
        "an": 2025,
        "title": "HG 86-2025 — Plan national integrat energie clima 2025-2030",
        "mo": "MO 151-153/25.03.2025 art. 159",
        "domeniu": ["energetică", "climă", "planificare"],
        "enabling_act": "[[Legea 174-2017 — energetica (text)|L174/2017]] art. 72(7) · [[Legea 10-2016 — surse regenerabile (text)|L10/2016]] art. 9 · [[Legea 74-2024]] art. 9(g) · [[HG 10-2024 — guvernanta energetica si actiuni climatice (text)|HG 10/2024]]",
        "complete": False,
        "continut": "doar-dispozitiv",
        "warn": "Anexa PNIEC 2025–2030 lipsește din PDF (doar placeholder „planul național”).",
    },
    {
        "kind": "hg",
        "pdf": "147714_dab3.pdf",
        "legis_id": "147714",
        "nr": "156",
        "an": 2025,
        "title": "HG 156-2025 — modificare HG 1059-2023 PSO securitate EE",
        "mo": "MO 154-156/27.03.2025 art. 162",
        "domeniu": ["energetică", "securitate", "PSO"],
        "enabling_act": "[[Legea 107-2016 — energia electrica (text)|L107/2016]] art. 4(1)(e), art. 11(1) — remap [[Legea 164-2025 — energia electrica (text)|L164/2025]]",
        "amends": "HG 1059/2023 (PSO security of electricity supply) — parent not yet in vault",
        "complete": True,
    },
    {
        "kind": "hg",
        "pdf": "147716_966a.pdf",
        "legis_id": "147716",
        "nr": "158",
        "an": 2025,
        "title": "HG 158-2025 — modificare norme cheltuieli institutii sociale",
        "mo": "MO 154-156/27.03.2025 art. 164",
        "domeniu": ["social", "buget"],
        "enabling_act": "HG 520/2006 (parent not in vault)",
        "complete": False,
        "continut": "doar-dispozitiv",
        "peripheral": True,
        "warn": "Anexa (norme de cheltuieli) lipsește din PDF. Act social/bugetar — periferic față de cascada energetică.",
    },
    {
        "kind": "law",
        "pdf": "147843_3f1e.pdf",
        "legis_id": "147843",
        "nr": "45",
        "an": 2025,
        "title": "Legea 45-2025 — garantiile avizelor de racordare si tolerante dezechilibre",
        "mo": "MO 154-156/27.03.2025 art. 165",
        "domeniu": ["energetică", "racordare", "regenerabile", "dezechilibre"],
        "enabling_act": "Amends [[Legea 107-2016 — energia electrica (text)|L107/2016]] art. 47, 88 and [[Legea 10-2016 — surse regenerabile (text)|L10/2016]] art. 37(7)",
        "amends": "[[Legea 107-2016 — energia electrica (text)|L107/2016]] · [[Legea 10-2016 — surse regenerabile (text)|L10/2016]]",
        "complete": True,
        "organic": True,
    },
    {
        "kind": "hg",
        "pdf": "148066_6246.pdf",
        "legis_id": "148066",
        "nr": "197",
        "an": 2025,
        "title": "HG 197-2025 — metodologie cogenerare inalta eficienta garantii origine",
        "mo": "MO 187-189/17.04.2025 art. 205",
        "domeniu": ["energetică", "cogenerare", "eficiență", "garanții de origine"],
        "enabling_act": "[[Legea 92-2014 — energia termica si cogenerarea (text)|L92/2014]] art. 7, 8, 14, 42(12) · Legea 1402/2002 art. 13(1)(b)",
        "amends": "HG 297/2016 (harmonised efficiency reference values) · Regulamentul servicii comunale HG 191/2002 area",
        "complete": False,
        "continut": "dispozitiv+modificari — anexa Metodologie lipsă",
        "warn": "Anexa „Metodologie…” lipsește din PDF (doar placeholder). Dispozitivul + modificările la HG 297/2016 (tabele referință) și la regulamentul serviciilor comunale sunt prezente.",
        "eu": "Delegated Regulation (EU) 2023/2104 amending (EU) 2015/2402 (Dir. 2012/27/EU)",
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
        m = re.match(r"^Art\.\s*([IVXLCDM]+)\.\s*[-–]?\s*(.*)$", s, re.I)
        if m:
            num = m.group(1)
            rest = m.group(2)
            art_nums.add(num)
            if rest:
                if len(rest) > 120:
                    out.append(f"### Art. {num}.")
                    out.append(rest)
                else:
                    out.append(f"### Art. {num}. {rest}")
            else:
                out.append(f"### Art. {num}.")
            continue
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
        act_type = "lege-organică" if act.get("organic") else "lege-ordinară"
        instrument = f"act_type: {act_type}"
        count_field = f"articole_numarate: {count}"
        puncte = "puncte_numarate: 0"
        extra = "forta_juridica: 3\nissuer: Parlament"
    else:
        instrument = "act_type: hotărâre-guvern"
        count_field = f"puncte_numarate: {count}"
        puncte = "articole_numarate: 0"
        extra = "issuer: Guvern"

    tags = ["act", "text", "acte_normative"]
    if not act.get("peripheral"):
        tags.append("energetică")
    if "racordare" in act["domeniu"]:
        tags.append("racordare")

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
        f"tags: [{', '.join(tags)}]",
        f"created: {TODAY}",
        f"updated: {TODAY}",
        "source_ingest: pdf-upload-pdftotext",
        "legal_status: in_vigoare",
    ]
    if act.get("enabling_act"):
        fm.append(f'enabling_act: "{act["enabling_act"]}"')
    for key in ("amended_by", "amends", "enables", "eu"):
        if act.get(key):
            fm.append(f'{key}: "{act[key]}"')
    if not complete:
        fm.append(f"status_ingestie: {continut}")
    fm.append("---")

    warn = ""
    if act.get("warn"):
        level = "warning" if not act.get("peripheral") else "note"
        warn = f"\n> [!{level}] Completeness\n> {act['warn']}\n"
    if act.get("kind") == "law" or "L107" in act.get("enabling_act", ""):
        if "107" in act.get("enabling_act", "") or act.get("legis_id") == "147843":
            warn += (
                "\n> [!danger] L107 currency\n"
                "> This act amends / cites **L107/2016**, repealed 19.08.2025 by "
                "[[Legea 164-2025 — energia electrica (text)|L164/2025]]. "
                "Map operative connection / tariff rules to L164 + [[HANRE 311-2026 — racordarea la retelele electrice (text)|HANRE 311/2026]] for 2026 advice.\n"
            )

    header = f"""# {act['title']}

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
        print(
            {
                "ingested": path.name,
                "kind": act["kind"],
                "count": count,
                "complete": act["complete"],
            }
        )


if __name__ == "__main__":
    main()
