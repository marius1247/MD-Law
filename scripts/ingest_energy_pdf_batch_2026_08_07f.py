#!/usr/bin/env python3
"""Ingest 2026-08-07 energy PDF batch 6 (pdftotext from legis.md PDFs)."""

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
        "pdf": "148815_4cf9.pdf",
        "legis_id": "148815",
        "nr": "329",
        "an": 2025,
        "title": "HG 329-2025 — modificare HG 401-2021 cote capacitate regenerabile",
        "mo": "MO 301-304/06.06.2025 art. 332",
        "domeniu": ["energetică", "regenerabile", "facturare netă"],
        "enabling_act": "[[Legea 10-2016 — surse regenerabile (text)|L10/2016]] art. 10(1)(e)(e1)(i)",
        "amends": "HG 401/2021 (RES capacity limits/quotas to 31.12.2025) — parent not in vault",
        "complete": False,
        "continut": "dispozitiv — anexa nr. 2 lipsă",
        "warn": "Anexa nr. 2 (plafoane/cote facturare netă) lipsește din PDF — placeholder „anexa nr.2”.",
    },
    {
        "kind": "hanre",
        "pdf": "149130_5fcb.pdf",
        "legis_id": "149130",
        "nr": "422",
        "an": 2019,
        "title": "HANRE 422-2019 — calitate servicii transport distributie gaze",
        "mo": "MO 14-23/24.01.2020 art. 62",
        "domeniu": ["energetică", "gaze", "calitate"],
        "enabling_act": "[[Legea 108-2016 — gazele naturale (text)|L108/2016]] art. 7(1)(l), art. 68",
        "amended_by": "[[HANRE 328-2025 — modificare Codul retelelor de gaze naturale (notă)|HANRE 328/2025]]",
        "complete": False,
        "continut": "doar-dispozitiv",
        "warn": "Regulamentul (anexă) lipsește din PDF — doar dispozitivul de aprobare + nota de modificare HANRE 328/2025.",
    },
    {
        "kind": "law",
        "pdf": "150581_da5b.pdf",
        "legis_id": "150581",
        "nr": "227",
        "an": 2025,
        "title": "Legea 227-2025 — optimizarea actelor permisive",
        "mo": "MO 467-470/05.09.2025 art. 629",
        "domeniu": ["autorizare", "energetică", "permisive"],
        "enabling_act": "Omnibus amending many acts incl. L461, L92, L10, L108, L160",
        "amends": "[[Legea 461-2001 — piata produselor petroliere (text)|L461]] · [[Legea 92-2014 — energia termica si cogenerarea (text)|L92]] · [[Legea 10-2016 — surse regenerabile (text)|L10]] · [[Legea 108-2016 — gazele naturale (text)|L108]] · [[Legea 160-2011 — reglementarea prin autorizare (text)|L160]] (+ many non-energy)",
        "amended_by": "LP317/2025 (Art. XLII IF tweak)",
        "complete": True,
        "organic": True,
    },
    {
        "kind": "hg",
        "pdf": "150831_eeb7.pdf",
        "legis_id": "150831",
        "nr": "596",
        "an": 2025,
        "title": "HG 596-2025 — infrastructura transport EE autorizare centrale echilibrare",
        "mo": "MO 494-497/19.09.2025 art. 614",
        "domeniu": ["energetică", "infrastructură", "racordare", "echilibrare"],
        "enabling_act": "[[Legea 164-2025 — energia electrica (text)|L164/2025]] art. 4(1)(g) · Legea 136/2017 · Legea 120/2022 (Vulcănești–Chișinău)",
        "amends": "HG 1037/2023 · HG 517/2024 · [[HG 26-2025 — PSO acces retea producatori regenerabile pret fix (text)|HG 26/2025]]",
        "complete": True,
    },
    {
        "kind": "law",
        "pdf": "148399_4415.pdf",
        "legis_id": "148399",
        "nr": "88",
        "an": 2025,
        "title": "Legea 88-2025 — utilitate publica LEA 400 kV Balti-Suceava",
        "mo": "MO 229-232/15.05.2025 art. 269",
        "domeniu": ["energetică", "infrastructură", "expropriere"],
        "enabling_act": "Legea 488/1999 expropriere art. 5, 6",
        "complete": True,
        "organic": True,
    },
    {
        "kind": "hg",
        "pdf": "148535_1749.pdf",
        "legis_id": "148535",
        "nr": "302",
        "an": 2025,
        "title": "HG 302-2025 — modificare HG 668-2022 stocuri securitate gaze",
        "mo": "MO 245-248/22.05.2025 art. 299",
        "domeniu": ["energetică", "gaze", "securitate"],
        "enabling_act": "[[Legea 108-2016 — gazele naturale (text)|L108/2016]] art. 4(2¹), art. 108¹",
        "amends": "HG 668/2022 (gas security stocks) — parent not in vault; prior patch [[HG 364-2024 — modificare stocuri securitate gaze (text)|HG 364/2024]]",
        "complete": True,
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
    if act["legis_id"] == "150831":
        warn += (
            "\n> [!danger] HANRE 168 currency inside amend\n"
            "> Pt. 3 still cites [[HANRE 168-2019 — racordarea la retelele electrice (text)|HANRE 168/2019]] "
            "(abrogated). Remap connection procedure to [[HANRE 311-2026 — racordarea la retelele electrice (text)|311/2026]].\n"
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
