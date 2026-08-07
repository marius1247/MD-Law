---
title: "Roadmap — Energy analysis architecture"
type: project
tags: [project, roadmap, energetică, analysis]
created: 2026-08-07
updated: 2026-08-07
status: in-progress
---

# Roadmap — Energy analysis architecture

Reorganise the energy **analysis layer** so a practitioner can navigate by **(A) how acts talk to each other** and **(B) market segments from a regulatory perspective** — not only by instrument type or by the four classic regulatory problems.

Corpus status and ingestion remain tracked in [[Status ingestie — Energetica]] and [[00 Inbox/Roadmap|the main vault roadmap]]. This note is the **structuring** track only.

> [!tip] Entry point for the new layer
> **[[Energetică — architecture map]]**. Electricity: [[MOC — Piața de energie electrică]]. Gas: [[MOC — Piața gazelor naturale]]. Petroleum: [[MOC — Piața produselor petroliere]] · coal gap [[Energetică — cărbune gap stub (notă)]]. Thermal: [[MOC — Piața energiei termice]] · geothermal gap [[Energetică — geotermal gap stub (notă)]].

---

## Why restructure

The vault already has strong pieces:

- [[Energetică — synthesis]] — practitioner read organised around four regulatory *problems*
- [[MOC — Energetică]] — act inventory by tier
- Sector dossiers (electricity / gas / tariffs / REMIT / contencios)
- Atomic concepts for selected doctrines

What is missing for market / regulatory work:

1. An explicit **inter-law communication map** (vertical cascade *and* horizontal bridges between electricity, gas, RES, heat, petroleum, efficiency, crisis, EnC)
2. A stable **market-segmentation spine** (DAM / ID / balancing / capacity / LT contracts; actors; regulated activities) reusable across energy vectors
3. Dedicated homes for **prosumers, incentives, ESG** as cross-cutting layers
4. Stubbed coverage for thin or absent vectors (hydrogen, coal, geothermal) so gaps are visible rather than silent

---

## Organising principle — two axes

| Axis | Question it answers | Primary home |
|---|---|---|
| **A — Inter-law map** | Which act creates the duty, which act operationalises it, which act amends or overrides it? | [[Energetică — architecture map]] |
| **B — Market segmentation** | Which market / activity / actor is regulated, and by what? | Per-vector MOCs under `50 MOCs` |

Keep [[Energetică — synthesis]] as the short practitioner narrative. Do **not** turn it into a catalogue. Catalogues live in MOCs; bridges live in the architecture map; doctrines stay atomic in `30 Concepts`.

---

## Phased plan

### Step 1 — Architecture + electricity market hub ✅
- Publish [[Energetică — architecture map]] (cascade + horizontal bridges + full-vector taxonomy)
- Rewrite [[MOC — Piața de energie electrică]] as the first regulation-oriented market hub (segments, actors, regulated activities, governing acts)
- Wire into [[MOC — Energetică]], [[Energetică — synthesis]], [[Home]], [[00 - Index general]]

### Step 2 — Electricity deep fill ✅ *(2026-08-07)*
- Segment briefs + licensing inventory: [[Energetică — segmente piață electricitate (notă)]]
- Concepts (batch A): [[Concept — OPEED]] · [[Concept — Consumator activ]] · [[Concept — Agregator independent]] · [[Concept — Stocare a energiei]] · [[Concept — Comunitate de energie a cetățenilor]]
- Concepts (batch B): [[Concept — Contract la prețuri dinamice]] · [[Concept — Furnizor central de energie electrică]]
- Boundary: [[Energetică — prosumer vs consumator activ (notă)]]
- Verdicts: **no live capacity market** (L164 arts. 49–51 toolbox only); HANRE 286 is **not** the licensing regulation

### Step 3 — Gas market hub ✅ *(2026-08-07)*
- [[MOC — Piața gazelor naturale]] · [[Energetică — segmente piață gaze (notă)]]
- Concept: [[Concept — Punct virtual de tranzacționare]]
- Live flags: third-package lag vs L164; industrial PSO withdrawal → **1 Apr 2026**; unbundling/TSO certification currency

