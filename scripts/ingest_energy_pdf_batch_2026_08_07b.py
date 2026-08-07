#!/usr/bin/env python3
"""Ingest 2026-08-07 energy PDF batch 2 (OCR from legis.md image PDFs)."""

from __future__ import annotations

import re
import shutil
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
UPLOADS = ROOT / "uploads"
SOURCE = ROOT / "99 Attachments/source-legis"
LAWS = ROOT / "10 Legislation/Laws"
HG = ROOT / "10 Legislation/Government Decisions"
AUTH = ROOT / "10 Legislation/Authority Acts"
TODAY = date.today().isoformat()
CURSOR_UPLOADS = Path("/home/ubuntu/.cursor/projects/workspace/uploads")

ACTS = [
    {
        "kind": "law",
        "pdf": "141905_f7ca.pdf",
        "ocr": "141905_f7ca.ocr.txt",
        "legis_id": "141905",
        "nr": "234",
        "an": 2022,
        "slug": "Energocom securitate furnizare gaze",
        "title": "Legea 234-2022 — Energocom securitate furnizare gaze",
        "mo": "MO 246-250/05.08.2022 art. 494",
        "domeniu": ["energetică", "gaze", "fiscal", "vamal"],
        "enabling_act": "Derogations from L419/2006, Cod fiscal, Cod vamal, tariff/env laws",
        "amended_by": "[[Legea 20-2024 — modificare Legea 234-2022 Energocom (notă)|20/2024]]",
        "complete": True,
    },
    {
        "kind": "law",
        "pdf": "141890_7091.pdf",
        "ocr": "141890_7091.ocr.txt",
        "legis_id": "141890",
        "nr": "20",
        "an": 2024,
        "slug": "modificare Legea 234-2022 Energocom",
        "title": "Legea 20-2024 — modificare Legea 234-2022 Energocom",
        "mo": "MO 73-75/16.02.2024 art. 104",
        "domeniu": ["energetică", "gaze", "fiscal", "vamal"],
        "enabling_act": "[[Legea 234-2022 — Energocom securitate furnizare gaze (text)|234/2022]]",
        "complete": True,
    },
    {
        "kind": "hg",
        "pdf": "142366_5eca.pdf",
        "ocr": "142366_5eca.ocr.txt",
        "legis_id": "142366",
        "nr": "10",
        "an": 2024,
        "slug": "guvernanta energetica si actiuni climatice",
        "title": "HG 10-2024 — guvernanta energetica si actiuni climatice",
        "mo": "MO 104-107/21.03.2024 art. 252",
        "domeniu": ["energetică", "climat", "guvernanță"],
        "enabling_act": "[[Legea 139-2018 — eficienta energetica (text)|L139/2018]] art. 6(1) · [[Legea 174-2017 — energetica (text)|L174/2017]] art. 7'",
        "complete": True,
    },
    {
        "kind": "hanre",
        "pdf": "135452_c62c.pdf",
        "ocr": "135452_c62c.ocr.txt",
        "legis_id": "135452",
        "nr": "297",
        "an": 2022,
        "slug": "masurare gaze naturale comerciale",
        "title": "HANRE 297-2022 — masurare gaze naturale comerciale",
        "mo": "MO 187-193/24.06.2022 art. 721",
        "domeniu": ["energetică", "gaze", "metrologie"],
        "enabling_act": "[[Legea 108-2016 — gazele naturale (text)|L108/2016]] art. 8(1)(g), art. 69(2)",
        "amended_by": "[[HANRE 8-2023 — modificare racordare gaze si masurare gaze (notă)|8/2023]]",
        "complete": True,
    },
    {
        "kind": "hanre",
        "pdf": "141300_eb1d.pdf",
        "ocr": "141300_eb1d.ocr.txt",
        "legis_id": "141300",
        "nr": "537",
        "an": 2020,
        "slug": "calitate servicii transport distributie EE",
        "title": "HANRE 537-2020 — calitate servicii transport distributie EE",
        "mo": "MO 13-20/22.01.2021 art. 47",
        "domeniu": ["energetică", "electricitate", "calitate"],
        "enabling_act": "[[Legea 107-2016 — energia electrica (text)|L107/2016]] art. 7(1)(i), art. 54",
        "amended_by": "[[HANRE 833-2023 — modificarea unor hotarari ANRE regenerabile (notă)|833/2023]]",
        "complete": False,
        "continut": "doar-dispozitiv",
    },
]


def load_ocr(path: Path) -> str:
    text = path.read_text(encoding="utf-8")
    return clean_ocr(text)


def clean_ocr(raw: str) -> str:
    text = raw.replace("--- page break ---", "\n\n")
    text = re.sub(r"^\s*x\s*$", "", text, flags=re.M)
    text = text.replace("\x0c", "\n")
    text = re.sub(r"HANRE\s*(\d+)\s*/\s*(\d{4})", r"HANRE\1/\2", text)
    text = re.sub(r"HG\s*(\d+)\s*/\s*(\d{4})", r"HG\1/\2", text)
    text = re.sub(r"\n{4,}", "\n\n\n", text)
    return text.strip() + "\n"


