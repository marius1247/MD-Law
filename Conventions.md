---
title: "Conventions"
type: reference
tags: [reference, meta]
created: 2026-07-22
updated: 2026-08-06
---

# Conventions

This vault is a **legal corpus + analysis layer**, not a note dump. The model is identical across the EU / Romanian / Moldovan vaults.

## Core idea — two layers, always

1. **`(text)`** — authoritative raw law (immutable substance; article-anchored)
2. **`(notă)`** — expert English analysis you can work from without reopening the official source

Industry / topic lives in **`20 Domains` + `50 MOCs` + frontmatter `domain[]`** — not as the main filing system under `10 Legislation`.

Open **`MD-Law/`** (this repo) as its own Obsidian vault root.

## Folder skeleton

| Folder | Role |
|---|---|
| `00 Inbox` | Capture, download lists, roadmaps, unfiled |
| `01 Legal system` | Meta: hierarchy, packages, procedures, bridges |
| `10 Legislation/` | Working corpus by instrument type |
| `20 Domains` | One synthesis per industry / practice area |
| `20 Position Papers` | Soft law / regulator guidance |
| `30 Concepts` | Atomic doctrine notes (`Concept — …`) |
| `50 MOCs` | Maps of content by domain |
| `60 Authorities` | Institutional profiles |
| `90 Templates` | Note templates |
| `99 Attachments/source-legis/` | Immutable raw dumps (HTML/PDF/plain) |
| `uploads/` | Repo-level drop zone (cleared after each batch) |

### Under `10 Legislation` (MD instrument types)

`Constitution` · `Codes` · `Laws` · `Government Decisions` · `Authority Acts`

(EU vaults use Treaties / Regulations / Directives / Decisions / Delegated Regulations / Network Codes — same *role*, different instrument labels.)

## Naming conventions

| Kind | Pattern | Example |
|---|---|---|
| Legislation | `<Type Nr-Year> — <short name> (text)` / `(notă)` | `Legea 164-2025 — energia electrica (text)` |
| Concepts | `Concept — <name>` | `Concept — Unbundling` |
| Domains | `<Industry> — synthesis` | `Energetică — synthesis` |
| Maps | `MOC — <domain>` | `MOC — Energetică` |
| Authorities | plain institution name | `ANRE` |
| Position papers | `<Issuer> — <short title> (notă)` | `ANRE — connection guidance (notă)` |

Use `-` in filenames for numbers (`164-2025`); keep legal form in prose (`Legea nr. 164/2025`).

## Note types & linking rules

- **`(text)`** — full consolidated text; headings as `### Articolul N` so links resolve: `[[Act (text)#Articolul N]]`
- **`(notă)`** — expert analysis (thesis → architecture → operative regime by problem → definitions → obligations → enforcement → hard edges → interactions → file checklist). Follow [[Template — Act (notă)]].
- **Concepts** — one doctrine/term; always cite the defining article
- **MOCs** — hub linking acts, notes, concepts, authorities for one domain
- **Domains** — synthesis / architecture across a practice area
- **Authorities** — mandate, enabling acts, what they issue

**Never edit substance of `(text)`** except to update to a newer consolidation.

## Frontmatter (minimum for acts)

Cross-vault minimum (English keys preferred going forward):

`type`, `instrument`, national ID (`legis_id`), `domain[]`, `in_force`, source URL, `version_date`

MD corpus also carries juris-specific fields already in use (Dataview-ready):

`act_type`, `nr`, `an`, `data_adoptarii`, `domeniu[]`, `forta_juridica` (1–8), `in_vigoare`, `mo_publicare`, `legis_url`, `versiune_text`

Map: `instrument` ↔ `act_type` · `domain[]` ↔ `domeniu[]` · `in_force` ↔ `in_vigoare` · `version_date` ↔ `versiune_text`.

For notes: `status` (`stub` / `reviewed`), `depth` / `analysis_tier` (`law-house`), link back to the `(text)`.

## Ingestion workflow

1. Get the official consolidated source (legis.md `doc_id`)
2. Drop immutable dump in `99 Attachments/source-legis/`
3. Convert to article-anchored markdown in `10 Legislation` as `(text)`
4. Write companion `(notă)` from [[Template — Act (notă)]]
5. Wire into the right `MOC — …` and update domain / concept links
6. Keep [[SOURCE INDEX]] mapping dump → working note
7. Clear `uploads/` after each batch

> [!warning] Automated fetch stops at ~96 KB
> Confirmed 2026-07-23. After any ingestion, check that the file ends on a complete sentence and that the last `### Articolul N` matches the act's real final article. If not, set `text_complet: false`, add a `[!danger]` callout, and log it in [[Status ingestie — Energetica]]. Large codes: one file per Titlu/Carte (`<Act> — text — Titlul N`).

## Bootstrap checklist (new legal vault)

1. Create the numbered folders above
2. Copy `90 Templates` (Act text, Act notă, Concept, MOC, Authority)
3. Add `Home.md` + `Conventions.md`
4. Seed `01 Legal system` (hierarchy / how sources work in that jurisdiction)
5. Ingest acts as `(text)` + `(notă)` pairs
6. Build MOCs per practice area; grow `30 Concepts` as doctrines appear
7. Keep industry in `20`/`50`, not as the primary `10` taxonomy

## Where analysis goes when the text is incomplete

Write the `(notă)` and the `20 Domains` synthesis from the act **as actually published**; use in-vault article links only for articles that are present, and mark anything else *(beyond truncation — verify at source)*.
