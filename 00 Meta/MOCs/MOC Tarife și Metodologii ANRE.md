---
type: moc
domain: tarife_metodologii
tags:
  - moc
  - tarife
  - metodologii
  - anre
created: 2026-07-28
---

# 📊 Map of Content: Tarife și Metodologii ANRE

Indexul tuturor metodologiilor de calcul, aprobărilor de tarife reglementate și veniturilor de bază aprobate de Consiliul de Administrație al ANRE.

---

## 1. Sectorul Energie Electrică
* [[Tarif de Transport]]
* Metodologia de determinare a tarifelor pentru serviciul de distribuție a energiei electrice
* Metodologia de calcul al prețurilor reglementate de furnizare

## 2. Sectorul Gaze Naturale
* Metodologia de calculare și aplicare a tarifelor reglementate la gazele naturale
* Hotărâri ANRE privind tarifele de ieșire/intrare în rețeaua GTS (*Vestmoldtransgaz* / *Moldovatransgaz*)

## 3. Concepte Atomice Asociate
* [[Tarif de Transport]]
* [[Baza Activelor Reglementate]]
* [[Costul Mediu Ponderat al Capitalului]]
* [[Devieri Financiare]]

## 4. Hotărâri Tarifare Aprobate (Dataview)
```dataview
TABLE type AS "Tip Act", last_amended AS "Data/Versiune"
FROM #acte_normative
WHERE contains(tags, "tarife") OR contains(tags, "metodologie")
SORT file.name DESC
```
