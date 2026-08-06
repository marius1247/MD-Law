---
title: "Audit vault — Law House Knowledge Engine"
type: reference
domeniu: [meta, energetică]
tags: [reference, meta, audit, law-house]
status: draft
created: 2026-07-28
updated: 2026-07-28
---

# Audit vault — Law House Knowledge Engine

**Purpose:** Strategic audit of vault richness and analysis quality, plus the masterplan and standard analysis blueprint for upgrading the Moldova energy corpus from a raw legal repository to an institutional Law House Knowledge Engine.

**Related:** [[Audit ingestie — 2026-07-26]] · [[Status ingestie — Energetica]] · [[Conventions]] · [[MOC — Energetică]]

---

## 1. Vault richness & quality audit

### 1.1 Key findings

| Dimension | Current state (Jul 2026) | Gap / missing elements |
|---|---|---|
| **Primary laws** | L174, L164, L108, L10, CA116, L117 ingested with companions | Gas sector still on third package (no L164-equivalent). Some acts truncated or decision-only (L107 abrogated; HANRE 423 annex missing) |
| **Analysis quality** | ~35 `— notă` files; several are substantive (L164, L174, HANRE 283, CA116) | Most notes lack **risk matrices**, **client checklists**, and **jurisprudence** layers. Status overwhelmingly `draft` |
| **Jurisprudence** | Referenced in prose in a few notes; no dedicated litigation vault | No CSJ / Chișinău Court of Appeal case matrix; no petition templates |
| **EU acquis alignment** | Tracked in L164, L117, HG 820 notes | No systematic mapping table per act (directive → article → HANRE implementation) |
| **Vault linking** | Good wikilink graph; YAML frontmatter on ~70% of files | Tags not standardised (`#ANRE/Gaze` style absent); bidirectional primary ↔ secondary links incomplete |
| **Uploads queue** | 32 raw dumps in `uploads/` | ~30 net-new acts not ingested; 2 duplicates already in vault |

### 1.2 Corpus composition (approximate)

| Layer | Files | Role |
|---|---:|---|
| `10 Legislation` — `(text)` | 66 | Romanian legal text, article-anchored |
| `10 Legislation` — `(notă)` | 35 | English analysis companions |
| `20 Domains` — synthesis | 5 | Cross-act reasoning |
| `30 Concepts` | 21 | Atomic institution/term notes |
| `50 MOCs` | 8 | Navigation hubs |
| `uploads/` (unprocessed) | 32 | Raw legis.md dumps |
| `99 Attachments/source-legis/` | 38 | Archive originals |

**Assessment:** ~85% of the *energy* corpus by file count is still raw norm text or basic metadata. The reasoning layer exists but is thin relative to the text layer.

### 1.3 Analysis quality tiers

| Tier | Description | Examples in vault |
|---|---|---|
| **T0 — stub** | Frontmatter only or placeholder | Some concept notes |
| **T1 — metadata** | What it is + structure outline | Early HANRE notes before Jul 2026 refresh |
| **T2 — practitioner** | Key provisions, connections, open questions | [[Legea 108-2016 — gazele naturale (notă)]], [[HANRE 112-2019 — racordarea la retelele de gaze (notă)]] |
| **T3 — Law House** | Executive impact + risk matrix + jurisprudence + client checklist | Target standard — see [[Template — Act (notă)]] |
| **T4 — domain synthesis** | Cross-act reasoning, sector risk map | [[Energetică — synthesis]] |

**Target:** every primary anchor and operative HANRE act at **T3**; sector themes at **T4**.

### 1.4 Files missing analysis (`— notă`)

| Act | Priority | Notes |
|---|---|---|
| [[HANRE 534-2019 — Regulile pietei gazelor naturale (text)]] | **High** | Full text; no companion — **created 2026-07-28** |
| [[HANRE 423-2019 — Codul retelelor electrice (text)]] | **High** | Annex missing; decision-only analysis still valuable — **created 2026-07-28** |
| [[HANRE 169-2019 — furnizarea energiei electrice (text)]] | Medium | Text incomplete; verify L164 currency |
| [[Legea 139-2018 — eficienta energetica (text)]] | Medium | Text complete; no notă |
| [[Legea 101-2026 — consolidarea mecanismelor de interventie in situatii de criza (text)]] | Medium | Crisis package; no notă |
| Amendment-only HANRE acts (261, 310, 328, 383, 177) | Low | Linked from parent notes — intentional deferral |

### 1.5 Uploads not yet in vault

30 net-new files in `uploads/` including: Legea 92/2022, 171/2012, 202/2017, 114/2012, Cod aerian, Cod transport feroviar, HG 280/2024, HANRE 286/2018, and others. See [[Audit ingestie — 2026-07-26]] for pipeline rules.

---

## 2. Four-tier ingestion & processing workflow

```
Tier 1 — Folder restructure & metadata normalisation
  └─ YAML frontmatter on every document; act_type, domeniu[], legis_id, status

Tier 2 — Statutory anchoring & hierarchy linkage
  └─ Link HANRE → primary law → CA 116/2018; cite enabling article in every notă

Tier 3 — Deep legal analysis & risk matrix extraction
  └─ Apply Law House template to every act-note

Tier 4 — Cross-referencing & jurisprudence integration
  └─ Domain dossiers, concept notes, litigation vault, EU acquis tables
```

