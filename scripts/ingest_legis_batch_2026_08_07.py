#!/usr/bin/env python3
"""Ingest legis.md dumps from uploads/ into article-anchored (text) + archive."""

from __future__ import annotations

import re
import shutil
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
UPLOADS = ROOT / "uploads"
SOURCE = ROOT / "99 Attachments/source-legis"
LAWS = ROOT / "10 Legislation/Laws"
CODES = ROOT / "10 Legislation/Codes"
TODAY = date.today().isoformat()

ARTICLE_RE = re.compile(
    r"^(#{1,3}\s*)?\*{0,2}Articolul\s+(\d+[¹]?)\.?\*{0,2}\s*(.*)$",
    re.IGNORECASE,
)
ART_DOT_RE = re.compile(
    r"^(#{1,3}\s*)?\*{0,2}Art\.?\s*(\d+[¹]?)\.?\s*[–-]?\*{0,2}\s*(.*)$",
    re.IGNORECASE,
)
ART_ROMAN_RE = re.compile(
    r"^(#{1,3}\s*)?\*{0,2}Art\.\s*([IVX]+)\.?\*{0,2}\s*[–-]?\s*(.*)$",
    re.IGNORECASE,
)


def clean_body(raw: str) -> str:
    text = raw.replace("```", "")
    text = re.sub(r"</?u>", "", text)
    text = text.lstrip("\n")
    return text


def normalize_articles(body: str, style: str = "articolul") -> tuple[str, int]:
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
                out.append(f"### Art. {num}. {rest}".rstrip())
                continue
        if style == "art_dot":
            m = ART_DOT_RE.match(stripped)
            if m:
                num, rest = m.group(2), (m.group(3) or "").strip()
                # skip roman Art. I in art_dot mode if somehow matched poorly
                if re.fullmatch(r"[IVX]+", num):
                    out.append(line)
                    continue
                nums.append(num)
                title = f"### Articolul {num}."
                if rest and not rest.startswith("-"):
                    # keep leading dash content as part of heading if short
                    if len(rest) < 80 and not rest.startswith("("):
                        title = f"### Articolul {num}. {rest}"
                        out.append(title)
                        continue
                    out.append(title)
                    out.append(rest)
                    continue
                out.append(title if not rest else f"{title} {rest}".rstrip())
                continue
        m = ARTICLE_RE.match(stripped)
        if m:
            num, rest = m.group(2), (m.group(3) or "").strip()
            nums.append(num)
            out.append(f"### Articolul {num}. {rest}".rstrip() if rest else f"### Articolul {num}.")
            continue
        out.append(line)
    return "\n".join(out), len(set(nums))


def text_complete(body: str) -> bool:
    s = body.rstrip()
    if not s:
        return False
    if "PREȘEDINTELE PARLAMENTULUI" in s or "PREŞEDINTELE PARLAMENTULUI" in s:
        return True
    if s.endswith((".", ";", ":", ")", "”", '"', "»")):
        return True
    return False


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
) -> dict:
    upload = UPLOADS / upload_name
    raw = upload.read_text(encoding="utf-8")
    body = clean_body(raw)
    body, article_count = normalize_articles(body, style=style)
    complete = text_complete(body)

    SOURCE.mkdir(parents=True, exist_ok=True)
    archive_path = SOURCE / archive_name
    shutil.copy2(upload, archive_path)

    domain_yaml = "\n".join(f"- {d}" for d in domeniu)
    fm_lines = [
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
        "issuer: Parlament",
        "legal_status: in_vigoare",
    ]
    if extra_fm:
        for k, v in extra_fm.items():
            fm_lines.append(f"{k}: {v}")
    fm_lines.append("---")

    warn = ""
    if not complete:
        warn = (
            "\n> [!danger] Verificare necesară\n"
            "> Textul poate fi trunchiat. Verificați ultimul articol / anexe la sursă.\n"
        )
    article_note = (
        "Articole normalizate ca `### Articolul N.` / `### Art. N.` pentru ancorare wikilink."
        if article_count
        else "Document pe articole romane (lege de modificare)."
    )
    header = f"""# {title.replace(' (text)', '')}

> [!info] Sursă & versiune
> Text preluat din **legis.md** HTML (doc_id [{legis_id}](https://www.legis.md/cautare/getResults?lang=ro&doc_id={legis_id})).
> {article_note}
> Analiză: [[{note_link}]].
{warn}
---
"""
    text_path.parent.mkdir(parents=True, exist_ok=True)
    text_path.write_text("\n".join(fm_lines) + "\n" + header + "\n" + body + "\n", encoding="utf-8")
    return {
        "title": title,
        "articles": article_count,
        "complete": complete,
        "path": str(text_path.relative_to(ROOT)),
        "archive": archive_name,
    }


