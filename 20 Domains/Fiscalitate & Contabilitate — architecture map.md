---
title: "Fiscalitate & Contabilitate — architecture map"
type: domain-note
domeniu: [fiscal, contabilitate]
tags: [domain, analysis, fiscal, contabilitate, architecture, inter-law, segmentation]
status: draft
created: 2026-08-08
updated: 2026-08-08
deepening: step-1
---

# Fiscalitate & Contabilitate — architecture map

How Moldovan **tax and accounting** acts **communicate**, and how the analysis layer should be **segmented by tax / regime / procedure** from a practitioner perspective.

Hub inventory: [[MOC — Fiscalitate & Contabilitate]] · First Axis-B hub: [[MOC — Impozit pe venit]] · Tax narrative: [[Fiscalitate — synthesis]] · Accounting narrative: [[Contabilitate & raportare financiară — synthesis]] · Currency / gaps: [[Fiscalitate & Contabilitate — horizon and gaps]] · Build plan: [[Roadmap — Fiscalitate & Contabilitate analysis architecture]]

> [!abstract] Use this note as the spine
> For “which law speaks to which?” → §1–3. For “how do we cut taxes and regimes?” → §4–5. For “what is filled vs stubbed?” → §6. For live rates → synthesis + horizon — **never this map alone**.