**Vault mapping (this repo's structure, not a separate `01_Primary_Legislation` tree):**

| Law House volume | Vault location |
|---|---|
| Vol I — Primary legislation | `10 Legislation/Laws/` + `Coduri/` |
| Vol II — Grid access & supply | `10 Legislation/Authority Acts/` (connection + supply HANRE) |
| Vol III — Tariff methodologies | `10 Legislation/Authority Acts/` + [[Energetică — metodologii tarifare (notă)]] |
| Vol IV — Market rules & renewables | HANRE 283, 534 + [[Legea 10-2016 — surse regenerabile (notă)]] |
| Vol V — Licensing, cross-border, REMIT | [[Energetică — licențiere cross-border și REMIT (notă)]] |
| Vol VI — Litigation & CSE | [[Energetică — contencios administrativ și precedente (notă)]] |

---

## 3. Standard analysis structure (Law House blueprint)

Every `— notă` companion should follow this structure. Full template: [[Template — Act (notă)]].

### 3.1 Frontmatter (extended)

```yaml
---
title: "<Act> (notă)"
type: act-note
act: "[[<Act> (text)]]"
domeniu: []
enabling_act: "[[Parent law]]"      # for HANRE acts
eu_directives: ""                    # where applicable
analysis_tier: law-house             # stub | practitioner | law-house
status: draft                        # draft | reviewed
tags: [act-note, analysis]
created:
updated:
---
```

### 3.2 Body sections

1. **Executive summary & commercial impact** — core purpose; primary business risk (callout block)
2. **Statutory hierarchy & legal foundation** — parent laws, procedural code, EU acquis
3. **Practical legal mechanics & key provisions** — obligations, deadlines, workflows
4. **Legal ambiguities, vulnerabilities & risk matrix** — table: provision | flaw | client risk | mitigation
5. **Relevant jurisprudence & ANRE practice** — CSJ / CA Chișinău / ANRE dispute board
6. **Client action checklist / compliance roadmap** — actionable checkboxes
7. **Connections in the vault** — wikilinks to concepts, MOCs, related acts
8. **Sources** — text file, doc_id, consolidation date

### 3.3 Domain dossiers (cross-act synthesis)

For themes spanning multiple acts, use `20 Domains/` with `type: domain-note`:

- [[Energetică — metodologii tarifare (notă)]] — Batch 3: tariff architecture, FD mechanism
- [[Energetică — licențiere cross-border și REMIT (notă)]] — Batch 5: licensing, CAM, REMIT
- [[Energetică — contencios administrativ și precedente (notă)]] — Batch 6: litigation, CSE

---

## 4. Six-volume deployment status

| Vol | Subject | Status | Key files |
|---|---|---|---|
| **I** | Primary legislation | ✅ Deployed | [[Legea 174-2017 — energetica (notă)]] · [[Legea 164-2025 — energia electrica (notă)]] · [[Legea 108-2016 — gazele naturale (notă)]] · [[Codul administrativ 116-2018 (notă)]] |
| **II** | Grid access & supply | ✅ Deployed | [[HANRE 311-2026 — racordarea la retelele electrice (notă)]] · [[HANRE 112-2019 — racordarea la retelele de gaze (notă)]] · [[HANRE 113-2019 — furnizarea gazelor naturale (notă)]] · [[HANRE 423-2019 — Codul retelelor electrice (notă)]] *(annex pending)* |
| **III** | Tariff methodologies | ✅ Domain dossier | [[Energetică — metodologii tarifare (notă)]] · [[HANRE 626-2023 — Metodologie tarife transport EE (notă)]] |
| **IV** | Market rules & renewables | 🔄 In progress | [[HANRE 283-2020 — Regulile pietei energiei electrice (notă)]] · [[HANRE 534-2019 — Regulile pietei gazelor naturale (notă)]] · [[Legea 10-2016 — surse regenerabile (notă)]] |
| **V** | Licensing, cross-border, REMIT | ✅ Domain dossier | [[Energetică — licențiere cross-border și REMIT (notă)]] |
| **VI** | Litigation & CSE | ✅ Domain dossier | [[Energetică — contencios administrativ și precedente (notă)]] |

---

## 5. Next execution batches

| Batch | Focus | Acts |
|---|---|---|
| **7** | Gas tariff methodologies | HANRE 535/2019, 443/2020 — not yet ingested |
| **8** | Electricity supply & QoS | HANRE 169/2019 (complete text), 422/2019 |
| **9** | Uploads ingestion | Priority: Legea 231/2010, 92/2022, HG 280/2024 |
| **10** | Jurisprudence enrichment | Populate case matrix in Vol VI dossier with real docket numbers |
| **11** | EU acquis mapping tables | Per-act directive → article → implementation tables |

---

## 6. Quality rules

1. **Never edit `— text` substance** except for consolidation updates — [[Conventions]]
2. **Honest truncation flags** — if `text_complet: false`, analysis must say so
3. **Currency checks** — L107-based HANRE acts need L164 verification
4. **Abrogation tracking** — historical notes must carry `[!danger] ABROGATED` callouts
5. **Procedure first** — any challenge route must cite [[Codul administrativ 116-2018 (notă)]] art. 162–167 (prior complaint) and art. 214 (suspension)
