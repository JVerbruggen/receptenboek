---
layout: default
title: Receptenboek 2025
---

# Receptenboek 2025

Welkom bij mijn collectie van heerlijke recepten! Hier vind je een uitgebreide verzameling van gerechten die ik heb uitgeprobeerd en verzameld.

## Recepten

{% for recipe in site.data.recipes %}
- [{{ recipe.title }}]({{ recipe.url }})
{% endfor %}

## Over dit receptenboek

Dit receptenboek bevat een verzameling van mijn favoriete recepten, inclusief:

- **Hoofdgerechten**: Van eenvoudige weekdag maaltijden tot uitgebreide weekendgerechten
- **Vegetarische opties**: Heerlijke plantaardige gerechten
- **Internationale keuken**: Recepten uit verschillende culinaire tradities
- **Gezonde opties**: Caloriebewuste en voedzame maaltijden

Alle recepten bevatten gedetailleerde ingrediëntenlijsten en stap-voor-stap instructies.

---

*Laatst bijgewerkt: {{ site.time | date: "%B %d, %Y" }}*