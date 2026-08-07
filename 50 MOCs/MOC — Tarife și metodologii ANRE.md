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

## 2. Sectorul Gaze Naturale
* [[HANRE 535-2019 — Metodologie tarife transport gaze (notă)|HANRE 535/2019]] gas TSO transport methodology ✅ · [[Concept — Consum tehnologic gaze]] · amending [[HANRE 329-2025 — modificare Metodologie tarife transport gaze (notă)|329/2025]] ✅ (conditional-capacity Section 7²)
* [[HANRE 443-2020 — Metodologie tarife distributie gaze (notă)|HANRE 443/2020]] gas DSO distribution methodology ✅ · [[Concept — Tarif de distribuție]]
* [[HANRE 355-2021 — preturi reglementate furnizare gaze (notă)|HANRE 355/2021]] regulated supply / FUO prices ✅ · amend [[HANRE 540-2024 — modificare Metodologie preturi furnizare gaze (notă)|540/2024]]
* [[Concept — Capacitate condiționată]] · [[HANRE 310-2026 — modificare Codul retelelor de gaze naturale (notă)|310/2026]] product rules
* HANRE 443/2020 — still not ingested

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
