#!/usr/bin/env python3
"""Ingest 2026-08-07 energy PDF batch 9 (pdftotext from legis.md PDFs)."""

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
        "pdf": "154839_b6cf.pdf",
        "legis_id": "154839",
        "nr": "668",
        "an": 2022,
        "title": "HG 668-2022 — stocuri securitate gaze naturale",
        "mo": "MO 305/30.09.2022 art. 750",
        "domeniu": ["energetică", "gaze", "securitate"],
        "enabling_act": "[[Legea 108-2016 — gazele naturale (text)|L108/2016]] art. 108¹ · LP249/2022 art. VI(11)–(12)",
        "amended_by": "[[HG 364-2024 — modificare stocuri securitate gaze (text)|HG 364/2024]] · [[HG 302-2025 — modificare HG 668-2022 stocuri securitate gaze (text)|HG 302/2025]] · HG 299/2026 (56.3 mcm — amend not yet ingested)",
        "complete": True,
    },
    {
        "kind": "hg",
        "pdf": "154418_6b51.pdf",
        "legis_id": "154418",
        "nr": "852",
        "an": 2024,
        "title": "HG 852-2024 — zone protectie retele electrice",
        "mo": "MO 552-555/27.12.2024 art. 1004",
        "domeniu": ["energetică", "infrastructură", "rețele"],
        "enabling_act": "[[Legea 164-2025 — energia electrica (text)|L164/2025]] art. 4(1)(l), art. 141(1) (remapped by HG 248/2026)",
        "amended_by": "HG 248/2026 (enabling remap + pts 7/40 — amend not yet ingested)",
        "complete": False,
        "continut": "regulament-corp — formulare lipsă",
        "warn": "Regulament body (pct. 1–57) + repeal list (HG Anexa nr. 2) present. Regulation form annexes (cerere / acord models) appear only as placeholders „anexa nr.1/nr.2”.",
    },
    {
        "kind": "law",
        "pdf": "154133_7a85.pdf",
        "legis_id": "154133",
        "nr": "74",
        "an": 2024,
        "title": "Legea 74-2024 — actiuni climatice",
        "mo": "MO 209-212/16.05.2024 art. 293",
        "domeniu": ["climă", "energetică", "GES"],
        "enabling_act": "Organic — ETS Directive 2003/87/CE · Governance Reg. (EU) 2018/1999 (energy union / climate)",
        "amended_by": "[[Legea 53-2026 — reforma autoritatilor Ministerul Mediului (text)|LP53/2026]]",
        "complete": True,
        "organic": True,
    },
    {
        "kind": "law",
        "pdf": "155406_205c.pdf",
        "legis_id": "155406",
        "nr": "75",
        "an": 2026,
        "title": "Legea 75-2026 — cadru institutii publice",
        "mo": "MO 330-333/23.07.2026 art. 331",
        "domeniu": ["administrativ", "instituții"],
        "enabling_act": "Organic framework for public institutions founded by Government / LPA (excl. education, health, culture, etc.)",
        "complete": True,
        "organic": True,
        "warn": "Peripheral to energy cascade — general public-institution law (IF 1.01.2027). May affect governance of energy-related public institutions (e.g. CNED) once within scope.",
    },
    {
        "kind": "law",
        "pdf": "154422_9db1.pdf",
        "legis_id": "154422",
        "nr": "105",
        "an": 2024,
        "title": "Legea 105-2024 — Retea date durabilitate agricola",
        "mo": "MO 210-212/15.05.2026 art. 198",
        "domeniu": ["agricultură", "date", "durabilitate"],
        "enabling_act": "Ordinary — agricultural sustainability data network (Reg. (EU) 1217/2009); republished via LP24/2026",
        "complete": True,
        "organic": False,
        "warn": "Peripheral — agriculture data network (RDDA). Not an energy-cascade act. IF = 24 months after republication (15.05.2026).",
    },
    {
        # Already in vault as legis_id 155511 — archive only, do not overwrite.
        "kind": "hg",
        "pdf": "155290_59ee.pdf",
        "legis_id": "155290",
        "nr": "346",
        "an": 2026,
        "title": "HG 346-2026 — Comisia Nationala Management Crize",
        "mo": "MO 301-304/10.07.2026 art. 369",
        "domeniu": ["administrativ", "crize", "energetică"],
        "complete": True,
        "archive_only": True,
        "warn": "Duplicate of vault HG 346 (preferred legis_id 155511). Archived upload only.",
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
        archive_sources(act, body)
        if act.get("archive_only"):
            print(
                {
                    "archived_only": act["legis_id"],
                    "reason": act.get("warn", "duplicate"),
                    "count": count,
                }
            )
            continue
        path = write_text(act, body, count)
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
