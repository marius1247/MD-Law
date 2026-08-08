---
title: "MOC — Impozit pe venit"
type: moc
domeniu: [fiscal, impozit-pe-venit]
tags: [moc, index, fiscal, impozit-pe-venit]
status: draft
created: 2026-08-08
updated: 2026-08-08
---

# MOC — Impozit pe venit

Regulation-oriented map of Moldova’s **income-tax regimes**: bases, actors, filings, and the acts that bind them — corporate, personal, withholding, and status-dependent single taxes.

Architecture spine: [[Fiscalitate & Contabilitate — architecture map]] · Master inventory: [[MOC — Fiscalitate & Contabilitate]] · Narrative: [[Fiscalitate — synthesis]] · Horizon: [[Fiscalitate & Contabilitate — horizon and gaps]] · Atomic doctrine: [[Concept — Impozit pe venit]]

> [!danger] Rates move every 1 January — and the 2027 draft is NOT law
> Figures below are **July / August 2026 orientation**. Re-verify against the CF consolidation and the annual fiscal-policy law before use. The Government **politica fiscală 2027** Estonian-style distributed-profit CIT is a **project only**.

---

## 1. Governing stack (how the acts talk)

| Tier | Act | Role for income tax |
|---|---|---|
| Code — general | [[Codul fiscal 1163-1997 — text — Titlul I\|CF Titlul I]] | Definitions, residence, taxpayer duties, treaty primacy (art. 4) |
| Code — income | **[[Codul fiscal 1163-1997 — text — Titlul II\|CF Titlul II]]** | Taxpayers, object, rates, deductions, regimes, withholding, non-residents |
| Code — IT Park tax | [[Codul fiscal 1163-1997 — text — Titlul X\|CF Titlul X]] | Single-tax mechanics for eligible residents |
| Annual amendment | [[Legea 318-2025 — modificare acte fiscale (notă)\|L318/2025]] (+ successors) | Rate / threshold / exemption rewrite each year |
| Business-support omnibus | [[Legea 41-2026 — suport desfasurare afaceri (notă)\|L41/2026]] | VAT threshold **1.7 MDL m** — kills/keeps the 4% SME gate |
| IT Park status | [[Legea 77-2016 — parcuri tehnologia informatiei (notă)\|L77]] · [[Legea 125-2024 — modificare parc IT si tranzitii vamale (notă)\|LP125]] | Admission / activities / withdrawal — status is not in CF alone |
| Accounting base | [[Legea 287-2017 — contabilitate (notă)\|L287]] · [[Legea 86-2026 — modificare Legea contabilitatii (notă)\|L86]] | Book profit → tax adjustments; size tiers (L86 IF 1 Jan 2027) |
| Payroll bridges | [[Legea 489-1999 — sistemul public de asigurari sociale (notă)\|L489]] · [[Legea 1593-2002 — prime asigurare medicala obligatorie (notă)\|L1593]] | CNAS 24% + AOAM ~9% sit beside PIT withholding |
| Administrator | [[SFS]] | Assessment, control, contestation, comerciant/IT interfaces |
| Procedure out | [[Codul fiscal 1163-1997 — text — Titlul V\|CF Titlul V]] → [[Codul administrativ 116-2018 (notă)\|Codul administrativ]] | Dispute ladder |

Horizontal logic: **Titlul II computes the tax; Titlul I defines who is resident; L287 supplies the book starting point; L77/Titlul X displace the ordinary regime when status applies; Titlul III VAT registration gates the 4% SME track; Titlul V decides disputes.** Full bridge table: [[Fiscalitate & Contabilitate — architecture map]] §1.2.

---

## 2. Regimes / segments (regulatory view)

