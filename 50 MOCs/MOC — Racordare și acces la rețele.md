---
title: MOC — Racordare și acces la rețele
type: moc
domain: racordare_acces
domeniu:
- racordare
- acces
- infrastructură
status: draft
tags:
- moc
- racordare
- infrastructura
created: '2026-07-28'
updated: '2026-08-07'
---

# Map of Content: Racordare și Acces la Rețele

Centrul de comandă pentru normele privind accesul la rețelele electrice, de gaze naturale și termice (avize, contracte de racordare, delimitare de proprietate).

---

## 1. Reglementări Sector Electrice
* [[HANRE 311-2026 — racordarea la retelele electrice (notă)|HANRE 311/2026]] — **current** connection regulation (L164)
* [[Legea 45-2025 — garantiile avizelor de racordare si tolerante dezechilibre (notă)|LP45/2025]] — statutory **>200 kW guarantees**, nevalorificare tax, imbalance deadbands (L10)
* [[HG 26-2025 — PSO acces retea producatori regenerabile pret fix (notă)|HG 26/2025]] — 6-year PSO grid access for fixed-price eligible producers
* ~~[[HANRE 168-2019 — racordarea la retelele electrice (notă)|HANRE 168/2019]]~~ — abrogated; patched while live by [[HANRE 833-2023 — modificarea unor hotarari ANRE regenerabile (notă)|833/2023]]
* [[HANRE 423-2019 — Codul retelelor electrice (notă)|HANRE 423/2019]] — *Codul rețelei electrice* · substance via [[HANRE 656-2021 — modificare Codul retelelor electrice (notă)|656/2021]] (Parts I–V)

## 2. Reglementări Sector Gaze Naturale
* [[HANRE 112-2019 — racordarea la retelele de gaze (notă)|HANRE 112/2019]] — *Regulamentul privind racordarea la rețelele de gaze naturale*
* [[HANRE 420-2019 — Codul retelelor de gaze naturale (notă)|HANRE 420/2019]] — *Codul rețelelor de gaze naturale*

## 3. Concepte Atomice Asociate
* [[Concept — Loc de consum]]
* [[Concept — Punct de delimitare]]
* [[Concept — Aviz de racordare]]
* [[Concept — Capacitate rezervată]]
* [[Concept — Garanție de bună execuție a avizului de racordare]]
* [[Concept — Producător eligibil]]

## 4. Acte de Racordare și Acces (Dataview)
```dataview
TABLE domain AS "Sector", legal_status AS "Statut"
FROM #acte_normative
WHERE contains(tags, "racordare") OR contains(tags, "acces")
SORT file.name ASC
```
