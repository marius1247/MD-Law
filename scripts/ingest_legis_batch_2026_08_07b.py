#!/usr/bin/env python3
"""Ingest second 2026-08-07 HTML/PDF batch into article-anchored (text) files."""

from __future__ import annotations

import re
import shutil
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
UPLOADS = ROOT / "uploads"
SOURCE = ROOT / "99 Attachments/source-legis"
LAWS = ROOT / "10 Legislation/Laws"
AUTH = ROOT / "10 Legislation/Authority Acts"
TODAY = date.today().isoformat()

ARTICLE_RE = re.compile(
    r"^(#{1,3}\s*)?\*{0,2}Articolul\s+(\d+[¹]?)\.?\*{0,2}\s*(.*)$",
    re.IGNORECASE,
)
ART_ROMAN_RE = re.compile(
    r"^(#{1,3}\s*)?\*{0,2}Art\.\s*([IVX]+)\.?\*{0,2}\s*[–.-]?\s*(.*)$",
    re.IGNORECASE,
)


def clean_body(raw: str) -> str:
    text = raw.replace("```", "")
    text = re.sub(r"</?u>", "", text)
    # PDF form-feed / soft hyphens noise
    text = text.replace("\x0c", "\n")
    text = text.lstrip("\n")
    return text


def normalize_articles(body: str, style: str) -> tuple[str, int]:
    lines = body.splitlines()
    out: list[str] = []
    nums: list[str] = []
    for line in lines:
        stripped = line.strip()
        if style == "roman":
            m = ART_ROMAN_RE.match(stripped)
            if m:
                num, rest = m.group(2), (m.group(3) or "").strip()
                nums.append(num)
                # Keep heading short
                if len(rest) > 100:
                    out.append(f"### Art. {num}.")
                    out.append(rest)
                else:
                    out.append(f"### Art. {num}. {rest}".rstrip())
                continue
        if style == "articolul":
            m = ARTICLE_RE.match(stripped)
            if m:
                num, rest = m.group(2), (m.group(3) or "").strip()
                nums.append(num)
                if len(rest) > 80:
                    out.append(f"### Articolul {num}.")
                    out.append(rest)
                else:
                    out.append(f"### Articolul {num}. {rest}".rstrip() if rest else f"### Articolul {num}.")
                continue
        # light chapter normalize
        if stripped.startswith("## **Capitolul") or stripped.startswith("Capitolul "):
            chap = re.sub(r"\*+", "", stripped)
            if not chap.startswith("#"):
                out.append(f"## {chap}")
                continue
        out.append(line)
    return "\n".join(out), len(set(nums))


def text_complete(body: str) -> bool:
    s = body.rstrip()
    markers = (
        "PREȘEDINTELE PARLAMENTULUI",
        "PREŞEDINTELE PARLAMENTULUI",
        "DIRECTOR GENERAL",
    )
    return any(m in s for m in markers) or s.endswith((".", ";", ":", ")", "”", '"', "»"))


def write_act(
    *,
    upload_name: str,
    archive_name: str,
    text_path: Path,
    title: str,
    act_type: str,
    nr: str,
    an: int,
    domeniu: list[str],
    mo: str,
    legis_id: str,
    note_link: str,
    style: str,
    forta: int = 3,
    extra_fm: dict | None = None,
    complete_override: bool | None = None,
) -> dict:
    upload = UPLOADS / upload_name
    raw = upload.read_text(encoding="utf-8")
    body = clean_body(raw)
    body, article_count = normalize_articles(body, style=style)
    complete = text_complete(body) if complete_override is None else complete_override

    SOURCE.mkdir(parents=True, exist_ok=True)
    shutil.copy2(upload, SOURCE / archive_name)
    # also keep PDF if present for same id
    pdf = UPLOADS / f"{legis_id}_4dec.pdf"
    if not pdf.exists():
        # try generic
        for p in UPLOADS.glob(f"{legis_id}*.pdf"):
            pdf = p
            break
    if pdf.exists():
        shutil.copy2(pdf, SOURCE / f"{legis_id}.pdf")

    domain_yaml = "\n".join(f"- {d}" for d in domeniu)
    fm = [
        "---",
        f'title: "{title}"',
        "type: act-text",
        f"instrument: {act_type}",
        f"act_type: {act_type}",
        f'nr: "{nr}"',
        f"an: {an}",
        "domeniu:",
        domain_yaml,
        f"domain: [{', '.join(domeniu)}]",
        f"forta_juridica: {forta}",
        "in_force: true",
        "in_vigoare: true",
        f'mo_publicare: "{mo}"',
        f'legis_id: "{legis_id}"',
        f'legis_url: "https://www.legis.md/cautare/getResults?lang=ro&doc_id={legis_id}"',
        f"version_date: {TODAY}",
        f"versiune_text: {TODAY}",
        f"continut: {'text-integral' if complete else 'partial'}",
        f"text_complet: {'true' if complete else 'false'}",
        f"articole_numarate: {article_count}",
        "tags: [act, text, acte_normative]",
        f"created: {TODAY}",
        f"updated: {TODAY}",
        "source_ingest: legis-html-upload",
        "issuer: Parlament" if not act_type.startswith("hotărâre-anre") else "issuer: ANRE",
        "legal_status: in_vigoare",
    ]
    if extra_fm:
        for k, v in extra_fm.items():
            fm.append(f"{k}: {v}")
    fm.append("---")

    warn = ""
    if not complete:
        warn = (
            "\n> [!danger] Verificare necesară\n"
            "> Textul poate fi trunchiat (anexe / formulă). Verificați la sursă.\n"
        )
    display = title.replace(" (text)", "")
    header = f"""# {display}

> [!info] Sursă & versiune
> Text preluat din **legis.md** (doc_id [{legis_id}](https://www.legis.md/cautare/getResults?lang=ro&doc_id={legis_id})).
> Analiză: [[{note_link}]].
{warn}
---
"""
    text_path.parent.mkdir(parents=True, exist_ok=True)
    text_path.write_text("\n".join(fm) + "\n" + header + "\n" + body + "\n", encoding="utf-8")
    return {"title": title, "articles": article_count, "complete": complete, "path": str(text_path.relative_to(ROOT))}


