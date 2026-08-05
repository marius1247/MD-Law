#!/usr/bin/env python3
"""Add legis metadata placeholders to upload-ingested (text) files missing legis_id."""

from __future__ import annotations

import re
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ACTS = ROOT / "10 Acte normative"

# Resolved doc_ids (manual / PDF filename pattern / SOURCE INDEX)
KNOWN: dict[str, str] = {
    "Legea 325-2025 — achizitii publice (text).md": "152974",
    "HANRE 423-2019 — Codul retelelor electrice (text).md": "151929",
}


def main() -> None:
    updated = 0
    pending = 0
    for path in ACTS.rglob("*(text).md"):
        text = path.read_text(encoding="utf-8")
        if "source_ingest: uploads-folder" not in text:
            continue
        if re.search(r"^legis_id:", text, re.M):
            continue
        fm_match = re.match(r"---\n(.*?)\n---", text, re.S)
        if not fm_match:
            continue
        fm = fm_match.group(1)
        nr_m = re.search(r"nr:\s*['\"]?([^'\n]+)", fm)
        an_m = re.search(r"an:\s*(\d{4})", fm)
        nr = nr_m.group(1).strip("'\"") if nr_m else "?"
        an = an_m.group(1) if an_m else "?"
        name = path.name
        if name in KNOWN:
            doc_id = KNOWN[name]
            insert = f"legis_id: '{doc_id}'\nlegis_url: https://www.legis.md/cautare/getResults?lang=ro&doc_id={doc_id}\n"
            updated += 1
        else:
            insert = (
                f"legis_id_pending: true\n"
                f"legis_search_hint: '{nr}/{an}'\n"
            )
            pending += 1
        # insert after in_vigoare or at start of frontmatter body
        if "in_vigoare:" in fm:
            fm_new = re.sub(r"(in_vigoare:.*\n)", r"\1" + insert, fm, count=1)
        else:
            fm_new = insert + fm
        fm_new = re.sub(
            r"updated:\s*\d{4}-\d{2}-\d{2}",
            f"updated: {date.today().isoformat()}",
            fm_new,
            count=1,
        )
        new_text = text.replace(fm_match.group(0), "---\n" + fm_new + "---", 1)
        path.write_text(new_text, encoding="utf-8")
        print(path.name, "known" if name in KNOWN else "pending")
    print(f"\nDone: {updated} with legis_id, {pending} with pending hints")


if __name__ == "__main__":
    main()