> [!warning] Currency is the domain’s primary risk
> The Fiscal Code is amended by the **annual fiscal-policy law** effective **1 January**, every year. Figures in sister notes are stamped July / August 2026. **Draft 2027 Estonian-style CIT is not law.** Re-verify at [SFS](https://sfs.md) / [MF](https://mf.gov.md) before quoting numbers.

---

## 1. Two kinds of communication between acts

### 1.1 Vertical cascade (delegation)

```
Parliament — Codul fiscal 1163/1997 (Titluri I–X)  + annual fiscal-policy law (e.g. L318/2025)
        ↓  temei legal / rate & threshold amendments each 1 Jan
Government — HG (VAT refund HG 93, omnibus HG 829, IT Park registration HGs, …)
        ↓
Ministry of Finance — OMF (SNC gateway 118, IPC21 forms, methodological orders)
        ↓
SFS — individual decisions, guidance, comerciant list, enforcement  ← mostly not ingested
        │
        ├── parallel administrator: Serviciul Vamal (border: duty + import VAT/excise)
        ├── parallel: CNAS (social contributions L489) · CNAM / AOAM (L1593)
        └── accounting stack (feeds the tax base):
              L287/2017 → L86/2026 (IF 1 Jan 2027) → SNC / IFRS → L271 statutory audit
```

**Reading rule:** an operational obligation on rates, bases and taxpayer duties is almost always in the **Codul fiscal Titlu** (as last amended by the annual package). Secondary acts operationalise *procedure* (refund clocks, forms, SNC). Challenging an SFS decision starts with the enabling Titlu article and the contestation clock in Titlul V — missing the deadline loses the case regardless of substance. See [[Fiscalitate — synthesis]] §7 · [[SFS]].

### 1.2 Horizontal bridges (same-tier talk)

Tax, customs, accounting and social contributions do **not** sit in silos. They **call**, **defer**, **replace** or **override** each other.

| From | To | How they communicate | Practical effect |
|---|---|---|---|
| [[Codul fiscal 1163-1997 (notă)\|CF Titlul I]] | All Titluri + treaties | Definitions, residence, taxpayer duties, treaty primacy (art. 4) | Interpretive key before any substantive Titlu |
| CF Titlul II | [[Legea 287-2017 — contabilitate (notă)\|L287]] | Taxable profit **starts from** accounting profit and adjusts | Always keep the book-to-tax reconciliation |
| CF Titlul II | CF Titlul III | SME **4% turnover** regime requires staying **outside VAT**; threshold interaction | Model VAT registration and CIT regime **together** |
| CF Titlul II / X | [[Legea 77-2016 — parcuri tehnologia informatiei (notă)\|L77]] | IT Park **status** lives in L77; **single tax** mechanics in Titlul X | Loss of status re-opens ordinary Titlul II |
| CF Titlul III | [[Codul vamal 95-2021 (notă)\|Codul vamal]] | Import VAT / excise collected at the border as *drepturi de import* | Inland SFS vs border Vamal — different administrator |
| CF Titlul III | [[HG 93-2013 — restituirea TVA (notă)\|HG 93]] · [[HG 829-2025 — modificare acte fiscale vamale audit (notă)\|HG 829]] | Refund clocks, reverse-charge excess chapters, ESOP annex | Refund advice is HG-tier, not CF alone |
| CF Titlul III art. **101⁷** | [[Energetică — synthesis]] · energy traders | Domestic EE/gas reverse charge to *comerciant* | Declare comerciant status to [[SFS]]; invoice without VAT |
| CF Titlul IV | Codul vamal · warehousekeepers | Excise stamps, import excise, authorised warehouses | Goods-specific + annex-sensitive |
| CF Titlul V | [[Codul administrativ 116-2018 (notă)\|Codul administrativ]] | Contestation → judicial review | [[MOC — Proceduri]] |
| CF Cap. 15 / payroll | [[Legea 489-1999 — sistemul public de asigurari sociale (notă)\|L489]] · [[Legea 1593-2002 — prime asigurare medicala obligatorie (notă)\|L1593]] | PIT withholding sits beside CNAS 24% + AOAM ~9% | Payroll wedge is **multi-statute** |
| L287 | [[Legea 271-2017 — auditul situatiilor financiare (notă)\|L271]] · company law | Size tier → audit / consolidation; accounts → distributable profit / net-assets trigger | [[Societăți & guvernanță — synthesis]] |
| [[Legea 318-2025 — modificare acte fiscale (notă)\|L318/2025]] (+ successors) | CF Titluri II–IV chiefly | Annual rate / threshold / exemption rewrite | **Currency calendar** — assume 1 Jan move |
| [[Legea 41-2026 — suport desfasurare afaceri (notă)\|L41/2026]] | CF Titlul III | VAT registration threshold **1.7 MDL m** | SME 4% modelling input |
| [[Legea 86-2026 — modificare Legea contabilitatii (notă)\|L86/2026]] | L287 | Size thresholds **IF 1 Jan 2027** | Many entities drop a reporting/audit category |
| [[Legea 125-2024 — modificare parc IT si tranzitii vamale (notă)\|LP125]] | L77 · customs transitions | Omnibus IT Park / customs | Status + border transitions |
| Public finance / BNM omnibus | [[Legea 327-2025 — managementul finantelor publice (notă)\|L327]] · [[Legea 187-2025 — modificare BNM (notă)\|L187]] | Staged IF → 2027; fiscal/customs touchpoints | Watch when advising banks / public entities |

**Reading rule for bridges:** when two acts both seem to answer the question, ask which one is *substantive tax* (CF Titlu), which is *annual amendment*, which is *procedure / refund / form*, which is *accounting base*, and which is *parallel payroll / border administrator*. Cite the lowest tier that actually binds, and the enabling article that authorised it.

### 1.3 Conflict & transitional themes (practitioner rules)

| Theme | Rule | Live exemplars |
|---|---|---|
| **Annual rate volatility** | Never quote a rate from a synthesis without a verification month. Prefer CF consolidation + annual fiscal-policy law over memory | L318/2025 package; L41 VAT threshold; every 1 Jan |
| **Draft ≠ law** | Government *politica fiscală* projects are contingency only until MO publication and IF | **2027 Estonian-style distributed-profit CIT** — not live |
| **Accounting profit ≠ taxable profit** | Book result under L287/SNC/IFRS is the *start*, not the answer. Adjustments in Titlul II control | Non-deductibles · fiscal depreciation · provisions · TP · art. 87(11) timing |
| **Four distinct gates (tax analogue)** | **Regime election ≠ VAT registration ≠ IT Park status ≠ accounting size category**. Clearing one never substitutes for another | 4% SME dies on VAT registration; IT Park needs L77 status + Titlul X; L86 reclass does not change CIT rate |
| **Administrator split** | Inland taxes → [[SFS]]; border duty/import VAT/excise → Serviciul Vamal; social → CNAS; health % → CNAM/SFS collection limbs | Do not file a customs dispute as a Titlul V contestation |
| **Enforcement does not pause on appeal** | Contestation ≠ automatic suspension; account seizure is fast | Titlul V · [[SFS]] |
| **Deferred IF vs live text** | Enacted but future IF must be modelled early and labelled clearly | L86 thresholds **IF 1 Jan 2027**; art. 87(11) through **2026**; L135 social coordination IF = EU accession |
| **Energy × tax overlays** | Sectoral energy law can create deductible transfers / reverse-charge duties without changing the tax Titlu architecture | Connection-asset gifts (L164 bridge); art. 101⁷; 8% VAT on gas transport |
| **Special regime primacy** | Where a single tax or turnover regime applies, ordinary Titlul II/III rules are displaced *only to the extent* the special statute says | IT Park Titlul X · independent entrepreneurs cap. 10⁴ · 4% SME |

**Advice formula:** (1) name the tax Titlu and the regime gate; (2) cite the lowest tier that binds + annual amendment if rates; (3) currency-check verification month and any deferred IF; (4) state whether SFS, Vamal, CNAS or CNAM administers; (5) if structuring, model the **whole extraction chain** (salary / dividend / turnover / IT Park), never a single headline rate.

---

## 2. Currency calendar (the legislative forecast)

| Layer | Domestic frame | Signal |
|---|---|---|
| Substantive taxes | CF 1163/1997 Titluri I–X as amended | **Live** — verify rates annually |
| 2026 fiscal-policy / omnibus | [[Legea 318-2025 — modificare acte fiscale (notă)\|L318/2025]] · [[Legea 41-2026 — suport desfasurare afaceri (notă)\|L41]] · [[HG 829-2025 — modificare acte fiscale vamale audit (notă)\|HG 829]] | Live staged IF |
| Accounting thresholds | [[Legea 86-2026 — modificare Legea contabilitatii (notă)\|L86/2026]] | Enacted · **IF 1 Jan 2027** — model now |
| Deferred CIT | CF art. 87(11) | Through **2026** unless extended |
| **2027 CIT rewrite draft** | MF *politica fiscală 2027* project | **Not law** — Estonian-style distributed profit (indicative 15%) / progressive PIT — gap stub in Step 8 |
| Full CF / Customs rewrite concept | Long-running MF concept | Do not hard-wire architecture until draft text exists |
| Digital notices / B2G e-invoice | Portal notices from 1 Jan 2027; B2G IF = EU accession | Procedure / procurement bridges |
| EU social coordination | [[Legea 135-2026 — coordonare securitate sociala UE (notă)\|L135/2026]] | IF = accession |

Annual amendment of CF rates is the best predictor of what changes next — stronger than any single sectoral rewrite. Full table: [[Fiscalitate & Contabilitate — horizon and gaps]].

---

## 3. Inter-law map (compact diagram)

```
                         ┌──────────────────────────────────────┐
                         │  Annual fiscal-policy law (1 Jan)    │
                         │  e.g. L318/2025 · successors         │
                         └──────────────────┬───────────────────┘
                                            │ amends rates / thresholds
                         ┌──────────────────▼───────────────────┐
                         │  Codul fiscal 1163/1997 (Titluri)     │
                         └──────────────────┬───────────────────┘
        ┌──────────┬───────────┬────────────┼────────────┬───────────┐
        ▼          ▼           ▼            ▼            ▼           ▼
     Titlul II  Titlul III  Titlul IV    Titlul V     Titlul X    VI–IX
     income      VAT         excise      procedure    IT Park    local etc.
        │          │           │            │            │
        │          ├───────────┤            │            │
        │          ▼           ▼            │            ▼
        │     Codul vamal   HG 93/829       │         L77 status
        │     Serviciul Vamal  refunds      │
        │                                   ▼
        │                          SFS contestation → Cod administrativ
        │
        ├──────────────────► L489 CNAS · L1593 AOAM  (payroll wedge)
        │
        └──────────────────► L287 / L86 / SNC / L271  (accounting base)
                                     │
                                     ▼
                          Company law (distributable profit, net assets)
```

---

## 4. Tax / regime segmentation taxonomy (practitioner lens)

Every tax hub is analysed with the **same columns**. Cells may be empty — that is information.

### 4.1 Columns (apply to each hub)

| Column | Meaning |
|---|---|
| **Regimes / segments** | Distinct legal bases or election tracks (standard, turnover, single tax, reverse charge, …) |
| **Actors** | Who the law names (taxpayer types, withholding agents, administrators) |
| **Filings / registrations** | Returns, certificates, registrations, declarations that open or close a regime |
| **Base & timing** | What is measured and when (profit, turnover, transaction, payroll) |
| **Procedure layer** | Control → assessment → contestation → enforcement hooks |
| **Incentives / special regimes** | Status-dependent displacements of the ordinary rules |
| **Cross-border / DTT** | Residence, PE, WHT, treaty relief |
| **Accounting / company-law hooks** | Where L287 or SA/SRL rules constrain the tax answer |

### 4.2 Standard income-tax regime list (filled in [[MOC — Impozit pe venit]])

| Regime | MD label / home | Regulatory character |
|---|---|---|
| Standard CIT | Impozit pe venit — persoane juridice | Profit-based; 12% orientation (verify) |
| Agricultural | Cota redusă agricultură | Profit-based special rate |
| SME turnover | Regim 4% din venitul din livrări | Turnover; **non-VAT** gate |
| Deferred CIT | Art. 87(11) | Timing of *payment* until distribution (through 2026) |
| IT Park single tax | Impozit unic (Titlul X) | Turnover 7%; replaces most taxes if L77 status |
| Independent entrepreneurs | Cap. 10⁴ | 15%/35% single tax; no books; SFS from ECC + bank |
| PIT (employment) | Cap. 15 withholding | Wage tax + payroll wedge bridges |
| Dividend / other WHT | Retenție la sursă | 6% dividends orientation; treaty relief |
| Non-resident / PE | Cap. non-rezidenți | Source rules + DTT tie-breakers |

### 4.3 Hubs to mirror (later steps)

| Hub | Status | Primary acts |
|---|---|---|
| **Impozit pe venit** | ✅ Step 1 | CF Titlul II · X · L77 · L41 interaction · [[MOC — Impozit pe venit]] |
| **TVA** | ⏳ Step 3 | CF Titlul III · HG 93/829 · L41 · art. 101⁷ |
| **Accize + vamă** | ⏳ Step 4 | CF Titlul IV · Codul vamal |
| **Salarizare & contribuții** | ⏳ Step 5 | CF Cap. 15 · L489 · L1593 · IPC21 |
| **Administrare fiscală** | ⏳ Step 6 | CF Titlul V · Codul administrativ · [[SFS]] |
| **Contabilitate & raportare** | ⏳ Step 7 | L287 · L86 · L271 · OMF 118 |
| **Regimuri speciale / stimulente** | ⏳ Step 8 | IT Park · 87(11) · energy×tax · ESOP |
| **2027 CIT draft** | ⏳ Step 8 stub | Draft ≠ law |
| **Local / property / resource / road** | ⏳ Step 9 | Titlurile VI–IX (thin) |

### 4.4 Cross-cutting layers (Step 10)

| Layer | Why separate | Seed material already in vault |
|---|---|---|
| **Accounting ↔ tax bridge** | Reconciliation is the first control document | Syntheses + [[Concept — Situații financiare]] · [[Concept — Impozit pe venit]] |
| **Energy × tax** | Reverse charge + reduced VAT + connection gifts | Horizon gaps · art. 101⁷ · [[Energetică — synthesis]] |
| **DTT network** | WHT and residence override domestic tests | [[Concept — Rezident fiscal]] · CF art. 4 — **texts still P1 gap** |
| **Digital compliance** | e-Factura, portal service, B2G e-invoice | Horizon §3 · procurement bridge |

---

## 5. Where existing notes sit in the new spine

| Existing note | Role under new architecture |
|---|---|
| [[Fiscalitate — synthesis]] | Practitioner narrative (architecture sketch, rates, procedure) — keep short; retune at Step 11 |
| [[Contabilitate & raportare financiară — synthesis]] | Accounting narrative — feeds Step 7 hub |
| [[Fiscalitate & Contabilitate — horizon and gaps]] | **Step 0** currency / ingest / reform map |
| [[MOC — Fiscalitate & Contabilitate]] | Master act inventory by instrument |
| [[MOC — Impozit pe venit]] | **Axis B hub — income tax** (regimes, actors, filings) |
| [[Codul fiscal 1163-1997 (notă)]] | Titlu-by-Titlu master analysis — remains the deep CF companion |
| [[Codul vamal 95-2021 (notă)]] | Border stack — feeds Step 4 |
| [[SFS]] · [[CNAM]] | Authority profiles — CNAS / Vamal / CSPA still open |
| `30 Concepts/*` (tax) | Atomic doctrines — do not duplicate into MOCs |
| Energy architecture / hubs | Horizontal bridges only (VAT reverse charge, connection gifts, 8% gas transport) |

---

## 6. Fill status & next action

| Step | Deliverable | Status |
|---|---|---|
| 0 | Horizon / currency map | **Done** — [[Fiscalitate & Contabilitate — horizon and gaps]] |
| 1 | This map + income-tax MOC | **Done (2026-08-08)** — [[MOC — Impozit pe venit]] |
| 2 | Income deep fill (regime briefs + concepts) | **Next** |
| 3 | VAT hub | Pending |
| 4 | Excise + customs hub | Pending |
| 5 | Payroll wedge hub | Pending |
| 6 | Administrare fiscală / dispute hub | Pending |
| 7 | Accounting & reporting hub | Pending |
| 8 | Special regimes + 2027 draft stub | Pending |
| 9 | Local / property / resource / road | Pending |
| 10 | Cross-cutting layers | Pending |
| 11 | Synthesis rewrite + audit | Pending |

**Next action:** Step 2 — publish income-tax regime briefs and harden structuring concepts; do not open the VAT hub until Step 2 is navigable.

## Related
[[Roadmap — Fiscalitate & Contabilitate analysis architecture]] · [[MOC — Impozit pe venit]] · [[MOC — Fiscalitate & Contabilitate]] · [[Fiscalitate — synthesis]] · [[Contabilitate & raportare financiară — synthesis]] · [[Fiscalitate & Contabilitate — horizon and gaps]] · [[Playbook — Domain analysis architecture (other hubs)]] · [[Codul fiscal 1163-1997 (notă)]] · [[Concept — Impozit pe venit]] · [[Concept — TVA]] · [[Concept — Rezident fiscal]] · [[Concept — Parc IT]] · [[SFS]] · [[Energetică — architecture map]]
