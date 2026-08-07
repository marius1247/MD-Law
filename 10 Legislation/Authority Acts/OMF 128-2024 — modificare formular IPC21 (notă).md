---
title: "OMF 128-2024 — modificare formular IPC21 (notă)"
type: act-note
act: "[[OMF 128-2024 — modificare formular IPC21 (text)]]"
domeniu: [fiscal, payroll]
enabling_act: "Legea 214/2024 (politica bugetar-fiscală și vamală) art. XVII(3); HG 696/2017"
eu_directives: ""
analysis_tier: law-house
status: reviewed
depth: expert
tags: [act-note, analysis, fiscal, payroll, OMF, IPC21]
created: 2026-08-07
updated: 2026-08-07
domain: fiscal
issuer: Ministerul Finanțelor
legal_status: in_vigoare
---

# OMF nr. 128/2024 — IPC21 withholding/payroll return amendments — Analysis

**Raw text:** [[OMF 128-2024 — modificare formular IPC21 (text)]] ✅ · **Parent form order:** OMF **94/2020** *(not yet ingested)* · **Tax admin:** [[SFS]] · **Hub:** [[MOC — Fiscalitate & Contabilitate]]

> [!abstract] Executive summary & commercial impact
> **Core purpose:** Amends the standardised **IPC21** declaration (income-tax withholding + mandatory health premiums + state social contributions) and its completion instruction — first reporting month **November 2024**.
> **Primary business risk:** Payroll software / returns still emitting deleted income-source codes **12** and **23**, or missing new insured-person category codes **179** / **180**.

---

## 1. Foundation

* OMF 128/31.10.2024; MO 457–458 art. 863 / 05.11.2024; IF on publication.
* Basis: HG 696/2017 (MF regulation) + **Law 214/2024** (budgetary-fiscal & customs policy) art. XVII(3).
* Amends OMF 94/2020 (Form IPC21 + instruction).

---

## 2. Substantive changes

### A. Deleted rows / codes (Annex 1 Table 1 + Annex 2 instruction)
* Remove codes **12** and **23**.
* Instruction cleanup: drop dual “SAL / SAL a)” wording → single **SAL**; drop **VMS**.
* Deleted instructional text tied to:
  * code 12 — taxable monthly income of employees of software-production economic agents under the old special annex to Law 1164-XIII / related withholding & health premiums;
  * code 23 — interest on state securities to natural persons (CF art. 90¹(3⁸) path).

> Practical read: the special software-employer IPC21 line and the state-securities interest line are no longer reported on those codes — confirm current CF / annual fiscal-policy treatment before advising substitute reporting.

### B. New insured-person classifier codes (Annex 3)
| Code | Category | Contribution rates shown in order |
|---|---|---|
| **179** | Person who received monthly allowance for **technical unemployment** under Labour Code art. 80(1)(b)/(c), paid from employer funds | 29% / 24% / 39% / 32% *(as printed — verify which column is employer/employee/base)* |
| **180** | Chernobyl-affected person who received **14 days additional leave** | **0** |

### C. First application period
Returns for **November 2024** must use the amended form.

---

## 3. Risk matrix

| Issue | Risk | Strategy |
|---|---|---|
| Parent OMF 94/2020 absent | Incomplete field-by-field map | Ingest OMF 94 for full IPC21 instruction |
| Stale payroll schemas | Rejected / corrected returns | Patch codes 12/23 out; add 179/180 |
| Technical unemployment coding | Wrong social-contribution base | Align HR events with code 179 |

---

## 4. Client checklist

- [ ] Payroll / ERP: deploy Nov-2024 IPC21 schema.
- [ ] Confirm treatment of software-sector wages and state-securities interest under **current** CF (not deleted IPC21 lines).
- [ ] HR: map technical-unemployment allowances to code 179.
- [ ] Next ingest: OMF **94/2020** parent form + Law **214/2024** fiscal-policy package if used for other 2024/2025 rate changes.

---

## 5. Connections

* [[Concept — Impozit pe venit]] · [[SFS]] · [[Codul fiscal 1163-1997 (notă)]]
* [[Legea 77-2016 — parcuri tehnologia informatiei (notă)]] *(IT Park residents still file payroll information flows — different single-tax mechanics)*
* [[MOC — Fiscalitate & Contabilitate]] · [[Fiscalitate & Contabilitate — horizon and gaps]]

---

## Sources

[[OMF 128-2024 — modificare formular IPC21 (text)]] — legis.md `145617`.