| Regime | Base | Who it fits | Governing ops rules | Status in analysis |
|---|---|---|---|---|
| **Standard CIT** | Taxable profit | Resident companies (default) | Titlul II arts. 12–15, 18, 20, 24… | Concept ✅ · brief ⏳ Step 2 |
| **Agricultural** | Taxable profit | Farming enterprises | Titlul II rate schedule | Concept ✅ (rate row) · brief ⏳ |
| **SME turnover 4%** | Turnover / deliveries | Qualifying SMEs **not VAT-registered** | Titlul II special regime + Titlul III threshold | Concept ✅ · **model with VAT** · brief ⏳ |
| **Deferred CIT art. 87(11)** | Same computation; **payment** deferred to distribution | ≤249 staff + ≤100 MDL m turnover/assets (trade exclusions) through **2026** | Titlul II art. 87(11) | Concept ✅ · **sunset risk** · brief ⏳ |
| **IT Park single tax** | Turnover **7%** | L77 residents | Titlul X + [[Concept — Parc IT]] | Concept ✅ · HG registration still P1 gap |
| **Independent entrepreneurs** | Single tax **15% / 35%** above 1.2 MDL m | Cap. 10⁴; no books; SFS from ECC + bank | Titlul II cap. 10⁴ · art. 24(11¹) labour tests | Concept ✅ · recharacterisation risk |
| **PIT employment** | Taxable employment income | Employees; withholding agents | Titlul II Cap. 15 | Partial — payroll hub Step 5 |
| **Dividend WHT** | Distributed profit | Residents & non-residents (treaty relief) | Titlul II WHT rules · CF art. 4 DTT | Concept ✅ · DTT texts P1 gap |
| **Other WHT** | Interest, royalties, services… | Payors as withholding agents | Titlul II | Thin — deepen Step 2 |
| **Non-resident / PE** | Moldovan-source income | Non-residents; PE threshold | Titlul II non-resident chapter · [[Concept — Rezident fiscal]] | Partial |

Economic spine for owner-managers: choose a **regime gate** → compute / withhold → distribute or pay salary → face payroll wedge or WHT. Structuring matrix: [[Concept — Impozit pe venit]].

---

## 3. Actors

| Actor | Role | Primary source |
|---|---|---|
| **Resident legal person** | Worldwide / MD income per Titlul II; keeps books under L287 | Titlul I–II · L287 |
| **Non-resident / PE** | Source taxation; treaty tie-breakers | Titlul I art. 4 · Titlul II · [[Concept — Rezident fiscal]] |
| **Individual resident** | PIT on taxable income; personal exemptions | Titlul II |
| **Independent entrepreneur** | Cap. 10⁴ single tax; often no full books | Titlul II cap. 10⁴ |
| **Withholding agent** | Salary, dividends, other WHT remittances | Titlul II Cap. 15 / WHT chapters |
| **IT Park resident** | Single-tax payer if status holds | L77 · Titlul X · [[Concept — Parc IT]] |
| **[[SFS]]** | Registration, assessment, control, appeal, guidance | Titlul V · authority note |
| **CNAS / [[CNAM]]** | Social / health contributions beside PIT | L489 · L1593 · [[Concept — Prima AOAM]] |
| **Ministry of Finance** | Policy; SNC; forms (OMF) | L287 · OMF layer |
| Shareholders / associates | Recipients of dividends; treaty certificates | Company law + Titlul II WHT |

---

## 4. Filings / registrations / certificates

| Gate | What it does | Notes |
|---|---|---|
| Tax identification / registration | Opens taxpayer file with SFS | Titlul V registration cluster |
| **VAT registration** | Crosses or stays under threshold — **controls 4% SME eligibility** | Threshold **1.7 MDL m** after L41/2026 · [[Concept — TVA]] |
| **IT Park admission** | Unlocks Titlul X single tax | L77 procedure; resident-registration **HG still P1 gap** |
| Income-tax return / payments | Annual / instalment compliance | Titlul II + Titlul V return rules |
| Withholding returns / remittances | Salary and passive-income WHT | Cap. 15; IPC21 payroll form bridge (OMF 128 ✅ / parent OMF 94 ❌) |
| Art. 87(11) eligibility tracking | Defers CIT cash until distribution | Model before **2026** year-end |
| Residency certificate (inbound) | Treaty WHT relief | CF art. 4 · DTT texts still thin |
| Book-to-tax reconciliation | Evidence pack for control | First document inspectors request |

