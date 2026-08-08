---
title: "Roadmap — Fiscalitate & Contabilitate analysis architecture"
type: project
tags: [project, roadmap, fiscal, contabilitate, analysis]
created: 2026-08-08
updated: 2026-08-08
status: active
---

# Roadmap — Fiscalitate & Contabilitate analysis architecture

Reorganise the tax & accounting **analysis layer** so a practitioner can navigate by **(A) how acts talk to each other** and **(B) tax / regime / procedure segments** — not only by Titlu inventory or by headline rates.

Corpus status, live reforms and ingest gaps remain tracked in [[Fiscalitate & Contabilitate — horizon and gaps]]. This note is the **structuring** track. Method: [[Playbook — Domain analysis architecture (other hubs)]]. Energy exemplar (complete): [[Roadmap — Energy analysis architecture]].

> [!tip] Entry point for the new layer
> **[[Fiscalitate & Contabilitate — architecture map]]**. First hub: [[MOC — Impozit pe venit]]. Master inventory: [[MOC — Fiscalitate & Contabilitate]]. Narratives: [[Fiscalitate — synthesis]] · [[Contabilitate & raportare financiară — synthesis]].

---

## Why restructure (gap vs Energy depth)

The vault already has strong pieces:

- [[Fiscalitate — synthesis]] — system architecture, live rates, procedure sketch
- [[Contabilitate & raportare financiară — synthesis]] — L287 tiers + 2027 L86 reset
- [[Fiscalitate & Contabilitate — horizon and gaps]] — 2026 live reforms, 2027 draft watch, ingest gaps
- [[MOC — Fiscalitate & Contabilitate]] — act inventory by instrument
- [[Codul fiscal 1163-1997 (notă)]] — Titlu-by-Titlu master analysis
- Atomic concepts: income tax · VAT · excise · residence · financial statements · IT Park · AOAM · statutory audit

What is missing for practitioner / structuring work at **Energy depth or deeper**:

1. An explicit **inter-law communication map** (vertical cascade *and* horizontal bridges: CF ↔ Customs ↔ L287 ↔ CNAS/CNAM ↔ annual fiscal-policy law ↔ IT Park)
2. A stable **segmentation spine** reusable across tax types (regime / base / actors / filings / procedure stage / incentives / cross-border)
3. Dedicated **per-tax hubs** (income, VAT, excise+customs, payroll wedge, fiscal administration, accounting) instead of one catalogue MOC
4. Named **conflict & currency themes** (annual rate volatility; draft ≠ law; accounting profit ≠ taxable profit; border vs inland administrator)
5. Stubbed coverage for thin areas and the **2027 Estonian-style CIT draft** so gaps are visible rather than silent
6. Cross-cutting layers: DTT network, accounting↔tax bridge, energy×tax, digital compliance (e-Factura / portal notices)

**Depth target vs Energy:** Energy organised by *market vector*. Tax organises by *tax type + procedure stage*, with an extra permanent axis — the **annual currency calendar** — because rates/thresholds move every 1 January. Accounting is a full hub (not a side note), because it supplies the tax base and company-law triggers.

---

## Organising principle — two axes (+ currency calendar)

| Axis | Question it answers | Primary home |
|---|---|---|
| **A — Inter-law map** | Which act creates the duty, which act operationalises it, which act amends rates this year? | [[Fiscalitate & Contabilitate — architecture map]] |
| **B — Tax / regime segmentation** | Which tax, regime, or procedure stage, and who acts? | Per-tax MOCs under `50 MOCs` |
| **C — Currency calendar** | What is live *this year* vs draft / deferred IF? | Horizon note + architecture map §2 |

Keep [[Fiscalitate — synthesis]] and [[Contabilitate & raportare financiară — synthesis]] as short practitioner narratives. Do **not** turn them into catalogues. Catalogues live in MOCs; bridges live in the architecture map; doctrines stay atomic in `30 Concepts`.

---

## Gap analysis vs Energy DoD (honest baseline — Aug 2026)

