---
title: "Societăți & guvernanță — sinteza"
type: domain-note
domeniu: [societăți, guvernanță]
tags: [domain, analysis, societăți]
status: draft
created: 2026-07-23
---

# Companies & corporate governance — synthesis

The reasoning layer for company law. Act inventory: [[MOC — Societăți & Guvernanță corporativă]].

> [!info] Sources and currency
> Figures below were verified in **July 2026**. Company-law thresholds move; re-check before advising. Key verification points are flagged inline.

---

## 1. The architecture

Moldovan company law is **three-layered**, and the layers are not always consistent with each other:

| Layer | Instrument | Role |
|---|---|---|
| General | **Codul civil nr. 1107/2002**, Cartea I — legal persons | Capacity, organs, representation, nullity, reorganisation, liquidation. The default rules. |
| Special | **Legea nr. 1134/1997** (SA) · **Legea nr. 135/2007** (SRL) | Form-specific rules. Prevail over the Civil Code where they differ. |
| Procedural | **Legea nr. 220/2007** — state registration | How a company comes into and goes out of legal existence; what the register does. |

Sitting across all three: **Legea nr. 845/1992** on entrepreneurship and enterprises — the Soviet-era survivor, still formally in force, largely obsolete, and slated for **complete repeal** by a new entrepreneurship law (Government project 345/MDED/2025) with a **two-year transition** after publication. Treat 845/1992 as a legacy layer: check whether the provision you need has already been superseded by the Civil Code.

The direction of the whole system is **EU company-law alignment** — L1134/1997 has been amended to transpose **Directive (EU) 2017/1132** (codified company law) and **Directive 2007/36/EC** (shareholder rights).

## 2. SRL vs SA — choosing the form

This is the first question in almost every corporate mandate, and it is not close for most clients.

| | **SRL** (Legea 135/2007) | **SA** (Legea 1134/1997) |
|---|---|---|
| Minimum share capital | **None.** The old MDL 5,400 floor was abolished — founders set it freely | **MDL 600,000** (art. 38(2)) |
| Ownership unit | *parte socială* — a **claim/participation**, not a security | *acțiune* — a **security**, registered in a securities register |
| Transfer | Restricted by default: pre-emption for other members, formalities, register update | Free in principle; transfer effected through the securities registrar |
| Members | Limited number (statutory cap); closed by design | Open; can be public |
| Mandatory organs | General meeting + administrator. Board optional | General meeting + **board (consiliu)** + executive + **censor/audit** function |
| Regulator | [[ASP]] registry only | [[ASP]] **+ [[CNPF]]** — securities market oversight |
| Disclosure | Minimal | Substantial and continuous |
| Typical use | SMEs, subsidiaries, JVs, holding vehicles | Banks, insurers, listed and formerly-privatised entities, regulated utilities |

**Practical read.** The SRL is the default for anything that is not required to be an SA. The MDL 600,000 floor plus CNPF supervision plus mandatory board and audit make the SA materially more expensive to run, and the compensating benefit — transferable securities and access to public capital — is worth little in a market with a thin equity market. Clients pick SA when a regulator requires it, when a historic privatisation left them with it, or when they genuinely need share transferability.

> [!warning] The 600,000 MDL floor has teeth
> Law nr. 18/2020 gave existing SAs a compliance runway to **1 January 2024**. A company that has not brought its capital to the minimum, and has not resolved to reorganise or dissolve, can be **dissolved by court order** on the application of a shareholder or of **[[CNPF]]**. When taking on a legacy SA, check the registered capital figure before anything else.

→ [[Concept — Capital social]] · [[Concept — Acțiune vs parte socială]]

## 3. The governance triangle

Every form resolves the same three-way tension: **owners** who bear residual risk, **managers** who have information and discretion, and **creditors** who are exposed to both.