def archive_only(upload_name: str, archive_name: str) -> dict:
    SOURCE.mkdir(parents=True, exist_ok=True)
    src = UPLOADS / upload_name
    dst = SOURCE / archive_name
    shutil.copy2(src, dst)
    return {"archive": archive_name, "status": "archived-only", "bytes": src.stat().st_size}


def main() -> None:
    results = []

    # --- NEW: L1593/2002 AOAM premiums ---
    results.append(
        write_act(
            upload_name="152955_fd93.md",
            archive_name="152955.md",
            text_path=LAWS / "Legea 1593-2002 — prime asigurare medicala obligatorie (text).md",
            title="Legea 1593-2002 — prime asigurare medicala obligatorie (text)",
            act_type="lege-ordinară",
            nr="1593",
            an=2002,
            domeniu=["fiscal", "social", "sanatate"],
            mo="MO 18-19/08.02.2003 art. 57",
            legis_id="152955",
            note_link="Legea 1593-2002 — prime asigurare medicala obligatorie (notă)",
            style="art_dot",
            forta=4,
        )
    )

    # --- NEW: L271/2017 statutory audit ---
    results.append(
        write_act(
            upload_name="153011_8630.md",
            archive_name="153011.md",
            text_path=LAWS / "Legea 271-2017 — auditul situatiilor financiare (text).md",
            title="Legea 271-2017 — auditul situatiilor financiare (text)",
            act_type="lege-organică",
            nr="271",
            an=2017,
            domeniu=["contabilitate", "audit", "fiscal"],
            mo="MO 7-17/12.01.2018 art. 48",
            legis_id="153011",
            note_link="Legea 271-2017 — auditul situatiilor financiare (notă)",
            style="articolul",
            forta=3,
            extra_fm={
                "eu_directives": '"Directive 2006/43/EC; Regulation (EU) 537/2014"',
                "last_amended": "'2025-12-31'",
            },
        )
    )

    # --- NEW: L41/2026 business-support omnibus ---
    results.append(
        write_act(
            upload_name="153667_7928.md",
            archive_name="153667.md",
            text_path=LAWS / "Legea 41-2026 — suport desfasurare afaceri (text).md",
            title="Legea 41-2026 — suport desfasurare afaceri (text)",
            act_type="lege-organică",
            nr="41",
            an=2026,
            domeniu=["fiscal", "comercial", "achizitii", "societati"],
            mo="MO 143-144/27.03.2026 art. 114",
            legis_id="153667",
            note_link="Legea 41-2026 — suport desfasurare afaceri (notă)",
            style="roman",
            forta=3,
        )
    )

    # --- EXISTING: archive CF refresh (same doc_id already split in vault) ---
    results.append(archive_only("152862_4a0c.md", "152862.md"))

    # --- EXISTING: L489 older consolidation — archive under distinct name ---
    results.append(archive_only("152737_a5fd.md", "152737.md"))

    for r in results:
        print(r)


if __name__ == "__main__":
    main()
