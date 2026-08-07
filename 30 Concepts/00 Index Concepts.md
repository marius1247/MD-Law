---
title: 00 Index Concepts
type: dashboard
tags:
- index
- concepte
- dataview
created: '2026-07-28'
updated: '2026-07-28'
---

# 🧠 Index Central: Concepte Atomice de Drept Energetic

Tablou de comandă interactiv pentru gestionarea, vizualizarea și navigarea prin toate conceptele juridice atomice definite în vault.

---

## 📊 Sumar General Concepte (Dataview)

```dataview
TABLE domain AS "Domeniu", status AS "Statut", tags AS "Tag-uri"
FROM "30 Concepts"
WHERE type = "concept"
SORT domain ASC, file.name ASC
```

## 🗂️ Concepte pe Domenii de Reglementare

### ⚡ Piața și Furnizarea de Energie

```dataview
LIST
FROM "30 Concepts"
WHERE type = "concept" AND (domain = "piata_energiei" OR domain = "energie_regenerabila")
SORT file.name ASC
```

### 🔌 Racordare, Acces și Rețele

```dataview
LIST
FROM "30 Concepts"
WHERE type = "concept" AND (domain = "racordare_acces" OR domain = "general_reglementat")
SORT file.name ASC
```

### 📊 Tarife și Economie Reglementată

```dataview
LIST
FROM "30 Concepts"
WHERE type = "concept" AND domain = "tarife"
SORT file.name ASC
```

## 🔗 Legături către Hărțile de Conținut (MOCs)

* [[Energetică — architecture map]] — inter-law + market taxonomy
* [[MOC — Piața de energie electrică]]
* [[MOC — Piața gazelor naturale]]
* [[MOC — Piața produselor petroliere]]
* [[Energetică — cărbune gap stub (notă)]]
* [[MOC — Racordare și acces la rețele]]
* [[MOC — Tarife și metodologii ANRE]]
* [[Roadmap — Energy analysis architecture]]

## Added 2026-08-07 (annex batch)
- [[Concept — Facturare netă]] — prosumer monetary netting; HG 401/2021 → HG 599/2025 envelopes
- [[Concept — Indicatori de calitate SAIDI SAIFI]] — electricity QoS continuity indices (HANRE 537/2020)
- [[Concept — Consum tehnologic gaze]] — gas TSO CTP / normative losses (HANRE 535/2019 annex)

## Added 2026-08-07 (analysis architecture Step 3 — gas)
- [[Concept — Punct virtual de tranzacționare]] — gas VTP / wholesale delivery point (HANRE 534)
- Gas hub: [[MOC — Piața gazelor naturale]] · [[Energetică — segmente piață gaze (notă)]]

## Added 2026-08-07 (analysis architecture Step 4 — petroleum / coal)
- [[Concept — Preț maxim ANRE produse petroliere]] — daily retail price cap (L461 art. 4)
- Petroleum hub: [[MOC — Piața produselor petroliere]] · [[Energetică — segmente piață petrol (notă)]]
- Coal: [[Energetică — cărbune gap stub (notă)]] — no dedicated ANRE coal market
