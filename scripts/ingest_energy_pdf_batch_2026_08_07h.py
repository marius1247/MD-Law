#!/usr/bin/env python3
"""Ingest 2026-08-07 energy PDF batch 8 (pdftotext from legis.md PDFs)."""

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
HANRE = ROOT / "10 Legislation/Authority Acts"
TODAY = date.today().isoformat()
CURSOR_UPLOADS = Path("/home/ubuntu/.cursor/projects/workspace/uploads")

ACTS = [
    {
        "kind": "hg",
        "pdf": "152235_287a.pdf",
        "legis_id": "152235",
        "nr": "1059",
        "an": 2023,
        "title": "HG 1059-2023 — PSO securitate aprovizionare energie electrica",
        "mo": "MO 495-496/22.12.2023 art. 1231",
        "domeniu": ["energetică", "securitate", "PSO"],
        "enabling_act": "[[Legea 164-2025 — energia electrica (text)|L164/2025]] art. 4(1)(e), art. 17(3) (remapped by HG 801/2025)",
        "amended_by": "[[HG 156-2025 — modificare HG 1059-2023 PSO securitate EE (text)|HG 156/2025]] · [[HG 801-2025 — modificare HG 1059-2023 PSO securitate EE (text)|HG 801/2025]]",
        "complete": True,
    },
    {
        "kind": "hg",
        "pdf": "152217_ceec.pdf",
        "legis_id": "152217",
        "nr": "801",
        "an": 2025,
        "title": "HG 801-2025 — modificare HG 1059-2023 PSO securitate EE",
        "mo": "MO 633-636/26.12.2025 art. 802",
        "domeniu": ["energetică", "securitate", "PSO"],
        "enabling_act": "[[Legea 164-2025 — energia electrica (text)|L164/2025]] art. 4(1)(e), art. 17(3)",
        "amends": "[[HG 1059-2023 — PSO securitate aprovizionare energie electrica (text)|HG 1059/2023]]",
        "complete": True,
    },
    {
        "kind": "hanre",
        "pdf": "152185_eca9.pdf",
        "legis_id": "152185",
        "nr": "443",
        "an": 2020,
        "title": "HANRE 443-2020 — Metodologie tarife distributie gaze",
        "mo": "MO 332-342/11.12.2020 art. 1312",
        "domeniu": ["energetică", "gaze", "tarife"],
        "enabling_act": "[[Legea 108-2016 — gazele naturale (text)|L108/2016]] art. 7(2)(a), art. 99(2)",
        "amended_by": "[[HANRE 785-2025 — modificare Metodologie tarife distributie gaze 443-2020 (text)|HANRE 785/2025]]",
        "complete": False,
        "continut": "doar-dispozitiv",
        "warn": "Metodologia (anexă) lipsește din PDF — doar dispozitivul de aprobare + nota de modificare HANRE 785/2025. Uniform-tariff overlay is in 785; rate decision HANRE 162/2026.",
    },
    {
        "kind": "hanre",
        "pdf": "153388_a941.pdf",
        "legis_id": "153388",
        "nr": "162",
        "an": 2026,
        "title": "HANRE 162-2026 — tarife uniforme distributie gaze",
        "mo": "MO 112-115/12.03.2026 art. 177",
        "domeniu": ["energetică", "gaze", "tarife"],
        "enabling_act": "[[Legea 108-2016 — gazele naturale (text)|L108/2016]] art. 7(2)(d), 7(42)(b), art. 9(7), art. 98(2)(b), 98(5¹) · [[HANRE 443-2020 — Metodologie tarife distributie gaze (text)|HANRE 443/2020]] (as amended by 785)",
        "complete": True,
    },
    {
        "kind": "law",
        "pdf": "152374_e3f4.pdf",
        "legis_id": "152374",
        "nr": "317",
        "an": 2025,
        "title": "Legea 317-2025 — modificare acte permisive",
        "mo": "MO 646-650/30.12.2025 art. 787",
        "domeniu": ["autorizare", "energetică", "permisive"],
        "enabling_act": "Omnibus amending many acts; energy: L164 art. 20 · LP227 Art. XX/XXV/XLII",
        "amends": "[[Legea 164-2025 — energia electrica (text)|L164/2025]] · [[Legea 227-2025 — optimizarea actelor permisive (text)|LP227/2025]] (+ many non-energy)",
        "complete": True,
        "organic": True,
    },
    {
        "kind": "law",
        "pdf": "154098_09a4.pdf",
        "legis_id": "154098",
        "nr": "53",
        "an": 2026,
        "title": "Legea 53-2026 — reforma autoritatilor Ministerul Mediului",
        "mo": "MO 183-185/25.04.2026 art. 150",
        "domeniu": ["mediu", "instituții", "climă"],
        "enabling_act": "Organic reform of Environment Ministry subordinate authorities; EMAS / environmental accounts (EU)",
        "complete": True,
        "organic": True,
        "warn": "Peripheral to energy cascade — environment/climate institutional reform (GHG inventory, environmental accounts incl. energy-flow module). Ingested for completeness of upload batch.",
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
        m = re.match(r"^Art\.\s*([IVXLCDM]+|\d+)\.\s*[-–]?\s*(.*)$", s, re.I)
        if m:
            num = m.group(1)
            rest = m.group(2)
            art_nums.add(num)
            label = f"Art. {num}" if re.match(r"^[IVXLCDM]+$", num, re.I) else f"Articolul {num}"
            if rest:
                if len(rest) > 120:
                    out.append(f"### {label}.")
                    out.append(rest)
                else:
                    out.append(f"### {label}. {rest}")
            else:
                out.append(f"### {label}.")
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
    if act["kind"] == "law":
        return LAWS
    if act["kind"] == "hanre":
        return HANRE
    return HG


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
    elif act["kind"] == "hanre":
        instrument = "act_type: hotărâre-anre"
        count_field = f"puncte_numarate: {count}"
        puncte = "articole_numarate: 0"
        extra = "issuer: ANRE"
    else:
        instrument = "act_type: hotărâre-guvern"
        count_field = f"puncte_numarate: {count}"
        puncte = "articole_numarate: 0"
        extra = "issuer: Guvern"

    tags = ["act", "text", "acte_normative", "energetică"]
    if act["kind"] == "hanre":
        tags.append("ANRE")

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
    for key in ("amended_by", "amends", "enables"):
        if act.get(key):
            fm.append(f'{key}: "{act[key]}"')
    if not complete:
        fm.append(f"status_ingestie: {continut}")
    fm.append("---")

    warn = ""
    if act.get("warn"):
        warn = f"\n> [!warning] Completeness\n> {act['warn']}\n"

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
