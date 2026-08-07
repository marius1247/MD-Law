---
title: MOC — Tarife și metodologii ANRE
type: moc
domain: tarife_metodologii
domeniu:
- tarife
- metodologii
- energetică
status: draft
tags:
- moc
- tarife
- metodologii
- anre
created: '2026-07-28'
updated: '2026-08-07'
---

# 📊 Map of Content: Tarife și Metodologii ANRE

Indexul tuturor metodologiilor de calcul, aprobărilor de tarife reglementate și veniturilor de bază aprobate de Consiliul de Administrație al ANRE.

---

## 1. Sectorul Energie Electrică
* [[Concept — Tarif de transport]] · [[HANRE 626-2023 — Metodologie tarife transport EE (notă)|626/2023]] (+ [[HANRE 261-2026 — modificare Metodologie tarife transport EE (notă)|261/2026]])
* [[HANRE 64-2018 — Metodologie tarife distributie EE (notă)|64/2018]] — distribution *(annex gap)*
* [[HANRE 375-2017 — Metodologie tarife regenerabile (notă)|375/2017]] — renewables fixed tariffs *(annex gap)*
* [[HANRE 286-2018 — licentiere energie (notă)|286/2018]] — tariff/price **application** procedure *(not licensing)*
* [[Legea 45-2025 — garantiile avizelor de racordare si tolerante dezechilibre (notă)|LP45/2025]] Art. I §2 — early recognition of **national-interest TSO CAPEX** (project value) in the transport tariff (historical L107 art. 88(2); remap under L164)

## 2. Sectorul Gaze Naturale
* HANRE **535/2019** gas TSO transport methodology — parent ❌ · amending [[HANRE 329-2025 — modificare Metodologie tarife transport gaze (notă)|329/2025]] ✅ (conditional-capacity Section 7²)
* [[Concept — Capacitate condiționată]] · [[HANRE 310-2026 — modificare Codul retelelor de gaze naturale (notă)|310/2026]] product rules
* [[HANRE 443-2020 — Metodologie tarife distributie gaze (notă)|HANRE 443/2020]] gas DSO methodology — decision ✅ · **annex still missing** · amending [[HANRE 785-2025 — modificare Metodologie tarife distributie gaze 443-2020 (notă)|785/2025]] ✅ (uniform + equalization overlay, IF 1.01.2026) · applied rates [[HANRE 162-2026 — tarife uniforme distributie gaze (notă)|162/2026]] ✅ (IF 1.04.2026)

## 3. Concepte Atomice Asociate
* [[Concept — Tarif de transport]]
* [[Concept — Baza activelor reglementate]]
* [[Costul Mediu Ponderat al Capitalului]]
* [[Concept — Devieri financiare]]

## 4. Hotărâri Tarifare Aprobate (Dataview)
```dataview
TABLE type AS "Tip Act", last_amended AS "Data/Versiune"
FROM #acte_normative
WHERE contains(tags, "tarife") OR contains(tags, "metodologie")
SORT file.name DESC
```
