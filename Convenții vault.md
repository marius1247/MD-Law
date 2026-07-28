---
title: "Convenții vault"
type: reference
tags: [reference, meta]
created: 2026-07-22
---

# Convenții vault

## Folders
- `00 Inbox` — capture / unfiled
- `01 Sistemul juridic` — meta-layer: how MD law works
- `10 Acte normative` — **working** legal texts (cleaned, article-anchored), by act type: `Constituție`, `Coduri`, `Legi organice & ordinare`, `Hotărâri de Guvern`, `Acte ANRE & autorități`
- `20 Domenii` — thematic analysis by area
- `30 Concepte` — atomic institution/concept notes
- `50 MOCs` — maps of content (navigation hubs)
- `60 Autorități & Instituții` — state-governance profiles
- `90 Templates`
- `99 Attachments/` — binaries and raw dumps
  - `99 Attachments/source-legis/` — **all original legis.md downloads** (named by `doc_id`). Index: [[SOURCE INDEX]]. Do not edit these; re-ingest into `10` when updating.

> [!important] One vault, two layers for texts
> 1. **Raw originals** → only in `99 Attachments/source-legis/` (single place).
> 2. **Working corpus** → only in `10 Acte normative/` (split by act type; large codes further split by Carte/Titlu).
>
> Open **`Moldovan Law/`** as the Obsidian vault root (not the GitHub repo root, which also contains `EU Law/` and `scripts/`).

## File naming
- Acts: `<Denumire> — text` and `<Denumire> — notă`
- Concepts: `Concept — <Denumire>`
- Maps: `MOC — <Domeniu>`

## Two-layer rule
Raw law (RO) lives in `10` as `— text`. Your English analysis, structure notes, and conclusions live in the `— notă` companion and in `20/30`. **Never edit the substance of a `— text` note** except to update to a newer consolidation — it must mirror the official source.

## Frontmatter (acts)
`type, act_type, nr, an, data_adoptarii, domeniu[], forta_juridica (1–8), in_vigoare, mo_publicare, legis_id, legis_url, versiune_text`. This makes the corpus queryable (Dataview-ready).

## Linking
Article-anchored: `[[<act> (text)#Articolul N]]`. Every act text uses `### Articolul N.` headings so links resolve to the exact article.

## Folders (added 2026-07-23)
- `20 Domenii` — one synthesis note per domain. English. This is where the *reasoning* lives.
- `30 Concepte` — atomic concept notes, one institution or term each, linked from everywhere.

## Law House analysis standard (added 2026-07-28)
Every `— notă` companion should follow the blueprint in [[Template — Act (notă)]] and [[Audit vault — Law House Knowledge Engine — 2026-07-28]]: executive summary, statutory hierarchy, risk matrix, jurisprudence, client checklist. Cross-act themes use `20 Domenii/` dossiers with `analysis_tier: law-house`.

## Ingestion workflow (how texts get here)
1. Find the act's `doc_id` on legis.md.
2. Pull full text: `https://www.legis.md/cautare/downloadpdf/<doc_id>` (returns clean plain text).
3. Convert to article-anchored markdown, prepend frontmatter + a source/version callout.
4. **Always verify the consolidation is current** — legis.md snapshots are per-version; a `doc_id` may be stale. Note any amendments not yet merged.

> [!warning] Automated fetch stops at ~96 KB
> Confirmed 2026-07-23. Step 2 silently truncates any act larger than ~96,000 characters, mid-sentence, with no error. It is a ceiling in the retrieval tooling — re-fetching gives the identical cut. legis.md has **no per-chapter endpoint**, so the act cannot be pulled in pieces, and the `getResults` viewer is client-rendered (a plain fetch returns only `Conținutul se încarcă...`).
>
> **Rule:** after any ingestion, check that the file ends on a complete sentence and that the last `### Articolul N` matches the act's real final article. If not, set `text_complet: false`, add a `[!danger]` callout naming the last complete article, and log it in [[Status ingestie — Energetica]].
>
> **The only reliable fix is a manual browser download.** Plan large codes (Codul fiscal, Codul civil) that way from the start — one file per Titlu/Carte, named `<Act> — text — Titlul N`.

## Where analysis goes when the text is incomplete
The two-layer rule still holds, but a truncated `— text` file must not silently limit the analysis. Write the `— notă` and the `20 Domenii` synthesis from the act **as actually published**; use in-vault article links only for articles that are present, and mark anything else *(beyond truncation — verify at source)*. Better a complete analysis with honest flags than an analysis quietly shaped by a download artefact.