def archive_only(upload_name: str, archive_name: str) -> dict:
    SOURCE.mkdir(parents=True, exist_ok=True)
    src = UPLOADS / upload_name
    shutil.copy2(src, SOURCE / archive_name)
    return {"archive": archive_name, "status": "archived-only", "bytes": src.stat().st_size}


def main() -> None:
    results = []

    # L318/2025 — annual fiscal package (P0)
    results.append(
        write_act(
            upload_name="153700_0b40.md",
            archive_name="153700.md",
            text_path=LAWS / "Legea 318-2025 — modificare acte fiscale (text).md",
            title="Legea 318-2025 — modificare acte fiscale (text)",
            act_type="lege-organică",
            nr="318",
            an=2025,
            domeniu=["fiscal", "vamal", "social"],
            mo="MO 659-661/31.12.2025 art. 792",
            legis_id="153700",
            note_link="Legea 318-2025 — modificare acte fiscale (notă)",
            style="roman",
            extra_fm={"last_amended": "'2026-03-27'"},
        )
    )

    # HANRE 853/2025 — balancing FSE + PRE T&Cs
    results.append(
        write_act(
            upload_name="154693_d58d.md",
            archive_name="154693.md",
            text_path=AUTH / "HANRE 853-2025 — clauze echilibrare FSE si PRE (text).md",
            title="HANRE 853-2025 — clauze echilibrare FSE si PRE (text)",
            act_type="hotărâre-anre",
            nr="853",
            an=2025,
            domeniu=["energetică", "echilibrare"],
            mo="MO 139-141/26.03.2026 art. 223",
            legis_id="154693",
            note_link="HANRE 853-2025 — clauze echilibrare FSE si PRE (notă)",
            style="none",
            forta=6,
            extra_fm={
                "enabling_act": '"[[Legea 164-2025 — energia electrica (text)]] art. 39(9),(13)"',
                "data_intrarii_in_vigoare": "2026-07-01",
            },
        )
    )

    # L461/2001 — petroleum (annex formula may be noisy)
    results.append(
        write_act(
            upload_name="155106_1a40.md",
            archive_name="155106.md",
            text_path=LAWS / "Legea 461-2001 — piata produselor petroliere (text).md",
            title="Legea 461-2001 — piata produselor petroliere (text)",
            act_type="lege-organică",
            nr="461",
            an=2001,
            domeniu=["energetică", "petrol"],
            mo="MO 40-49/10.02.2017 art. 82 (republicare)",
            legis_id="155106",
            note_link="Legea 461-2001 — piata produselor petroliere (notă)",
            style="articolul",
            complete_override=True,  # has Presedinte; annex formula OCR-noisy but body present
            extra_fm={"last_amended": "'2026-06-26'"},
        )
    )

    # L76/2026 — public institutions companion amendments
    results.append(
        write_act(
            upload_name="155410_6715.md",
            archive_name="155410.md",
            text_path=LAWS / "Legea 76-2026 — ajustare legislatie institutii publice (text).md",
            title="Legea 76-2026 — ajustare legislatie institutii publice (text)",
            act_type="lege-organică",
            nr="76",
            an=2026,
            domeniu=["administrativ", "civil", "energetică"],
            mo="MO 330-333/23.07.2026 art. 333",
            legis_id="155410",
            note_link="Legea 76-2026 — ajustare legislatie institutii publice (notă)",
            style="roman",
            extra_fm={"data_intrarii_in_vigoare": "2027-01-01"},
        )
    )

    # L248/2025 — crisis management parent (from PDF extract)
    results.append(
        write_act(
            upload_name="155526.md",
            archive_name="155526.md",
            text_path=LAWS / "Legea 248-2025 — managementul situatiilor de criza (text).md",
            title="Legea 248-2025 — managementul situatiilor de criza (text)",
            act_type="lege-organică",
            nr="248",
            an=2025,
            domeniu=["situatii-de-criza", "administrativ", "energetică"],
            mo="MO 437-440/19.08.2025 art. 600",
            legis_id="155526",
            note_link="Legea 248-2025 — managementul situatiilor de criza (notă)",
            style="articolul",
            extra_fm={
                "last_amended": "'2026-07-28'",
                "source_ingest": "pdf-upload",
                "eu_directives": '"Decision 1313/2013/EU (partial)"',
            },
        )
    )
    # copy PDF archive
    pdf = UPLOADS / "155526_4dec.pdf"
    if pdf.exists():
        shutil.copy2(pdf, SOURCE / "155526.pdf")

    # L101 — already ingested same doc_id
    results.append(archive_only("155085_cb19.md", "155085.md"))

    for r in results:
        print(r)


if __name__ == "__main__":
    main()