| DoD item (Energy playbook) | Energy status | Fiscalitate status before this roadmap |
|---|---|---|
| Architecture map (cascade + bridges + conflict rules) | ✅ | ❌ → **Step 1** |
| Segmentation spine (same columns per hub) | ✅ | ❌ → **Step 1 taxonomy** |
| One filled hub at a time | ✅ 5 vectors + stubs | ❌ one catalogue MOC only → **Step 1 income hub** |
| Segment briefs + concepts per hub | ✅ | Partial concepts; **no** segment briefs |
| Cross-cutting layers | ✅ prosumers / incentives / ESG | Thin (energy×tax named as gap) |
| Gap stubs for absent / draft regimes | ✅ coal / H₂ / geothermal | ❌ 2027 draft not stubbed as architecture |
| Synthesis rewritten against map | ✅ | Still rate-first narrative |
| Completeness & actuality audit note | ✅ | Horizon gaps only (ingest-focused) |

---

## Phased plan

### Step 0 — Currency & ingestion map *(precondition — already present)*
- Treat [[Fiscalitate & Contabilitate — horizon and gaps]] as the Step 0 deliverable (structure · 2026 live · 2027 pipeline · gap list)
- Do **not** invent a parallel status note until the architecture audit (Step 11) needs one
- Rule: every hub cites the horizon note for figures; never hard-wire draft 2027 rates as live

### Step 1 — Architecture + income-tax hub ✅ *(2026-08-08)*
- Publish [[Fiscalitate & Contabilitate — architecture map]] (cascade + horizontal bridges + conflict themes + full tax/regime taxonomy)
- Publish [[MOC — Impozit pe venit]] as the first regulation-oriented tax hub (regimes, actors, filings, accounting bridge, governing acts)
- Wire into [[MOC — Fiscalitate & Contabilitate]], [[Fiscalitate — synthesis]], [[Home]], [[00 - Index general]], [[Playbook — Domain analysis architecture (other hubs)]], [[00 Inbox/Roadmap]]

### Step 2 — Income-tax deep fill
- Regime briefs note: [[Fiscalitate — regimuri impozit pe venit (notă)]] *(to create)* — standard CIT · agri 7% · SME 4% turnover · art. 87(11) deferral · IT Park single tax · independent entrepreneurs (cap. 10⁴) · dividend WHT · salary withholding · PE / non-resident
- Concepts to harden or add: deferred CIT · SME turnover regime · withholding agent · permanent establishment (if thin) · independent-entrepreneur single tax
- Boundary note: **salary vs dividend vs turnover regimes** (structuring matrix already sketched in [[Concept — Impozit pe venit]] — promote to dedicated note)
- Verdict flags: **2027 Estonian-style draft ≠ law**; art. 87(11) ends **2026** unless extended

### Step 3 — VAT hub
- [[MOC — TVA]] *(to create)* · [[Fiscalitate — segmente TVA (notă)]] *(to create)*
- Cover: taxable person · registration threshold · rates · place of supply · deduction · refund (HG 93 / HG 829) · reverse charge art. 101⁷ · e-Factura · energy bridges
- Concept deepen: [[Concept — TVA]] article-anchored refresh after each fiscal-policy law

### Step 4 — Excise + customs interface hub
- [[MOC — Accize și vamă]] *(to create)* · segment briefs
- Stack: CF Titlul IV ↔ [[Codul vamal 95-2021 (notă)]] ↔ Serviciul Vamal
- Gap: Serviciul Vamal authority profile; transfer-pricing secondaries stay P2

### Step 5 — Payroll wedge hub
- [[MOC — Salarizare și contribuții]] *(to create)* — PIT (Titlul II Cap. 15) + [[Legea 489-1999 — sistemul public de asigurari sociale (notă)|CNAS L489]] + [[Legea 1593-2002 — prime asigurare medicala obligatorie (notă)|AOAM L1593]]
- Concepts: [[Concept — Prima AOAM]] · employer CNAS · IPC21 filing ([[OMF 128-2024 — modificare formular IPC21 (notă)|OMF 128]] / parent OMF 94 gap)
- Authority stubs: CNAS profile; deepen [[CNAM]]

### Step 6 — Fiscal administration & dispute hub
- [[MOC — Administrare fiscală și contestații]] *(to create)* · [[Fiscalitate — control și contestație (notă)]] *(dispute workflow — named gap in horizon)*
- Sequence: control → decision → SFS contestation → Codul administrativ court · enforcement / suspension
- Bridge: [[MOC — Proceduri]] · [[SFS]]

