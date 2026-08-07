#!/usr/bin/env python3
"""Ingest 2026-08-07 energy PDF batch 7 (pdftotext from legis.md PDFs)."""

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
        "pdf": "152035_cba8.pdf",
        "legis_id": "152035",
        "nr": "1060",
        "an": 2023,
        "title": "HG 1060-2023 — organizare functionare CNED",
        "mo": "MO 515-518/30.12.2023 art. 1276",
        "domeniu": ["energetică", "eficiență", "instituții"],
        "enabling_act": "[[Legea 139-2018 — eficienta energetica (text)|L139/2018]] art. 9(1)(h), art. 11 · Legea 136/2017 · Legea 98/2012",
        "amended_by": "HG 765/2025",
        "complete": False,
        "continut": "statut+structura — anexa 4 modificări trunchiată la final",
        "warn": "Statut (anexa 1) + structură (anexa 2) prezente. Anexa 4 (modificări HG conexe) se oprește mid-sentence la HG 676/2020 — verificare la sursă.",
    },
    {
        "kind": "hanre",
        "pdf": "152132_8972.pdf",
        "legis_id": "152132",
        "nr": "23",
        "an": 2017,
        "title": "HANRE 23-2017 — furnizarea energiei termice",
        "mo": "MO 316-321/25.08.2017 art. 1581",
        "domeniu": ["energetică", "termică", "furnizare"],
        "enabling_act": "[[Legea 92-2014 — energia termica si cogenerarea (text)|L92/2014]] art. 39(1)",
        "amended_by": "HANRE 792/2023",
        "complete": False,
        "continut": "regulament-corp — anexe formulare lipsă",
        "warn": "Corpul Regulamentului (pct. 1–175) este prezent. Anexele nr. 1–3 (formulare) apar doar ca placeholder.",
    },
    {
        "kind": "hanre",
        "pdf": "152152_f7c1.pdf",
        "legis_id": "152152",
        "nr": "785",
        "an": 2025,
        "title": "HANRE 785-2025 — modificare Metodologie tarife distributie gaze 443-2020",
        "mo": "MO 626-629/23.12.2025 art. 1122",
        "domeniu": ["energetică", "gaze", "tarife"],
        "enabling_act": "[[Legea 108-2016 — gazele naturale (text)|L108/2016]] art. 7(2)(a), art. 99(5¹), art. 99³(2)",
        "amends": "HANRE 443/2020 gas DSO tariff methodology — parent not in vault",
        "complete": True,
    },
    {
        "kind": "hg",
        "pdf": "150832_b5ff.pdf",
        "legis_id": "150832",
        "nr": "599",
        "an": 2025,
        "title": "HG 599-2025 — limite cote capacitate regenerabile pana 2030",
        "mo": "MO 494-497/19.09.2025 art. 615",
        "domeniu": ["energetică", "regenerabile", "facturare netă"],
        "enabling_act": "[[Legea 10-2016 — surse regenerabile (text)|L10/2016]] art. 10(1)(e)(e1)(i), art. 34, 39¹, 39²",
        "amends": "Abrogates HG 401/2021 (as amended, incl. [[HG 329-2025 — modificare HG 401-2021 cote capacitate regenerabile (text)|HG 329/2025]])",
        "complete": False,
        "continut": "dispozitiv — anexe 1–2 lipsă",
        "warn": "Anexele nr. 1 (limite/cote sprijin) și nr. 2 (plafoane facturare netă) lipsesc — doar placeholder. Dispozitivul abrogă HG 401/2021.",
    },
    {
        "kind": "hg",
        "pdf": "150858_cc59.pdf",
        "legis_id": "150858",
        "nr": "517",
        "an": 2024,
        "title": "HG 517-2024 — Regulament constructie reconstructie centrale electrice",
        "mo": "MO 347-349/09.08.2024 art. 680",
        "domeniu": ["energetică", "autorizare", "infrastructură"],
        "enabling_act": "[[Legea 164-2025 — energia electrica (text)|L164/2025]] art. 4(1)(g) (as remapped by HG 596/2025)",
        "amended_by": "[[HG 596-2025 — infrastructura transport EE autorizare centrale echilibrare (notă)|HG 596/2025]]",
        "complete": True,
    },
    {
        "kind": "hg",
        "pdf": "150977_a64d.pdf",
        "legis_id": "150977",
        "nr": "620",
        "an": 2025,
        "title": "HG 620-2025 — transmitere bunuri Fond eficienta energetica CNED",
        "mo": "MO 506-509/26.09.2025 art. 641",
        "domeniu": ["energetică", "eficiență", "CNED"],
        "enabling_act": "[[Legea 139-2018 — eficienta energetica (text)|L139/2018]] art. 8(12¹)",
        "complete": False,
        "continut": "regulament-corp — anexe formulare lipsă",
        "warn": "Corpul Regulamentului (pct. 1–17) prezent. Anexele-formulare apar doar ca placeholder. MO header in PDF may show 26.09.2026 — treat as 2025 publication pending source check.",
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
    if act["kind"] == "hanre":
        return HANRE
    if act["kind"] == "law":
        return LAWS
    return HG


def write_text(act: dict, body: str, count: int) -> Path:
    title = f"{act['title']} (text)"
    note = f"{act['title']} (notă)"
    path = dest_dir(act) / f"{title}.md"
    domain_yaml = "\n".join(f"- {d}" for d in act["domeniu"])
    complete = act["complete"]
    continut = act.get("continut", "text-integral" if complete else "partial")

    if act["kind"] == "hanre":
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
    if act["legis_id"] == "152035":
        warn += (
            "\n> [!danger] Possible truncation\n"
            "> File ends mid-amendment of HG 676/2020 inside annex 4. Do not assume the annex-4 package is complete.\n"
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