> [!warning] Four gates — do not conflate
> **CIT regime election ≠ VAT registration ≠ IT Park status ≠ L287 size category.** L86 reclassification in 2027 changes reporting/audit burden, **not** the CIT rate.

---

## 5. Accounting & company-law layer (feeds the tax but is not a “regime”)

- Financial statements & size tiers — [[Contabilitate & raportare financiară — synthesis]] · [[Concept — Situații financiare]] · L86 IF 1 Jan 2027
- Statutory audit pull — [[Legea 271-2017 — auditul situatiilor financiare (notă)|L271]] · [[Concept — Audit statutar]]
- Distributable profit / net-assets trigger — [[Societăți & guvernanță — synthesis]] · [[Concept — Capital social]] · [[Concept — Adunarea generală]]
- Book → tax adjustments — non-deductibles, fiscal depreciation, provisions, TP, art. 87(11) timing → dedicated bridge note in Step 10

---

## 6. Incentives, energy bridges, crisis (out of pure Titlul II)

| Theme | Acts / concepts | Hub later |
|---|---|---|
| IT Park single tax | L77 · Titlul X · [[Concept — Parc IT]] | Step 8 special regimes |
| Art. 87(11) deferral | Titlul II art. 87(11) through 2026 | Step 2 briefs · Step 8 |
| Connection-asset gifts (energy) | Titlul II art. 24 + [[Legea 164-2025 — energia electrica (notă)\|L164]] | Step 10 energy×tax |
| ESOP / stock-option valuation | [[HG 829-2025 — modificare acte fiscale vamale audit (notă)\|HG 829]] annex | Step 8 |
| **2027 Estonian-style draft** | MF project — **not law** | Step 8 gap stub |
| Payroll wedge comparison | L489 · L1593 · [[Concept — Prima AOAM]] | Step 5 |

---

## 7. Risk matrix (income-tax file)

| Risk | Why it bites | Mitigant in vault |
|---|---|---|
| Quoting stale rates | Annual 1 Jan rewrite | Horizon + verification month on every figure |
| Advising 2027 draft as live | Draft ≠ law | Architecture §1.3 · this MOC danger callout |
| 4% SME + VAT sequenced wrong | VAT registration kills turnover regime | Model jointly with [[Concept — TVA]] |
| Missing contestation deadline | Short Titlul V clock | [[SFS]] · Step 6 dispute hub |
| Ignoring book-to-tax bridge | Control starts with reconciliation | [[Concept — Impozit pe venit]] · Step 10 bridge note |
| IT Park advice from Titlul X alone | Status lives in L77 | [[Concept — Parc IT]] |
| Labour recharacterisation of “independent” | Art. 24(11¹) tests | Cap. 10⁴ briefing in Step 2 |
| Art. 87(11) assumed perpetual | Sunset end-2026 unless extended | Horizon watch |

---

## 8. Open threads (Step 1 → Step 2)

- [ ] Regime briefs note ([[Fiscalitate — regimuri impozit pe venit (notă)]])
- [ ] Harden concepts: deferred CIT · SME 4% · withholding agent · PE
- [ ] Salary vs dividend vs turnover **boundary note**
- [ ] Ingest priority DTT texts (RO, UA corridors, NL, DE, US if used)
- [ ] IT Park resident-registration HG (P1)
- [ ] Do **not** open [[MOC — TVA]] until Step 2 is navigable

## Related
[[Fiscalitate & Contabilitate — architecture map]] · [[Roadmap — Fiscalitate & Contabilitate analysis architecture]] · [[MOC — Fiscalitate & Contabilitate]] · [[Fiscalitate — synthesis]] · [[Fiscalitate & Contabilitate — horizon and gaps]] · [[Concept — Impozit pe venit]] · [[Concept — Rezident fiscal]] · [[Concept — Parc IT]] · [[Concept — TVA]] · [[Concept — Situații financiare]] · [[Codul fiscal 1163-1997 (notă)]] · [[SFS]] · [[Contabilitate & raportare financiară — synthesis]]
