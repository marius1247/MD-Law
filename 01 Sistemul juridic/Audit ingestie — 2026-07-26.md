---
title: "Audit ingestie — 2026-07-26"
type: reference
domeniu: [meta]
tags: [reference, meta, ingestion, audit]
created: 2026-07-26
updated: 2026-07-26
---

# Audit of the 2026-07-26 source ingestion

## What was done with the uploads

You uploaded raw legis.md dumps into repo-root `source/` (filenames = `doc_id.md`).

The ingestion pipeline:

1. Kept each raw dump (now consolidated under [[SOURCE INDEX|`99 Attachments/source-legis/`]]).
2. Converted a working copy into `10 Acte normative/… (text).md` with frontmatter + `### Articolul N.` anchors.
3. Wrote English `— notă` companions and updated MOCs / Home / Roadmap / Status.

**38 source files** → **36 ingested** + **2 intentional duplicates unused** (`146678` older Customs Code; `154797` older SA law).

## Mistakes found in audit (and fixed)

| Issue | Severity | Fix |
|---|---|---|
| [[HANRE 423-2019 — Codul retelelor electrice (text)\|HANRE 423/2019]] marked `text_complet: true` though only the approving decision exists (~3.5 KB) | **High** — false completeness | Corrected to `continut: doar-dispozitiv`, `text_complet: false`, danger callout |
| [[HANRE 486-2017 — Metodologie tarife transport EE (text)\|HANRE 486/2017]] same false-complete + already abrogated by 626/2023 | High | Corrected flags + `abrogat_prin` |
| Fiscal **Titlul VI¹** (*impozitul pe avere*) merged into Titlul VI because source heading was `Titlul VI` / `## 1` | Medium | Split into [[Codul fiscal 1163-1997 — text — Titlul VI¹]]; index + notă updated |
| Raw dumps lived at repo-root `source/` while working texts lived under `Moldovan Law/10…` | Structure | Moved all originals to `Moldovan Law/99 Attachments/source-legis/` + [[SOURCE INDEX]] |

## Not mistakes — remaining gaps (no adequate source uploaded)

| File | Status |
|---|---|
| [[HANRE 169-2019 — furnizarea energiei electrice (text)\|HANRE 169/2019]] electricity supply | Still truncated. Source `148195` is a **different** act (HANRE 169/**2025** water/sewerage) |
| [[HANRE 64-2018 — Metodologie tarife distributie EE (text)\|HANRE 64/2018]], [[HANRE 375-2017 — Metodologie tarife regenerabile (text)\|375/2017]] | Still decision/annex-incomplete |
| [[HG 820-2024 — situatii exceptionale electroenergetic (text)\|HG 820/2024]] | Annex still missing |
| [[Legea 107-2016 — energia electrica (text)\|L107/2016]] | Still truncated — **abrogated**, not worth completing |
| HANRE 423 annex | Still missing (decision only in source) |

## Known quality limitations (accepted for now)

1. **ASCII-stripped filenames** — many files use `retele` / `pietei` / `societati` without diacritics (pre-existing energy corpus pattern + new files matched it for wikilink stability). Folder names use diacritics. Renaming would break links; defer a dedicated rename pass.
2. **ANRE acts use puncte, not articole** — converter reports `articole_numarate: 0`. Body text is complete where annex was present; heading normalisation is weaker than for laws.
3. **Bis-article headings** in some PDF-derived files still look like `### Articolul 287. ## 1` in places (partially cleaned in Titlul VI¹).
4. **Amendment-only HANRE acts** (261, 310, 328, 383, 177, rectificare, 169/2025 water) have text but no dedicated `— notă` yet — acceptable; they are linked from parent-act notes / Status.

## Canonical structure (after fix)

```
Moldovan Law/                          ← open THIS as the Obsidian vault
├── Home.md · Roadmap.md · Convenții vault.md
├── 01 Sistemul juridic/               ← meta, status, this audit
├── 10 Acte normative/                 ← WORKING texts + notes
│   ├── Constituție/
│   ├── Coduri/                        ← Civil (by Carte), Fiscal (by Titlu), etc.
│   ├── Legi organice & ordinare/
│   ├── Hotărâri de Guvern/
│   └── Acte ANRE & autorități/
├── 20 Domenii/ · 30 Concepte/ · 50 MOCs/ · 60 Autorități/
├── 90 Templates/
└── 99 Attachments/
    └── source-legis/                  ← ALL original legis.md dumps (one place)
        └── SOURCE INDEX.md
```

Repo root also has `EU Law/` (separate vault) and `scripts/` (ingestion tooling) — outside the Moldovan Obsidian vault.

## Coverage snapshot after audit

- Source dumps: **38** in `source-legis/`
- Working `— text` files under `10`: **~65**
- Analysis `— notă` files under `10`: **~33**
- Every mapped source has a working text, except the 2 intentional duplicate losers

## See also
[[SOURCE INDEX]] · [[Status ingestie — Energetica]] · [[Convenții vault]] · [[Roadmap]]
