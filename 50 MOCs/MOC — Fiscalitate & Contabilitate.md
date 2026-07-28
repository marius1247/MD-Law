---
title: "MOC — Fiscalitate & Contabilitate"
type: moc
domeniu: fiscal
tags: [moc, index, fiscal]
created: 2026-07-22
updated: 2026-07-23
status: draft
---

# MOC — Fiscalitate & Contabilitate

Domain hub for **taxation and accounting** — deliberately paired, because accounting supplies the base that tax is levied on.

> [!tip] Start here
> **[[Fiscalitate — sinteza sistemului fiscal]]** — the tax system: architecture, rates, procedure.
> **[[Contabilitate & raportare financiară — sinteza]]** — the accounting regime and the 2027 threshold reset.

> [!warning] Everything numeric here is time-stamped
> Figures verified **July 2026**. The Fiscal Code is amended by the annual fiscal-policy law effective 1 January, every year. Re-verify at [SFS](https://sfs.md) / [Ministerul Finanțelor](https://mf.gov.md) before use.

## Analysis layer
- **[[Fiscalitate — sinteza sistemului fiscal]]** · **[[Contabilitate & raportare financiară — sinteza]]**
- Concepts: [[Concept — Impozit pe venit]] · [[Concept — TVA]] · [[Concept — Accize]] · [[Concept — Rezident fiscal]] · [[Concept — Situații financiare]]

## Headline rates *(July 2026)*
| Tax | Rate |
|---|---|
| Corporate income tax | **12%** (agriculture 7%; SME turnover regime **4%**; IT Park **7% of turnover**) |
| Dividend withholding | **6%** — treaty relief available |
| VAT | **20%** standard · **8%** reduced (incl. **natural gas transport**) · 0% exports |
| Personal income tax | **12%** |
| Social contributions (CNAS) | **24%**, employer |
| Health insurance (AOAM) | **9%**, employee |

## Primary legislation
- **Codul fiscal nr. 1163/1997** — organised by **Titluri**; ingest one file per Titlu
- **Legea contabilității și raportării financiare nr. 287/2017** — as amended by **Legea nr. 86 of 21 May 2026**
- **Codul vamal** — customs, import VAT and excise
- The **annual fiscal policy law** — the amendment vehicle

## The Fiscal Code by Titlu — ingestion map
| Titlu | Subject | Priority |
|---|---|---|
| I | Dispoziții generale — definitions, residence, taxpayer duties | **High** |
| II | **Impozitul pe venit** | **Highest** |
| III | **TVA** | **Highest** |
| IV | Accize | Medium |
| V | **Administrarea fiscală** — control, appeals, penalties | **High** |
| VI / VI¹ | Impozitul pe bunurile imobiliare / pe avere | Medium / Low |
| VII–IX | Taxe locale · resurse naturale · taxe rutiere | Low |

*Verify exact numbering and later additions at ingestion.*

## The 2027 accounting reset
**Legea nr. 86/2026** raises the entity-size thresholds from **1 January 2027**: micro ≤ MDL 8.5M assets / 17M revenue; small ≤ 95M / 190M; medium ≤ 480M / 960M. Many entities move **down** a category, cutting reporting and audit obligations. Small and medium **groups** are exempt from consolidation unless a member is a public interest entity. → [[Contabilitate & raportare financiară — sinteza]]

## Authorities
- **[[SFS]]** — Serviciul Fiscal de Stat: assessment, control, enforcement, first-instance appeal
- **Serviciul Vamal** — the border
- **Ministerul Finanțelor** — policy; approves the **SNC** accounting standards
- **CNAS** / **CNAM** — social and health contributions

## Cross-domain bridges
- **Company form and profit extraction** → [[Societăți & guvernanță — sinteza]] · [[MOC — Societăți & Guvernanță corporativă]]
- **Accounts drive distributable profit, the net-assets trigger and insolvency dating** → [[Concept — Situații financiare]]
- **Appeals run into administrative procedure** → [[MOC — Proceduri]]
- **8% VAT on gas transport and fuel excise feed regulated tariffs** → [[Concept — Tarif reglementat]] · [[Energetică — sinteza sectorului]]

## Primary legislation — now in the vault
| Act | Text | Analysis |
|---|---|---|
| [[Codul fiscal 1163-1997 (text) — Index\|Codul fiscal nr. 1163/1997]] | ✅ Titlurile I–X | [[Codul fiscal 1163-1997 (notă)]] |
| [[Legea 287-2017 — contabilitate (text)\|Legea nr. 287/2017]] | ✅ complete | [[Legea 287-2017 — contabilitate (notă)]] |
| [[Legea 86-2026 — modificare Legea contabilitatii (text)\|Legea nr. 86/2026]] | ✅ complete | [[Legea 86-2026 — modificare Legea contabilitatii (notă)]] |
| [[Codul vamal 95-2021 (text)\|Codul vamal nr. 95/2021]] | ✅ complete | [[Codul vamal 95-2021 (notă)]] |

## Still open
- Build the **double tax treaty** reference table
- Detail the **IT Park** regime — the most consequential incentive in the system
- Track the Ministry of Finance's **Fiscal Code / Customs Code rewrite concept**
- Map **SNC** — a separate normative layer below the accounting law
- Annual fiscal-policy law (the amendment vehicle) — track each 1 January