def normalize_hanre_hg(body: str) -> tuple[str, int]:
    lines = body.splitlines()
    out: list[str] = []
    point_nums: set[str] = set()
    for line in lines:
        s = line.strip()
        m = re.match(r"^CAPITOLUL\s+([IVXLCDM]+|\d+)\s*$", s, re.I)
        if m:
            out.append(f"## Capitolul {m.group(1)}")
            continue
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


def dest_dir(act: dict) -> Path:
    kind = act["kind"]
    if kind == "law":
        return LAWS
    if kind == "hg":
        return HG
    return AUTH


def write_text(act: dict, body: str, count: int) -> Path:
    title = f"{act['title']} (text)"
    note = f"{act['title']} (notă)"
    text_path = dest_dir(act) / f"{title}.md"
    domain_yaml = "\n".join(f"- {d}" for d in act["domeniu"])
    complete = act["complete"]
    continut = act.get("continut", "text-integral" if complete else "partial")

    if act["kind"] == "law":
        fm_type = "act-text"
        instrument = "act_type: lege-organică"
        count_field = f"articole_numarate: {count}"
        puncte = "puncte_numarate: 0"
        tags_extra = ""
        issuer = "issuer: Parlament"
        forta = "forta_juridica: 3"
    elif act["kind"] == "hg":
        fm_type = "act-text"
        instrument = "act_type: hotărâre-guvern"
        count_field = f"puncte_numarate: {count}"
        puncte = "articole_numarate: 0"
        tags_extra = ""
        issuer = "issuer: Guvern"
        forta = ""
    else:
        fm_type = "act-text"
        instrument = "instrument: act-anre\nact_type: hotărâre-anre"
        count_field = f"puncte_numarate: {count}"
        puncte = "articole_numarate: 0"
        tags_extra = "forta_juridica: 8"
        issuer = "issuer: ANRE"
        forta = ""

    fm = [
        "---",
        f'title: "{title}"',
        f"type: {fm_type}",
        instrument,
        f'nr: "{act["nr"]}"',
        f"an: {act['an']}",
        "domeniu:",
        domain_yaml,
        f"domain: [{', '.join(act['domeniu'])}]",
        forta,
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
        "source_ingest: pdf-ocr-upload",
        issuer,
        "legal_status: in_vigoare",
    ]
    fm = [x for x in fm if x]
    if act.get("enabling_act"):
        fm.append(f'enabling_act: "{act["enabling_act"]}"')
    if act.get("amended_by"):
        fm.append(f'amended_by: "{act["amended_by"]}"')
    if not complete and act["kind"] == "hanre":
        fm.append("status_ingestie: DECIZIE ONLY — regulament/anexa absent din OCR")
    fm.append("---")

    warn = ""
    if not complete:
        if act["kind"] == "hanre":
            warn = (
                "\n> [!danger] Anexa / regulamentul lipsește\n"
                "> OCR conține **doar dispozitivul** hotărârii. Regulamentul cu privire la calitatea "
                "serviciilor de transport și distribuție EE (anexă) nu este în acest fișier — "
                "consultați [legis.md](https://www.legis.md/cautare/getResults?lang=ro&doc_id="
                f"{act['legis_id']}) sau [ANRE — Hotărâri](https://anre.md/acte-normative-3-18).\n"
            )
        else:
            warn = (
                "\n> [!warning] OCR / annex check\n"
                "> Text from scanned legis.md PDF via OCR. Verify at source before citing.\n"
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
> Analiză: [[{note}]].
{warn}
---
"""
    text_path.write_text("\n".join(fm) + "\n" + header + "\n" + body + "\n", encoding="utf-8")
    return text_path


def archive_sources(act: dict) -> None:
    SOURCE.mkdir(parents=True, exist_ok=True)
    UPLOADS.mkdir(exist_ok=True)
    pdf_src = CURSOR_UPLOADS / act["pdf"]
    ocr_src = CURSOR_UPLOADS / act["ocr"]
    if pdf_src.exists():
        shutil.copy2(pdf_src, SOURCE / f"{act['legis_id']}-{act['pdf']}")
        shutil.copy2(pdf_src, UPLOADS / act["pdf"])
    if ocr_src.exists():
        shutil.copy2(ocr_src, SOURCE / f"{act['legis_id']}.ocr.txt")


def main() -> None:
    for act in ACTS:
        ocr_path = CURSOR_UPLOADS / act["ocr"]
        if not ocr_path.exists():
            raise SystemExit(f"Missing OCR: {ocr_path}")
        body = load_ocr(ocr_path)
        if act["kind"] == "law":
            body, count = normalize_law(body)
        else:
            body, count = normalize_hanre_hg(body)
        path = write_text(act, body, count)
        archive_sources(act)
        print({"ingested": path.name, "kind": act["kind"], "count": count, "complete": act["complete"]})


if __name__ == "__main__":
    main()