### Step 7 — Accounting & reporting hub
- [[MOC — Contabilitate și raportare financiară]] *(to create)* · size-tier / obligation matrix
- Stack: [[Legea 287-2017 — contabilitate (notă)|L287]] · [[Legea 86-2026 — modificare Legea contabilitatii (notă)|L86 IF 1 Jan 2027]] · [[Legea 271-2017 — auditul situatiilor financiare (notă)|L271]] · SNC gateway [[OMF 118-2013 — Standardele Nationale de Contabilitate (notă)|OMF 118]]
- Concepts: [[Concept — Situații financiare]] · [[Concept — Audit statutar]]
- Explicit gap stub: **individual SNC texts** not ingested

### Step 8 — Special regimes, incentives & 2027 draft stub
- [[Fiscalitate — regimuri speciale și stimulente (notă)]] *(to create)* — IT Park ([[Concept — Parc IT]] · L77) · art. 87(11) · SME 4% · energy connection-asset deduction · ESOP annex under HG 829
- **Gap stub:** [[Fiscalitate — proiect CIT tip Estonian 2027 (gap stub)]] *(to create)* — draft ≠ law; watch MF project; rewrite Titlul II when enacted
- Cross-link energy incentives only where tax-relevant (reverse charge, connection gifts)

### Step 9 — Local / property / resource / road taxes
- Thin hub or stubs: Titlurile VI · VI¹ · VII · VIII · IX
- Do not fake market depth; label cells *thin corpus* where analysis stays Titlu-level

### Step 10 — Cross-cutting layers
1. [[Fiscalitate — punte contabilitate-impozit (notă)]] — non-deductibles, depreciation, provisions, art. 87(11), TP
2. [[Fiscalitate — energie × tax (notă)]] — art. 101⁷ · 8% gas transport VAT · connection-asset deduction
3. [[Fiscalitate — tratate de evitare a dublei impuneri (notă)]] — DTT table (RO, UA corridors, NL, DE, US…) — ingest texts P1
4. Digital compliance layer — e-Factura · governmental portal notices from 1 Jan 2027 · B2G e-invoicing (IF = EU accession)

### Step 11 — Synthesis rewrite + audit
- Rewrite [[Fiscalitate — synthesis]] as architecture entry (point at map + hubs; keep rates table short + dated)
- Retune [[Contabilitate & raportare financiară — synthesis]] against the accounting hub
- Completeness & actuality audit: [[Fiscalitate & Contabilitate — audit analysis layer (notă)]] *(to create)*
- Update playbook with lessons learned

---

## Definition of done (per tax / regime hub)

A hub is “filled” when it has:

1. Primary + secondary acts that govern it (with **currency flags** and IF dates)
2. Regime / segment table (even if some cells are *not yet organised*)
3. Actor map (taxpayer types, withholding agents, administrators)
4. Filing / registration / certificate list
5. Links to procedure (Titlul V) and accounting bridge where the base matters
6. Cross-links to incentives / special regimes / cross-border / energy where relevant
7. Explicit **gaps** (missing secondaries, draft instruments, incomplete texts)

---

## Sequencing rule

**Do not open Step N+1 until Step N has a navigable stub.** Prefer one complete hub over eight empty folders. **Income tax first** because the corpus and structuring questions are densest (CIT regimes · distributions · art. 87(11) · IT Park · independent entrepreneurs). VAT second because transaction architecture + refund + energy reverse charge are the next densest live file. Procedure hub early enough that dispute advice is not orphaned (Step 6), but after the main substantive taxes so appeals have something to attach to.

**Currency rule (stricter than Energy):** every numeric cell carries a verification month; annual fiscal-policy law is assumed to move Titlul II/III/IV figures every 1 January.

---

## Related
[[Fiscalitate & Contabilitate — architecture map]] · [[MOC — Impozit pe venit]] · [[MOC — Fiscalitate & Contabilitate]] · [[Fiscalitate — synthesis]] · [[Contabilitate & raportare financiară — synthesis]] · [[Fiscalitate & Contabilitate — horizon and gaps]] · [[Playbook — Domain analysis architecture (other hubs)]] · [[Roadmap — Energy analysis architecture]] · [[00 Inbox/Roadmap]] · [[Codul fiscal 1163-1997 (notă)]] · [[SFS]]
