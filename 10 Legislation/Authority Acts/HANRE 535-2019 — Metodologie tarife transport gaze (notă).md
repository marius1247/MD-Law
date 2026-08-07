---
title: "HANRE 535-2019 — Metodologie tarife transport gaze (notă)"
type: act-note
act: "[[HANRE 535-2019 — Metodologie tarife transport gaze (text)]]"
domeniu: [energetică, gaze, tarife]
enabling_act: "[[Legea 108-2016 — gazele naturale (text)]]"
eu_directives: "Energy Community / EU gas tariff network codes (alignment via L108)"
analysis_tier: law-house
tags: [act-note, analysis, energetică, gaze, tarife, incomplete]
status: draft
created: 2026-08-07
updated: 2026-08-07
issuer: ANRE
legal_status: in_vigoare
last_amended: '2025-06-24'
legis_id: "149131"
---
# HANRE 535/2019 — gas transmission tariff methodology — Analysis

**Raw text:** [[HANRE 535-2019 — Metodologie tarife transport gaze (text)]] ⚠️ *decision + CTP annex; methodology body missing* · **Hub:** [[MOC — Tarife și metodologii ANRE]] · [[MOC — Energetică]] · **Parent:** [[Legea 108-2016 — gazele naturale (notă)]] · **Related:** [[Energetică — metodologii tarifare (notă)]] · [[Concept — Consum tehnologic gaze]] · [[Concept — Tarif de transport]]

> [!warning] Methodology body still missing
> Vault now holds the approving decision **and** the annex on **technological consumption & normative losses (CTP)** in the transmission network. The core tariff methodology (WACC, RAB, entry/exit allocation keys) is **still absent**. Do not price capacity products from CTP alone.

> [!abstract] Executive summary & commercial impact
> **Core purpose:** ANRE decision approving the regulated **gas transmission** tariff methodology under L108/2016 arts. 7(2) and 99(5); amended by HANRE 329/2025 (IF 24.06.2025). The CTP annex sets how planned/actual technological consumption and normative losses feed the tariff update.
> **Primary business risk:** Treating CTP formulas as a full tariff model; missing 329/2025 conditional-capacity overlay.

---

## 1. Statutory hierarchy & legal foundation

* **Enabling:** [[Legea 108-2016 — gazele naturale (text)]] arts. 7(2), 99(5).
* **Instrument:** ANRE CA decision 535/2019 (MO 44-54/14.02.2020, art. 173); MJ registration 1536/03.02.2020.
* **Amendment:** HANRE 329/20.06.2025 (MO 329-332/24.06.2025, art. 490; IF 24.06.2025).
* **Supersession note in decision:** transport-tariff parts of HANRE 678/2014 considered *caduce*.

---

## 2. What the vault currently holds

| Element | Status |
|---|---|
| Approving decision (pct. 1–2) | ✅ |
| CTP / normative losses annex | ✅ *(upload 2026-08-07)* |
| Methodology body (tariff formulas) | ❌ missing |
| HANRE 329/2025 amending act | ✅ [[HANRE 329-2025 — modificare Metodologie tarife transport gaze (notă)\|ingested]] |

### CTP annex — operative logic

* **Planned CTPₙ** = `(Vₜ × Nₚₙ) / 100`, excluding **backhaul** volumes.
* **Nₚₙ** from factual CTP/V over years **n−5 … n−1**.
* Annual update uses factual transported volumes for year n.
* If factual CTP > normative because of repair purging, add calculated purge gas **Qₚᵣ** (emptying, SCR/CR purge, air displacement formulas (3)–(8)).
* If factual CTP < normative, tariff update accepts **factual CTP**.
* OST files CTP calculations annually with activity report + schemes/supporting acts.

---

## 3. Risk matrix

| Provision | Flaw / ambiguity | Practical risk | Mitigation |
| :--- | :--- | :--- | :--- |
| **Methodology body absent** | No WACC / allocation keys | Wrong capacity price advice | Block full tariff opinions |
| **CTP only** | Efficiency incentive visible; entry/exit not | Over-reading annex | Use for loss/allowance disputes only |
| **Post-329 rules** | Conditional-capacity Section 7² live | Citing pre-amend methodology | Read [[HANRE 329-2025 — modificare Metodologie tarife transport gaze (notă)\|329/2025]] together |

---

## 4. Client action checklist

- [ ] Obtain full methodology body before any tariff model
- [ ] For loss/CTP disputes: recompute Nₚₙ window and purge adders from the annex
- [ ] Apply [[HANRE 329-2025 — modificare Metodologie tarife transport gaze (notă)|329/2025]] unit and conditional-capacity overlays
- [ ] Cross-check capacity products against [[HANRE 420-2019 — Codul retelelor de gaze naturale (notă)|gas network code]]

---

## 5. Connections in the vault

* **Parent:** [[Legea 108-2016 — gazele naturale (notă)]]
* **Amendment:** [[HANRE 329-2025 — modificare Metodologie tarife transport gaze (notă)]] · [[Concept — Capacitate condiționată]] · [[Concept — Tarif de transport]] · [[Concept — Consum tehnologic gaze]]
* **Network rules:** [[HANRE 420-2019 — Codul retelelor de gaze naturale (notă)]]
* **EE analogue:** [[HANRE 626-2023 — Metodologie tarife transport EE (notă)]]
* **Dossiers:** [[Energetică — metodologii tarifare (notă)]] · [[Status ingestie — Energetica]]

---

## Sources

[[HANRE 535-2019 — Metodologie tarife transport gaze (text)]] — legis.md doc_id `149131` · CTP annex upload `an_1_535md_0728.md`
