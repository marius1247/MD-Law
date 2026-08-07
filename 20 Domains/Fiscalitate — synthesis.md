---
title: "Fiscalitate — synthesis"
type: domain-note
domeniu: [fiscal]
tags: [domain, analysis, fiscal]
status: reviewed
created: 2026-07-23
updated: 2026-08-07
---

# Taxation — synthesis

The reasoning layer for tax. Act inventory: [[MOC — Fiscalitate & Contabilitate]]. Accounting side: [[Contabilitate & raportare financiară — synthesis]]. Horizon / reforms / gaps: [[Fiscalitate & Contabilitate — horizon and gaps]].

> [!warning] Rates and thresholds move every single year
> The figures below were **verified in July / August 2026**. The Fiscal Code is amended by the annual fiscal-policy law effective 1 January, without exception. **Never quote a rate from this note without re-checking** [SFS](https://sfs.md) or [Ministerul Finanțelor](https://mf.gov.md). Treat every number here as a starting point for verification, not as an answer.

---

## 1. The architecture

One code, one administrator, one appeal route.

- **Codul fiscal nr. 1163/1997** — the substantive law, organised by **Titluri**, each a self-contained tax → [[Codul fiscal 1163-1997 (notă)]] ✅ ingested (Titluri I–X)
- **Legea nr. 287/2017** — accounting and financial reporting; supplies the numbers the tax system taxes → [[Legea 287-2017 — contabilitate (notă)]] ✅
- **Codul vamal nr. 95/2021** — customs duties and import VAT/excise at the border → [[Codul vamal 95-2021 (notă)]] ✅
- **[[SFS]]** (Serviciul Fiscal de Stat) — administration, audit, collection, enforcement
- **Serviciul Vamal** — the border; **CNAS** and **[[CNAM]]** — social and health contributions, which are *not* in the Fiscal Code but behave like payroll taxes → [[Legea 489-1999 — sistemul public de asigurari sociale (notă)|L489]] · [[Legea 1593-2002 — prime asigurare medicala obligatorie (notă)|L1593]]

**Watch item:** MF has a long-running **concept for rewriting the Fiscal Code and the Customs Code**, and a live **2027 fiscal-policy draft** (Estonian-style CIT). Neither is law. Track via [[Fiscalitate & Contabilitate — horizon and gaps]] — do not hard-wire advice to draft text.

## 2. The Fiscal Code by Titlu — the map

Each Titlu is effectively a separate statute and lives as its own `— text` file. All Titluri I–X are in the vault.

| Titlu | Subject | Priority |
|---|---|---|
| **I** | Dispoziții generale — definitions, principles, residence, taxpayer obligations | **High** — the interpretive key |
| **II** | **Impozitul pe venit** — corporate and personal income tax | **Highest** |
| **III** | **TVA** — value added tax | **Highest** |
| **IV** | Accize — excise duties | Medium |
| **V** | **Administrarea fiscală** — procedure, audit, assessment, appeals, penalties | **High** — where disputes are won |
| **VI** | Impozitul pe bunurile imobiliare | Medium |
| **VI¹** | Impozitul pe avere | Low |
| **VII** | Taxele locale | Low |
| **VIII** | Taxele pentru resursele naturale | Low |
| **IX** | Taxele rutiere | Low |
| **X** | Other regimes, including IT Park single tax | High when status applies |

## 3. The main taxes *(July / Aug 2026 — verify)*

### Corporate income tax
| Regime | Rate | Applies to |
|---|---|---|
| **Standard** | **12%** | Taxable profit of resident companies |
| Agricultural | **7%** | Farming enterprises |
| **Small business regime** | **4%** | Turnover-based; for SMEs **not registered as VAT payers** meeting statutory criteria |
| **IT Park residents** | **7% of turnover** | Single tax replacing most others — the flagship incentive |

The **4% turnover regime** is the one most often missed. For a low-margin, non-VAT-registered SME it is a genuinely different tax position — and it interacts with the VAT registration decision (now at **1.7 MDL m** after [[Legea 41-2026 — suport desfasurare afaceri (notă)|L41/2026]]), so the two must be modelled together.

There is also **deferred CIT under art. 87(11)** for qualifying SMEs through **2026** — cash tax until distribution. See §4 below and [[Concept — Impozit pe venit]].

### Dividends
**6% withholding** on distributed profit, for residents and non-residents alike. For non-residents the rate may be reduced under a **double tax treaty**, on production of a residency certificate.

**The combined burden matters more than the headline.** MDL 100 of profit distributed to a shareholder bears 12% CIT and then 6% on the remainder — an effective ~17.3%. Compare that with salary (payroll wedge below), interest or royalties.

### VAT
- **Standard: 20%**
- **Reduced: 8%** — bread and bakery, milk and dairy, **transport of natural gas**, certain agricultural products *(list amended almost annually)*
- **0%** on exports and assimilated supplies; exemptions without credit for specified supplies
- Registration threshold **1.7 MDL m** after [[Legea 41-2026 — suport desfasurare afaceri (notă)|L41/2026 Art. I]] (was 1.5), with voluntary registration available

Note the 8% rate on **natural gas transport** and the domestic **energy reverse charge (art. 101⁷)** — direct bridges to [[Energetică — synthesis]].

**Refund procedure:** [[HG 93-2013 — restituirea TVA (notă)|HG 93/2013]] (consolidated with [[HG 829-2025 — modificare acte fiscale vamale audit (notă)|HG 829/2025]], IF 1 Jan 2026) — chapters XI²/XI³ for art. 101(5¹) reverse-charge excess and the Dec-2025 gas transitional path; general clock **45 days**, staged payout on the art. 4(20⁹) limb.

→ [[Concept — TVA]]

### Personal income tax and the payroll wedge
| | Rate | Borne by |
|---|---|---|
| **Impozit pe venit** | **12%** | Employee |
| **CNAS** — social contributions | **24%** | **Employer**, on payroll |
| **AOAM** — health insurance | **~9%** | Employee · [[Concept — Prima AOAM]] · [[Legea 1593-2002 — prime asigurare medicala obligatorie (notă)|L1593/2002]] |

Personal exemptions apply before the 12%. The employer-side 24% sits **on top of** gross salary.

→ [[Concept — Impozit pe venit]] · [[Concept — Prima AOAM]]

### Excise
On alcohol, tobacco, fuel, and specified goods including vehicles. Rates are **specific** (per unit) far more often than ad valorem, and are indexed annually. → [[Concept — Accize]]

---

## 4. 2026 live changes (must know)

Verified against MF summaries and the vault CF consolidation (Aug 2026). Full table and commercial bite: [[Fiscalitate & Contabilitate — horizon and gaps]].

| Theme | What changed | Anchor |
|---|---|---|
| **VAT registration threshold** | Raised to **1.7 MDL m** ([[Legea 41-2026 — suport desfasurare afaceri (notă)\|L41/2026]]; was 1.5) | Titlul III art. 54¹ / 112 area |
| **Energy reverse charge** | Domestic EE/gas to **comerciant**; also imports of energy + network services | Titlul III art. **101⁷** — declare comerciant status to [[SFS]] |
| **VAT refund regulation update** | XI²/XI³ chapters + 45-day / staged-payout clocks; stock-option annex under HG 693/2018 | [[HG 829-2025 — modificare acte fiscale vamale audit (notă)\|HG 829/2025]] → [[HG 93-2013 — restituirea TVA (notă)\|HG 93/2013]] |
| **e-Factura deduction clamp removed** | Art. **102(18) abrogated** 01.01.2026 | Titlul III art. 102 — paper/other formats no longer automatic denial vs mandatory e-Factura users |
| **Independent entrepreneurs** | Single tax **15% / 35%** above 1.2 MDL m; no books; SFS computes from ECC + bank data | Titlul II cap. **10⁴** — labour recharacterisation risk if art. 24(11¹) tests fail |
| **Deferred CIT (art. 87(11))** | Extended through **2026**; ≤249 staff + ≤100 MDL m turnover/assets (trade exclusions) | Titlul II art. 87 — model before year-end |
| **Taxi payroll special regime** | Ends **1 July 2026** | Titlul II / payroll returns — back to ordinary salary taxation |

Also live on the accounting side (separate from tax rates): [[Legea 86-2026 — modificare Legea contabilitatii (notă)|L86/2026]] thresholds **IF 1 Jan 2027** — model now → [[Contabilitate & raportare financiară — synthesis]].

---

## 5. 2027 pipeline

Point of truth: [[Fiscalitate & Contabilitate — horizon and gaps#3. Horizon — advancing / about to be implemented]].

- **Politica fiscală 2027 draft** (Government project to Parliament): Estonian-style corporate tax on **distributed profit**; proposed indicative rates **15%** companies / **7%+15%** progressive PIT; cleanup of exemptions. **Not yet law — do not advise as live.** When enacted, ingest as annual fiscal-policy act and rewrite Titlul II concepts.
- B2G e-invoicing draft (IF = EU accession); governmental digital notices from 1 Jan 2027; long-running full CF/Customs rewrite concept; ongoing SNC updates.

## 6. Residence — who is taxed on what
The **resident / non-resident** distinction determines whether Moldova taxes worldwide income or only Moldovan-source income, and it governs withholding on outbound payments. For companies, place of organisation and management; for individuals, domicile and physical presence tests. Treaty tie-breakers override the domestic test where a treaty applies.

→ [[Concept — Rezident fiscal]]

## 7. Tax procedure — where cases are actually decided
Titlul V is the most under-read part of the Code and the most useful. The sequence to know:

1. **Fiscal control** (desk or on-site) → **decision** assessing tax, penalty and late-payment interest
2. **Administrative appeal to [[SFS]]** — a mandatory first stage with a **short limitation period**
3. **Judicial review** under the **Codul administrativ nr. 116/2018** → [[MOC — Proceduri]]

Two practical points that decide outcomes more often than the substantive law:
- **Limitation periods are short and are the most common way a good case is lost.** Diarise the appeal deadline the day the decision is received.
- **Enforcement is powerful and fast** — account seizure and asset attachment. Suspension of enforcement is a separate application and does not follow automatically from filing an appeal.

## 8. How this connects
- **Accounting supplies the tax base.** Taxable profit starts from accounting profit and is adjusted. Get [[Contabilitate & raportare financiară — synthesis]] right first.
- **Company form drives the tax outcome** — SRL/SA choice, distribution policy, salary/dividend mix. → [[Societăți & guvernanță — synthesis]]
- **Fiscal claims rank in insolvency** → [[Concept — Insolvabilitate]]
- **Sector interaction with energy** — 8% VAT on gas transport, reverse charge art. 101⁷, connection-asset deduction, excise on fuel → [[Energetică — synthesis]] · [[Concept — Tarif reglementat]]

## 9. Open threads

**Ingested (do not re-list as missing):** Codul fiscal Titluri I–X · Codul vamal · L287 + L86.

**Still open** (from [[Fiscalitate & Contabilitate — horizon and gaps|horizon gaps]]):
- Ingest the **annual fiscal-policy law** for the current year (and 2027 package when enacted)
- Map the **double tax treaty** network — standing reference table
- IT Park admission law ✅ [[Legea 77-2016 — parcuri tehnologia informatiei (notă)|L77/2016]] · [[Concept — Parc IT]] — still need HG resident-registration regulation
- Map **individual SNC texts** (gateway [[OMF 118-2013 — Standardele Nationale de Contabilitate (notă)|OMF 118/2013]] ✅); Serviciul Vamal / CNAS profiles; deepen [[CNAM]]; CSPA authority note under [[Legea 271-2017 — auditul situatiilor financiare (notă)|L271]] ✅
- Track the **2027 Estonian-style draft** and the longer CF/Customs rewrite concept — contingency only until enacted
- Dispute workflow note; accounting ↔ tax bridge table; energy × tax dossier

## Related
[[MOC — Fiscalitate & Contabilitate]] · [[Fiscalitate & Contabilitate — horizon and gaps]] · [[Contabilitate & raportare financiară — synthesis]] · [[Codul fiscal 1163-1997 (notă)]] · [[Concept — Impozit pe venit]] · [[Concept — TVA]] · [[Concept — Accize]] · [[Concept — Rezident fiscal]] · [[SFS]]
