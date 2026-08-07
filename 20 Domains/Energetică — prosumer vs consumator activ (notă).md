---
title: "Energetică — prosumer vs consumator activ (notă)"
type: domain-note
domeniu: [energetică, energie-electrică, regenerabile]
tags: [domain, analysis, energetică, prosumer, consumator-activ]
analysis_tier: law-house
status: draft
created: 2026-08-07
updated: 2026-08-07
---

# Prosumer vs active consumer — boundary note

Step 2 bridge note. Feeds the Step 7 prosumer cross-cutting layer. Hub: [[MOC — Piața de energie electrică]] · Concepts: [[Concept — Consumator activ]] · [[Concept — Facturare netă]] · [[Concept — Comunitate de energie a cetățenilor]] · [[Concept — Producător eligibil]]

> [!abstract] One-line rule
> **Consumator activ** = L164 market-participation status. **Prosumer (facturare netă)** = L10 support/settlement overlay. Same physical rooftop can be one, both, or move between them — the licence, balancing and revenue rules are not the same.

---

## 1. Side-by-side

| | **Consumator activ** (L164) | **Prosumer / facturare netă** (L10) | **Producător eligibil** (L10) |
|---|---|---|---|
| Legal home | [[Legea 164-2025 — energia electrica (notă)\|L164]] arts. 122–123 | [[Legea 10-2016 — surse regenerabile (notă)\|L10]] + [[Concept — Facturare netă]] | [[Concept — Producător eligibil]] |
| Purpose filter | Activities **not** main commercial/professional activity | Self-consumption + surplus injection under quota | Support-scheme status (fixed tariff / auction) |
| Revenue | Market sale, bilaterals, flexibility, energy sharing | Monetary netting vs consumption (net billing) | Guaranteed offtake / support price via [[Concept — Furnizor central de energie electrică\|FCEE]] (until CfD transition) |
| Licence | Usually none for plain active-consumer acts; storage ≥1 MW / supply / aggregation still bite | No eligible-producer licence track; connection + supply annex | Generation licence if ≥5 MW; support status separate |
| Balancing | Must be PRE or delegate (art. 122(3)) | Typically inside **supplier** PRE perimeter (HANRE 853 / market rules) | Often FCEE balancing group or own PRE |
| Caps | ANRE max capacity **by technology** for active consumers (art. 122(5)) | Government aggregate quota + individual ceilings (HG 401 → HG 599) | Government support quotas / auction volumes |
| Ops acts | HANRE 311 connection · supply reg · future sharing/CEC regs | HANRE 833 Anexa 5 · HANRE 169 · HANRE 311 | HANRE 375 · HANRE 283 FCEE lane · HG 26 |

---

## 2. How L164 forces the distinction

Art. 122(6): an active consumer **may become** a RES prosumer under L10 art. 39¹ and then **may not** engage in activities outside that L10 regime.

Practical reading:

1. Entering net billing **narrows** the activity set — you trade the broader active-consumer toolbox for the L10 settlement overlay.
2. Conversely, an active consumer who sells on bilaterals, joins flexibility markets, or shares energy under art. 123 is **not** automatically a prosumer.
3. Energy sharing (art. 123) is **not supply** and needs **no supply licence** — distinct from both net billing and eligible-producer offtake.

CEC ([[Concept — Comunitate de energie a cetățenilor]]) is a third box: collective vehicle with ANRE register + non-profit-primary filter; members may still be active consumers or prosumers individually.

---

## 3. Decision tree (advice order)

```
Is the client seeking L10 net-billing credit against its bill?
  ├─ YES → Prosumer track: check HG quota/ceiling → connection (311) → supplier annex (169/833)
  │         Warn: art. 122(6) lock-in — other active-consumer activities constrained
  └─ NO  → Is the client mainly self-consuming / storing / sharing / selling without support?
            ├─ YES → Active-consumer track: art. 122 rights + BRP + ANRE capacity cap
            │         Storage ≥1 MW? → [[Concept — Stocare a energiei]] licence
            └─ Seeking support tariff / auction offtake?
                  └─ YES → Eligible-producer track (not prosumer) → FCEE / CfD
```

---

## 4. Common misfiles

| Mistake | Why it fails |
|---|---|
| Calling every rooftop PV owner a “prosumer” | Without L10 net-billing enrolment they may only be an active consumer (or neither) |
| Advising eligible-producer support for net-billing clients | Different quota, different offtake, different balancing |
| Ignoring BRP when “only self-consuming” | Art. 122(3) still assigns imbalance responsibility |
| Using HG 401 ceilings after the 2030 package | Check [[HG 599-2025 — limite capacitate regenerabile 2030 (notă)\|HG 599/2025]] envelope for the connection date |
| Treating CEC registration as optional branding | Without ANRE register entry, CEC rights do not attach |

---

## 5. Status & Step 7 handoff

This note closes the Step 2 **boundary** question. Step 7 should expand into a full **Prosumers & active consumers** layer (procedures, annex walkthroughs, worked examples) without re-deriving the taxonomy.

## Related
[[Concept — Consumator activ]] · [[Concept — Facturare netă]] · [[Concept — Producător eligibil]] · [[Concept — Furnizor central de energie electrică]] · [[Concept — Comunitate de energie a cetățenilor]] · [[Concept — Contract la prețuri dinamice]] · [[Energetică — segmente piață electricitate (notă)]] · [[Roadmap — Energy analysis architecture]] · [[MOC — Piața de energie electrică]]