### Step 4 — Petroleum products (+ coal gap) ✅ *(2026-08-07)*
- [[MOC — Piața produselor petroliere]] · [[Energetică — segmente piață petrol (notă)]]
- [[Concept — Preț maxim ANRE produse petroliere]]
- Coal: [[Energetică — cărbune gap stub (notă)]] — **no dedicated ANRE coal market**; PNIEC/reserves/customs/environment

### Step 5 — Thermal / CHP / geothermal ✅ *(2026-08-07)*
- [[MOC — Piața energiei termice]] · [[Energetică — segmente piață termică (notă)]]
- Concept: [[Concept — Cogenerare de înaltă eficiență]]
- Verdict: **local public-service tariffs**, not PZU/PVT; CHP electricity → L164 / transitional FCEE; HANRE 23 body still incomplete
- Geothermal: [[Energetică — geotermal gap stub (notă)]] — RES (L10) / SACET (L92) / **no** dedicated market; PNIEC **PM_DC25** watch

### Step 6 — Biofuels & hydrogen

- Biofuels: [[HG 53-2025 — durabilitate biocarburanti emisii GES (notă)|HG 53/2025]] + L10 / fuel-quality bridges
- Hydrogen: map EnC / EU acquis expectations vs MD primary law silence; keep as **watch-list vector**, not fake completeness

### Step 7 — Cross-cutting layers
Three thin synthesis notes (or MOCs if they grow):
1. **Prosumers & active consumers** — seed already: [[Energetică — prosumer vs consumator activ (notă)]] · L10 net billing · L164 consumator activ / CEC · HANRE 311 / 169 / 833 · [[Concept — Facturare netă]]
2. **Incentives & support** — eligible producers, fixed tariff / auctions, [[Concept — Furnizor central de energie electrică|FCEE]], FEE/CNED, vulnerability fund L241
3. **ESG / climate governance** — HG 10/2024 · PNIEC HG 86/2025 · L139 efficiency · non-financial reporting bridge in accounting law · biofuel GHG

### Step 8 — Synthesis rewrite
Retune [[Energetică — synthesis]] so §1–2 point at the architecture map, § market design expands by vector, and open threads map to Steps 2–7 rather than only ingestion gaps.

> [!note] Professional deepening pass *(2026-08-07)*
> Steps 1–5 hubs received a **professional legal analysis** pass: architecture map §1.3 conflict themes; per-vector risk matrices on electricity / gas / petroleum / thermal MOCs; FCEE art. 150(3)–(4) hardened; FUO ≥6m vs HANRE 169 90d conflict surfaced; gas unbundling/PSO/reconciliation/servitude lifted from L108 note; petroleum crisis decision tree; thermal Cap. VI + dual-statute CHP checklist. Synthesis §4 updated. Incomplete sources remain flagged (HANRE 23 body, 201/2017, 535 annex, L461 Annex 2 OCR, HG 197 placeholders).

---

## Definition of done (per vector hub)

A market hub is “filled” when it has:

1. Primary + secondary acts that govern it (with currency flags)
2. Market segments table (even if some cells are *not yet organised*)
3. Actor map
4. Regulated activities / licensing list
5. Links to monopoly layer (network codes, tariffs, connection)
6. Cross-links to support / PSO / crisis / ESG where relevant
7. Explicit **gaps** (missing acts, package lag, transitional HANRE)

---

## Sequencing rule

**Do not open Step N+1 until Step N has a navigable stub.** Prefer one complete hub over seven empty folders. Electricity first because the corpus and concepts are densest; gas second because the package lag is the live legislative story.

## Related
[[Energetică — architecture map]] · [[MOC — Piața de energie electrică]] · [[MOC — Piața gazelor naturale]] · [[MOC — Piața produselor petroliere]] · [[MOC — Piața energiei termice]] · [[Energetică — segmente piață electricitate (notă)]] · [[Energetică — segmente piață gaze (notă)]] · [[Energetică — segmente piață petrol (notă)]] · [[Energetică — segmente piață termică (notă)]] · [[Energetică — cărbune gap stub (notă)]] · [[Energetică — geotermal gap stub (notă)]] · [[Energetică — synthesis]] · [[MOC — Energetică]] · [[00 Inbox/Roadmap]]
