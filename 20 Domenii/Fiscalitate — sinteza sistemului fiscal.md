---
title: "Fiscalitate — sinteza sistemului fiscal"
type: domain-note
domeniu: [fiscal]
tags: [domain, analysis, fiscal]
status: draft
created: 2026-07-23
---

# Taxation — synthesis

The reasoning layer for tax. Act inventory: [[MOC — Fiscalitate & Contabilitate]]. Accounting side: [[Contabilitate & raportare financiară — sinteza]].

> [!warning] Rates and thresholds move every single year
> The figures below were **verified in July 2026**. The Fiscal Code is amended by the annual fiscal-policy law effective 1 January, without exception. **Never quote a rate from this note without re-checking** [SFS](https://sfs.md) or [Ministerul Finanțelor](https://mf.gov.md). Treat every number here as a starting point for verification, not as an answer.

---

## 1. The architecture

One code, one administrator, one appeal route.

- **Codul fiscal nr. 1163/1997** — the substantive law, organised by **Titluri**, each a self-contained tax
- **Legea nr. 287/2017** — accounting and financial reporting; supplies the numbers the tax system taxes
- **Codul vamal** — customs duties and import VAT/excise at the border
- **[[SFS]]** (Serviciul Fiscal de Stat) — administration, audit, collection, enforcement
- **Serviciul Vamal** — the border; **CNAS** and **CNAM** — social and health contributions, which are *not* in the Fiscal Code but behave like payroll taxes

**Watch item:** the Ministry of Finance has an active **concept for rewriting the Fiscal Code and the Customs Code**. If it lands, the Titlu structure below changes. Track it before committing to a long-term ingestion plan.

## 2. The Fiscal Code by Titlu — the ingestion map

Each Titlu is effectively a separate statute and should become **its own `— text` file** ([[Convenții vault]]): `Codul fiscal — text — Titlul N`. The Code is far too large for automated ingestion in one piece.

| Titlu | Subject | Priority |
|---|---|---|
| **I** | Dispoziții generale — definitions, principles, residence, taxpayer obligations | **High** — the interpretive key to all the rest |
| **II** | **Impozitul pe venit** — corporate and personal income tax | **Highest** |
| **III** | **TVA** — value added tax | **Highest** |
| **IV** | Accize — excise duties | Medium |
| **V** | **Administrarea fiscală** — procedure, audit, assessment, appeals, penalties | **High** — where disputes are actually won |
| **VI** | Impozitul pe bunurile imobiliare — real estate tax | Medium |
| **VI¹** | Impozitul pe avere — wealth tax on high-value residential property | Low |
| **VII** | Taxele locale | Low |
| **VIII** | Taxele pentru resursele naturale | Low |
| **IX** | Taxele rutiere — road taxes | Low |

*Verify the exact Titlu numbering and any later additions against the current consolidation at ingestion — the Code has grown by accretion and numbering includes bis/ter forms.*

## 3. The main taxes *(July 2026 — verify)*

### Corporate income tax
| Regime | Rate | Applies to |
|---|---|---|
| **Standard** | **12%** | Taxable profit of resident companies |
| Agricultural | **7%** | Farming enterprises |
| **Small business regime** | **4%** | Turnover-based; for SMEs **not registered as VAT payers** meeting statutory criteria |
| **IT Park residents** | **7% of turnover** | Single tax replacing most others — the flagship incentive |

The **4% turnover regime** is the one most often missed. For a low-margin, non-VAT-registered SME it is a genuinely different tax position, not a rounding difference — and it interacts with the VAT registration decision, so the two must be modelled together.

There is also a **reinvested-profit relief** for SMEs below a turnover ceiling, running through 2026 — verify the current conditions and whether it has been extended before relying on it.

### Dividends
**6% withholding** on distributed profit, for residents and non-residents alike. For non-residents the rate may be reduced under a **double tax treaty**, on production of a residency certificate — Moldova has a wide treaty network, so always check.

**The combined burden matters more than the headline.** MDL 100 of profit distributed to a shareholder bears 12% CIT and then 6% on the remainder — an effective ~17.3%. Compare that with extracting value as salary, where the payroll wedge is much heavier (below), or as interest or royalties. This comparison is the core of most Moldovan structuring advice.

### VAT
- **Standard: 20%**
- **Reduced: 8%** — bread and bakery, milk and dairy, **transport of natural gas**, certain agricultural products *(the list is amended almost annually)*
- **0%** on exports and assimilated supplies; exemptions without credit for specified supplies
- Registration is threshold-based, with voluntary registration available

Note the 8% rate on **natural gas transport** — a direct bridge to [[Energetică — sinteza sectorului]]: VAT treatment feeds into regulated tariff construction.

→ [[Concept — TVA]]

### Personal income tax and the payroll wedge
| | Rate | Borne by |
|---|---|---|
| **Impozit pe venit** | **12%** | Employee |
| **CNAS** — social contributions | **24%** | **Employer**, on payroll |
| **AOAM** — health insurance | **9%** | Employee |

Personal exemptions apply before the 12%. The employer-side 24% sits **on top of** gross salary, so the true cost of employment is materially above the gross figure — this is the number that drives the salary-versus-dividend comparison above, and the reason informal payment persists.

→ [[Concept — Impozit pe venit]]

### Excise
On alcohol, tobacco, fuel, and specified goods including vehicles. Rates are **specific** (per unit) far more often than ad valorem, and are indexed annually. → [[Concept — Accize]]

## 4. Residence — who is taxed on what
The **resident / non-resident** distinction determines whether Moldova taxes worldwide income or only Moldovan-source income, and it governs withholding on outbound payments. For companies, place of organisation and management; for individuals, domicile and physical presence tests. Treaty tie-breakers override the domestic test where a treaty applies.

→ [[Concept — Rezident fiscal]]

## 5. Tax procedure — where cases are actually decided
Titlul V is the most under-read part of the Code and the most useful. The sequence to know:

1. **Fiscal control** (desk or on-site) → **decision** assessing tax, penalty and late-payment interest
2. **Administrative appeal to [[SFS]]** — a mandatory first stage with a **short limitation period**
3. **Judicial review** under the **Codul administrativ nr. 116/2018** → [[MOC — Proceduri]]

Two practical points that decide outcomes more often than the substantive law:
- **Limitation periods are short and are the most common way a good case is lost.** Diarise the appeal deadline the day the decision is received.
- **Enforcement is powerful and fast** — account seizure and asset attachment. Suspension of enforcement is a separate application and does not follow automatically from filing an appeal.

## 6. How this connects
- **Accounting supplies the tax base.** Taxable profit starts from accounting profit and is adjusted. Get [[Contabilitate & raportare financiară — sinteza]] right first, or the tax analysis is built on sand.
- **Company form drives the tax outcome** — the SRL/SA choice, distribution policy, and the salary/dividend mix. → [[Societăți & guvernanță — sinteza]]
- **Fiscal claims rank in insolvency** → [[Concept — Insolvabilitate]]
- **Sector interaction with energy** — the 8% VAT on gas transport, and excise on fuel, feed into regulated tariffs → [[Concept — Tarif reglementat]]

## 7. Open threads
- Ingest **Codul fiscal per Titlu**, starting with I, II, III, V
- Ingest the **annual fiscal policy law** for the current year — the amendment vehicle
- Ingest the **Codul vamal**
- Write the [[SFS]] institutional profile in more depth; add **Serviciul Vamal**, **CNAS**, **CNAM**
- Map the **double tax treaty network** — a standing reference table would be high value
- Detail the **IT Park** regime — it is the single most consequential incentive in the system
- Track the **Fiscal Code rewrite concept** at the Ministry of Finance

## Related
[[MOC — Fiscalitate & Contabilitate]] · [[Contabilitate & raportare financiară — sinteza]] · [[Concept — Impozit pe venit]] · [[Concept — TVA]] · [[Concept — Accize]] · [[Concept — Rezident fiscal]] · [[SFS]]