**Owners → managers: the agency problem.** The instruments are competence allocation (reserved matters for the general meeting), appointment and removal, fiduciary duties, related-party transaction control, and liability.
→ [[Concept — Adunarea generală]] · [[Concept — Administrator]] · [[Concept — Consiliul societății]]

**Majority → minority: the expropriation problem.** Qualified majorities for structural decisions, pre-emption rights, withdrawal/appraisal rights, information rights, and the ability to challenge resolutions. The **related-party transaction** regime — *tranzacții cu conflict de interese* — is the sharpest tool in the SA law and the one most worth knowing.

**Company → creditors: the asset-shielding problem.** Capital maintenance, restrictions on distributions, the obligation to act on net assets falling below share capital, directors' duties in the vicinity of insolvency, and ultimately **Legea insolvabilității nr. 149/2012**. This is the corridor through which limited liability is paid for.

## 4. Registration — how a company exists

State registration under **Legea nr. 220/2007**, administered by **[[ASP]]**, is **constitutive**: the legal person comes into being on registration, not on signature of the constitutive act.

The register does three separate jobs, and conflating them causes errors:
1. **Creates** legal personality
2. **Publicises** — third parties are protected in relying on registered data, and the company generally cannot invoke unregistered facts against a good-faith third party
3. **Controls** — a limited legality check at entry

Practical points: the **administrator's mandate is registered**, so a counterparty verifies authority against the register, not against a board minute; changes to the constitutive act and to representation take effect on registration; and registration is also the exit gate — dissolution and liquidation run through it.

Beyond registration sit the **permits and authorisations** for particular activities, which are a different question entirely and are governed by the licensing framework. → [[Drept comercial — sinteza]]

## 5. Reorganisation and the corporate toolkit
Merger (*fuziune* — by absorption or by consolidation), division (*dezmembrare* — split-up or spin-off), and transformation of form. Governed by the Civil Code with form-specific overlays, following the EU cross-border and domestic merger architecture.

**This is where energy meets company law.** Unbundling a vertically integrated utility is executed as a corporate reorganisation: spin-off of the network business, contribution of a going concern, and governance ring-fencing. The regulatory obligation is in the energy statute; the mechanics are here. → [[Concept — Unbundling]] · [[Energetică — sinteza sectorului]]

## 6. Insolvency
**Legea insolvabilității nr. 149/2012** provides the collective procedure: general insolvency leading to liquidation, and **restructuring** as the reorganisation alternative. Its governance significance is the **shift in duty** — as insolvency approaches, the interests directors must serve tilt from shareholders toward creditors, and late filing plus transactions in the suspect period expose directors personally.

For a director, the two dates that matter are the date the company became insolvent in fact and the date the filing was made. The gap between them is the liability.

→ [[Concept — Insolvabilitate]] · [[Drept comercial — sinteza]]

## 7. Beneficial ownership and AML
Registration of **beneficial owners** with [[ASP]], under the AML framework, is a live and increasingly enforced compliance duty with real consequences for banking access. Any structuring advice that stops at the legal owner is incomplete.

## 8. Open threads
- Ingest **Legea 135/2007** (SRL) and **Legea 1134/1997** (SA) — the two keystone acts; both are large enough to need manual, per-chapter ingestion ([[Convenții vault]])
- Ingest **Codul civil Cartea I** (legal persons) — per Titlu
- Ingest **Legea 220/2007** (registration) and **Legea 149/2012** (insolvency)
- Track the **new entrepreneurship law** replacing L845/1992 — repeal with a 2-year transition
- Write [[ASP]] and [[CNPF]] institutional profiles into `60 Autorități`
- Reporting duties bridge to [[Contabilitate & raportare financiară — sinteza]]

## Related
[[MOC — Societăți & Guvernanță corporativă]] · [[Drept comercial — sinteza]] · [[Fiscalitate — sinteza sistemului fiscal]] · [[Contabilitate & raportare financiară — sinteza]] · [[ASP]] · [[CNPF]]
