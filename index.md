---
layout: default
title: Receptenboek 2025
---

<style>
.recipe-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
  gap: 1.5rem;
  margin: 2rem 0;
  max-width: 100%;
}

.recipe-card {
  border: 1px solid #e1e1e1;
  border-radius: 8px;
  overflow: hidden;
  background: white;
  transition: transform 0.2s ease, box-shadow 0.2s ease;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

.recipe-card:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 20px rgba(0,0,0,0.15);
}

.recipe-card-image {
  width: 100%;
  height: 180px;
  object-fit: cover;
  display: block;
}

.recipe-card-content {
  padding: 1rem;
}

.recipe-card h3 {
  margin-top: 0;
  margin-bottom: 0.5rem;
  color: #2c3e50;
}

.recipe-meta {
  font-size: 0.9rem;
  color: #666;
  margin-bottom: 0.5rem;
}

.recipe-tags {
  margin-top: 0.5rem;
}

.recipe-tag {
  display: inline-block;
  background: #3498db;
  color: white;
  padding: 0.2rem 0.5rem;
  border-radius: 12px;
  font-size: 0.8rem;
  margin-right: 0.5rem;
  margin-bottom: 0.3rem;
}

.search-box {
  width: 100%;
  max-width: 400px;
  padding: 0.8rem;
  border: 2px solid #e1e1e1;
  border-radius: 8px;
  font-size: 1rem;
  margin-bottom: 2rem;
}

.search-box:focus {
  outline: none;
  border-color: #3498db;
}

/* Recipe Styling */
h1 {
  margin-top: 2rem;
  color: #2c3e50;
  border-bottom: 2px solid #3498db;
  padding-bottom: 0.5rem;
}

h1:first-of-type {
  margin-top: 0;
}

table {
  width: 100%;
  border-collapse: collapse;
  margin: 1rem 0;
}

table th,
table td {
  border: 1px solid #ddd;
  padding: 0.5rem;
  text-align: left;
}

table th {
  background: #f1f1f1;
  font-weight: bold;
}

hr {
  border: none;
  border-top: 2px solid #e1e1e1;
  margin: 3rem 0;
}

.back-to-top {
  position: fixed;
  bottom: 20px;
  right: 20px;
  background: #3498db;
  color: white;
  border: none;
  border-radius: 50%;
  width: 50px;
  height: 50px;
  cursor: pointer;
  font-size: 18px;
  display: none;
  box-shadow: 0 2px 10px rgba(0,0,0,0.3);
  z-index: 1000;
}

.back-to-top:hover {
  background: #2980b9;
}

/* Override default container width for better use of screen space */
.container {
  max-width: 1400px !important;
}

/* Markdown/content images (not card thumbnails)
   — shrink to the viewport or container but do not upscale the image.
   Uses min() so the image will be at most the smaller of its container (100%)
   and the viewport width (100vw). width:auto prevents upscaling above
   the image's intrinsic size. */
img:not(.recipe-card-image) {
  display: block;
  margin: 1rem 0;
  width: auto; /* don't force a width (prevents upscaling) */
  max-width: min(100%, 100vw);
  height: auto;
}

/* Responsive grid adjustments */
@media (min-width: 1200px) {
  .recipe-grid {
    grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
    gap: 2rem;
  }
}

@media (max-width: 768px) {
  .recipe-grid {
    grid-template-columns: 1fr;
    gap: 1rem;
  }

  .recipe-card {
    margin-bottom: 1rem;
  }
}
</style>

# Receptenboek 2025

*Laatst bijgewerkt: {{ site.time | date: "%B %d, %Y" }}*

---

Welkom bij mijn collectie van heerlijke recepten! Hier vind je een uitgebreide verzameling van gerechten die ik heb uitgeprobeerd en verzameld.

{::nomarkdown}
<input type="text" class="search-box" id="recipeSearch" placeholder="🔍 Zoek recepten..." onkeyup="filterRecipes()">

<div class="recipe-grid" id="recipeGrid">
  <!-- Cards will be rendered here by JS -->
</div>

<script>
// Fetch recipes.json and render cards
async function loadRecipes() {
  try {
    const res = await fetch('/receptenboek/assets/recipes.json');
    if (!res.ok) throw new Error('Failed to load recipes.json');
    const recipes = await res.json();
    const grid = document.getElementById('recipeGrid');
    grid.innerHTML = '';

    recipes.forEach(r => {
      const card = document.createElement('div');
      card.className = 'recipe-card';

      const img = document.createElement('img');
      img.className = 'recipe-card-image';
      img.src = r.image || '/receptenboek/assets/images/placeholder.svg';
      img.alt = r.title;
      img.onerror = () => img.src = '/receptenboek/assets/images/placeholder.svg';

      const content = document.createElement('div');
      content.className = 'recipe-card-content';

      const h3 = document.createElement('h3');
      const a = document.createElement('a');
      a.href = '#' + r.slug;
      a.textContent = r.title;
      h3.appendChild(a);

      const meta = document.createElement('div');
      meta.className = 'recipe-meta';
      meta.textContent = '⏰ ' + (r.time || '—');

      const tags = document.createElement('div');
      tags.className = 'recipe-tags';
      (r.tags || []).forEach(t => {
        const span = document.createElement('span');
        span.className = 'recipe-tag';
        span.textContent = t;
        tags.appendChild(span);
      });

      content.appendChild(h3);
      content.appendChild(meta);
      content.appendChild(tags);

      card.appendChild(img);
      card.appendChild(content);
      grid.appendChild(card);
    });

  } catch (err) {
    console.error(err);
    document.getElementById('recipeGrid').textContent = 'Kan recepten niet laden.';
  }
}

loadRecipes();

// Keep the existing filterRecipes function behavior but operate on rendered cards
function filterRecipes() {
  const searchTerm = document.getElementById('recipeSearch').value.toLowerCase();
  const recipeCards = document.querySelectorAll('.recipe-card');

  recipeCards.forEach(card => {
    const title = card.querySelector('h3 a').textContent.toLowerCase();
    const tags = Array.from(card.querySelectorAll('.recipe-tag')).map(tag => tag.textContent.toLowerCase()).join(' ');
    const searchText = title + ' ' + tags;

    if (searchText.includes(searchTerm)) {
      card.style.display = 'block';
    } else {
      card.style.display = 'none';
    }
  });
}
</script>
{:/}

{::nomarkdown}
<script>
function filterRecipes() {
  const searchTerm = document.getElementById('recipeSearch').value.toLowerCase();
  const recipeCards = document.querySelectorAll('.recipe-card');

  recipeCards.forEach(card => {
    const title = card.querySelector('h3 a').textContent.toLowerCase();
    const tags = Array.from(card.querySelectorAll('.recipe-tag')).map(tag => tag.textContent.toLowerCase()).join(' ');
    const searchText = title + ' ' + tags;

    if (searchText.includes(searchTerm)) {
      card.style.display = 'block';
    } else {
      card.style.display = 'none';
    }
  });
}
</script>
{:/}

## Over dit receptenboek

Dit receptenboek bevat een verzameling van mijn favoriete recepten, inclusief:

- **Hoofdgerechten**: Van eenvoudige weekdag maaltijden tot uitgebreide weekendgerechten
- **Vegetarische opties**: Heerlijke plantaardige gerechten
- **Internationale keuken**: Recepten uit verschillende culinaire tradities
- **Gezonde opties**: Caloriebewuste en voedzame maaltijden

Alle recepten bevatten gedetailleerde ingrediëntenlijsten en stap-voor-stap instructies.

---

## 📖 Alle Recepten

# Krieltjessalade met Mediterrane kipfilet

![Krieltjessalade met Mediterrane kipfilet](/receptenboek/assets/images/krieltjessalade-met-mediterrane-kipfilet.jpg)

- Totale tijd: 20 - 25 min.
- Lekker snel, caloriebewust, familie.

## Benodigdheden
4 personen

| Ingredient | Hoeveelheid |
|------------|-------------|
| Krieltjes  | 800g        |
| Kipfilet  | 4 stuks |
| Mediterrane kruiden (kipfilet)  | oregano, tijm, rozemarijn, salie, lavasblad, peterselie, knoflookpoeder, paprikapoeder, uipoeder, kurkuma, zwarte peper |
| Rode ui | 1 |
| Komkommer | 1 |
| Italiaanse kuiden | basilicum, oregano, rozemarijn, knoflook, paprika, majoraan, salie |
| Mais in blik | 140g |
| Mini tomaten | 200g |
| Olijfolie | 2 el |
| Witte balsamicoazijn | 5 tl |
| Mayo | 6 el |
| Peper zout | naar smaak |

## 1 Krieltjes koken
- Breng ruim water met een snuf zout aan de kook in een pan voor de krieltjes.
- Was de krieltjes en halveer ze.
- Kook de krieltjes 12-14 minuten. Giet af en spoel af met koud water.
- Bewaar apart en laat afkoelen.
  - Laat de krieltjes afkoelen anders absorberen ze de mayo.

## 2 Mengen
- Snipper ondertussen de ui heel fijn
- Giet de mais af. Halveer de tomaatjes.
- Snijd de komkommer in kleine blokjes.
- Meng in een grote salade kom de mayo met de witte balsamicoazijn en de Italiaanse kruiden.

## 3 Salade maken
- Voeg de krieltjes, komkommer, tomaat, ui en mais toe aan de saladekom.
- Meng door de dressing.
- Breng op smaak met peper en zout.

## 4 Serveren
- Vershit een scheutje olijfolie in een koekenpan op middelhoog vuur. Bak de kip 2 minuten per kant.
- Verlaag het vuur en bak de kipfilet nog 4 minuten per kant, of tot de kip gaar is.
- Snijd de kip in plakken.
- Verdeel de krieltjessalade over de borden en leg de kip er bovenop

---

# Piri-piri garnalen met tomatensalsa

![Piri-piri garnalen met tomatensalsa](/receptenboek/assets/images/piri-piri-garnalen-met-tomatensalsa.jpg)

- Totale tijd: 25 - 30 min.
- Lekker snel, caloriebewust.

## Benodigdheden
4 personen

| Ingredient | Hoeveelheid |
|------------|-------------|
| Witte langgraanrijst | 300g |
| Garnalen | 320g |
| Knoflookteen | 2 stuks |
| Rode ui | 1 stuk |
| Paprika | 2 stuks |
| Pruimtomaat | 4 stuks |
| Citroen | 2 stuks |
| Verse bladpeterselie en bieslook | 20g |
| Rode pesto | 80g |
| Piri-pirikruiden | 6 tl (Chilipoeder, paprikapoeder, uienpoeder, knoflookpoeder, oregano, peterselie, komijn, peper) |
| Olijfolie | 1 el |
| Zwarte balsamicoazijn | 2 tl |
| Mayo | 4 el |
| Extra vierge olijfolie | naar smaak |
| Peper en zout | naar smaak |

## 1 Rijst koken
- Breng ruim water met een snuf zout aan de kook in een pan.
- Snijd de paprika in dunne reepjes en de tomaat in blokjes.
- Kook de rijst zoals de verpakking zegt.
- Giet daarna af, maar bewaar wat van het kookvocht en laat de rijst uitstomen.

## 2 Saus maken
- Snijf de ui in halve ringen en pers de knoflook of snijd fijn.
- Snijd de verse kruiden fijn.
- Rasp de schil van de citroen met een fijne rasp. Snijd de citroen in 4 partjes.
- Meng in een kleine kom de mayo met de knoflook, de helft van de verse kruiden en per persoon: 1/4 tl citroensap, 1/2 el water en het sap van 1 citroenpartje. Meng goed en breng op smaak met peper en zout.

## 3 Garnalen bakken
- Verhit een klein scheutje olijfolie in een koekenpan op middelhoog vuur en bak de ui en paprika 3-4 minuten.
- Voeg de garnalen en de piri-pirikruiden toe en bak 3 minuten, of tot de garnalen roze zijn.
- Meng in een saladekom de tomaat, de overige verse kruiden en extra vierge olijfolie naar smaak. Breng goed op smaak met peper en zout.

## 4 Serveren
- Meng vlak voor serveren de pesto en zwarte balsamicoazijn door de rijst. Voeg eventueel een scheutje kookvocht toe om de rijst smeuïger te maken. Breng op smaak met peper en zout.
- Verdeel de rijst over diepe borden en verdeel alles erover.
- Verdeel de salsa over de borden en besprenkel met de saus.
- Garneer met de eventuele overige citroenpartjes.





# Aubergine fatteh met krokante kikkererwten

![Aubergine fatteh met krokante kikkererwten](/receptenboek/assets/images/aubergine-fatteh-met-krokante-kikkererwten.jpg)

- Totale tijd: 25 - 30 min.
- Lekker snel, caloriebewust, veggie.

## Benodigdheden
4 personen

| Ingredient | Hoeveelheid |
|------------|-------------|
| Volkoren Libanees platbrood | 4 stuks |
| Kikkererwten | 2 pakken |
| Knoflookteen | 2 stuks |
| Tomaat | 4 stuks |
| Rode puntpaprika | 1 stuk |
| Aubergine | 2 stuks |
| Citroen | 2 stuks |
| Verse bladpeterselie | 20g |
| Tomatenblokjes | 2 pakken |
| Volle yoghurt | 200g |
| Tahin | 40g |
| Ras el hanout | genoeg |
| Olijfolie | 3 el |
| Honing | 2 el |
| Zwarte balsamicoazijn | 2 el |
| Peper en zout | naar smaak |

## 1 Groenten bakken
- Verwarm de oven voor op 200 graden.
- Snijd de aubergine in blokjes van 1 cm. Snijd de puntpaprika in dunne ringen.
- Verdeel de aubergine en puntpaprika over een bakplaat met bakpapier en besprenkel een klein scheutje olijfolie. Breng op smaak met peper en zout en schep goed om.
- Rooster 15 - 18 minuten in de oven.

## 2 Platbrood bereiden
- Snijd het platbrood in hapklare reepjes en leg op een andere bakplaat met bakpapier.
- Besprenkel met een klein scheutje olijfolie en breng op smaak met peper en zout.
- Rooster het brood, boven de groenten, 5 - 7 minuten in de oven.

## 3 Kikkererwten bakken
- Laat de kikkererwten uitlekken in een vergiet.
- Verhit een koekenpan zonder olie op middelhoog vuur. Bak de kikkererwten 8 - 9 minuten.
- Voeg de ras el hanout toe en bak nog 1 minuut. Breng op smaak met peper en zout.
- Pers de knoflook of snijd fijn. Snijd de peterselie groef en de tomaat in blokjes.

## 4 Tomatensaus maken
- Verhit een klein scheutje olijfolie in een koekenpan op middelhoog vuur. Bak de knoflook en verse tomaat 2 minuten.
- Voeg de zwarte balsamicoazijn, de honing en de tomatenblokjes uit pak toe. Laat 4 - 6 minuten pruttelen.
- Voeg de aubergine en de puntpaprika toe aan de saus en laat nog 1 minuut pruttelen.

## 5 Yoghurtsaus maken
- Snijd de helft van de citroen in partjes en pers de overige citroen uit in een kleine kom.
- Voeg de yoghurt en de tahin toe aan het citroensap.
- Breng op smaak met peper en zout en meng goed.

## 6 Serveren
- Serveer de groenten met saus op diepe borden.
- Top af met de tahin-yoghursaus en de kikkererwten.
- Garneer met de peterselie.
- Serveer met het knapperige platbrood en de citroenpartjes.




# Mujaddara met harissa, cherrytomaten en komkommeryoghurt

![Mujaddara met harissa, cherrytomaten en komkommeryoghurt](/receptenboek/assets/images/mujaddara-met-harissa-cherrytomaten-en-komkommeryoghurt.jpg)

- Totale tijd: 25 - 30 min.
- Lekker snel, caloriebewust, veggie.

## Benodigdheden
4 personen

| Ingredient | Hoeveelheid |
|------------|-------------|
| Basmatirijst | 300g |
| Linzen | 2 pakken |
| Komkommer | 1 stuk |
| Volle yoghurt | 200 g |
| Gemalen komijnzaad | genoeg |
| Gemalen kurkuma | 4 tl |
| Rode cherrytomaten | 500 g |
| Verse bladpeterselie en munt | 20 g |
| Knoflookteen | 2 stuks |
| Citroen | 1 stuk |
| Harissa | Paprikapoeder, chilipoeder, komijnpoeder, knoflookpoeder, koriander, piment gemalen, zout |
| Ui | 1 stuk |
| Uienchutney | 80 g |
| Gemalen kaneel | 3 tl |
| Olijfolie | 4 el |
| Zwarte balsamicoazijn | 2 el |
| Honing | 2 tl |
| Zoutarme groentebouillon | 1000 ml |

## 1 Voorbereiden
- Verwarm de oven voor op 200 graden.
- Bereid de bouillon in een pan. Voeg de rijst, komijn, kaneel en kurkuma toe.
- Kook de rijst zoals op de verpakking staat.
- Pers ondertussen de knoflook of snijd fijn.

## 2 Tomaten roosteren
- Verdeel de cherrytomaten over een bakplaat met bakpapier en besprenkel met olijfolie.
- Voeg de zwarte balsamicoazijn, honing, harissa, en de helft van de knoflook toe. Breng op smaak met peper en zout en schep goed om.
- Rooster 10 - 15 minuten in de oven.
- Laat ondertussen de linzen uitelekken in een vergiet en spoel af.
- Snijd de ui in halve ringen.

## 3 Ui bakken
- Verhit een scheutje olijfolie in een koekenpan op middelhoog vuur. Bak de ui 4 minuten.
- Voeg de uienchutney toe en bak 1 minuut mee. Breng op smaak met peper en zout.
- Voeg de linzen toe aan de rijst en roer goed door.
- Snijd de komkommer in kleine blokjes. Snijd de verse kruiden grof.
- Snijd de helft van de citroen in partjes en pers de andere helft uit boven een kom.

## 4 Serveren
- Voeg de komkommer, yoghurt, overige knoflook en de helft van de verse kruiden toe aan de kom met citroensap. Roer goed door en breng op smaak met peper en zout.
- Serveer de majuddara over diepe borden. Verdeel de ui, komkommeryoghurt en cherrytomaten eroverheen.
- Garneer met de overige verse kruiden.
- Serveer de citroenpartjes ernaast.





# Bulgur met harissa-portobello, knapperige kikkererwten en tomaat-komkommersalade

![Bulgur met harissa-portobello](/receptenboek/assets/images/bulgur-met-harissa-portobello.jpg)

- Totale tijd: 25 - 30 min.
- Lekker snel, caloriebewust, veggie.

## Benodigdheden

4 personen

| Ingredient | Hoeveelheid |
|------------|-------------|
| Kikkererwten | 2 pakken |
| Bulgur | 300 g |
| Midden-Oosterse kruidenmix | genoeg (komijn, koriander, paprika, knoflook, chili, laurier) |
| Mini-komkommer | 1 stuk |
| Tomaat | 2 stuks |
| Gerookt paprikapoeder | 1 tl |
| Ui | 1 stuk |
| Portobello | 4 stuks |
| Harissa | 6 g |
| Zonnebloemolie | 6 el |
| Wittewijnazijn | 2 tl |
| Extra vierge olijfolie | 4 tl |
| Mayo | 4 el |
| Water voor saus | 2 el |
| Honing | 2 tl |
| Sambal | 2 tl |
| Peper en zout | naar smaak |

## 1 Voorbereiden
- Breng ruim water aan de kook in een pan voor de bulgur.
- Kook de bulgur 10-12 minuten. Giet af en laat uitstomen.
- Voeg de Midden-Oosterse kruiden toe en breng op smaak met extra vierge olijfolie, peper en zout. Meng goed door.
- Spoel de kikkererwten af onder koud water, laat uitlekken en dep ze droog met keukenpapier.
- Verhit een koekenpan zonder olie op middelhoog vuur en bak de kikkererwten 12-14 minuten.

## 2 Kikkererwten bakken
- Voeg 1 el zonnebloemolie per persoon en het gerookte paprikapoeder toe en bak nog 2-3 minuten.
- Snijd ondertussen de ui in halve ringen. Snijd de portobello in dunne plakken.
- Verhit een tweede koekenpan zonder olie op middelhoog vuur en bak de portobello en de ui 5 minuten.
- Roer de harissa en honing door de portobello en bak 1 minuut verder. Breng op smaak met peper en zout.

## 3 Salade maken
- Snijd de komkommer en tomaat in blokjes (scan voor kooktips!).
- Meng in een kom per persoon: 1/2 tl wittewijnazijn met 1 tl extra vierge olijfolie. Voeg de tomaat en komkommer toe en meng met de dressing. Breng op smaak met peper en zout.
- Meng in een kleine kom de mayonaise met de sambal en de aangegeven hoeveelheid water voor saus.

## 4 Serveren
- Verdeel de bulgur over diepe borden.
- Verdeel de portobello, kikkererwten en tomaat-komkommersalade erover.
- Garneer met de sambalmayonaise.





# Linguine met grote garnalen

![Linguine met grote garnalen](/receptenboek/assets/images/linguine-met-grote-garnalen.jpg)

- Totale tijd: 35 - 45 min.
- Caloriebewust, familie.

## Benodigdheden
4 personen

| Ingredient | Hoeveelheid |
|------------|-------------|
| Rode puntpaprika | 2 stuk(s) |
| Knoflookteen | 4 stuk(s) |
| Ui | 2 stuk(s) |
| Tomaat | 2 stuk(s) |
| Vers basilicum | 10 gram |
| Parmigiano Reggiano DOP | 1 stuk(s) |
| Linguine | 360 gram |
| Passata | 400 gram |
| Gedroogde oregano | 1 zakje(s) |
| Harissa | 60 gram |
| Grote garnalen | 320 gram |
| Rodewijnazijn | 1 tl |
| Suiker | 1 tl |
| Olijfolie | 4 el |
| Extra vierge olijfolie | naar smaak |
| Peper en zout | naar smaak |

## 1 Snijden
- Snijd de puntpaprika in ringen. Pers de knoflook of snijd fijn en snipper de ui. Snijd de tomaat in kleine blokjes. Snijd de basilicumblaadjes in fijne reepjes.

## 2 Puntpaprika bakken
- Verhit de helft van de olijfolie in een koekenpan met deksel op middelhoog vuur. Voeg de puntpaprika toe aan de pan en bak 6 - 7 minuten. Breng op smaak met peper en zout. Haal uit de pan en bewaar apart.

## 3 Pasta koken
- Breng ondertussen ruim water aan de kook in een pan met deksel. Kook de linguine, afgedekt, 11 - 13 minuten. Giet daarna af en laat zonder deksel uitstomen.

## 4 Saus maken
- Verhit de overige olijfolie in de koekenpan van de puntpaprika. Voeg de garnalen, ui en de knoflook toe aan de pan en fruit 2 - 3 minuten. Verlaag het vuur en haal de garnalen uit de pan. Voeg de passata, tomatenblokjes, gedroogde oregano, rodewijnazijn, suiker en harissa toe aan de pan en laat, afgedekt, 6 - 8 minuten zachtjes koken. Rasp ondertussen het blokje Parmigiano Reggiano.

## 5 Pasta mengen
- Voeg de linguine en de helft van de puntpaprika toe aan de saus. Schep goed om. Breng op smaak met peper, zout en extra vierge olijfolie naar smaak.

## 6 Serveren
- Verdeel de pasta over de borden en garneer met het basilicum, de overige puntpaprika, de geraspte Parmigiano Reggiano en de grote garnalen.





# Parelcouscous met chorizo en courgette

![Parelcouscous met chorizo en courgette](/receptenboek/assets/images/parelcouscous-met-chorizo-en-courgette.jpg)

- Totale tijd: 20 - 25 min.
- Lekker snel, caloriebewust.

## Benodigdheden
4 personen

| Ingredient | Hoeveelheid |
|------------|-------------|
| Parelcouscous | 300 g |
| Ui | 4 stuks |
| Courgette | 2 stuks |
| Knoflookteen | 4 stuks |
| Chorizoblokjes | 160 g |
| Cranberrychutney | 80 g |
| Radicchio en ijsbergsla | 200 g |
| Witte kaas | 100 g |
| Zongedroogde tomaten | 60 g |
| Wittewijnazijn | 4 tl |
| Olijfolie | 1 el |
| Zoutarme groentebouillon | 520 ml |
| Peper en zout | naar smaak |

## 1 Voorbereiden
- Bereid de bouillon in een pan met deksel voor de parelcouscous (zie Tip).
- Voeg de parelcouscous toe en kook zachtjes, afgedekt, in 12 - 14 minuten droog. Roer de korrels daarna los met een vork en laat zonder deksel uitstomen.
- Snijd de ui in fijne halve ringen. Halveer de courgette in de lengte en snijd in dunne plakjes. Pers de knoflook of snijd fijn.

## 2 Bakken
- Verwarm ondertussen 1/4 el olijfolie per persoon in een hapjespan op middelhoog vuur.
- Voeg de chorizoblokjes, ui en knoflook toe en bak 3 minuten.
- Voeg de courgette toe en bak 6 - 8 minuten, of tot de courgette gaar is.
- Voeg de cranberrychutney en de parelcouscous toe aan de hapjespan en bak nog 1 minuut. Breng op smaak met peper en zout.

## 3 Salade maken
- Voeg de radicchio en ijsbergsla toe aan een saladekom.
- Breng de salade op smaak met de wittewijnazijn, peper en zout.
- Snijd de zongedroogde tomaten in reepjes.

## 4 Serveren
- Verdeel de parelcouscous met groenten en chorizoblokjes over de borden. Verdeel de salade ernaast.
- Garneer met de zongedroogde tomaten.
- Verkruimel de witte kaas erboven.





# Burger met aardappelpartjes en champignons

![Burger met aardappelpartjes en champignons](/receptenboek/assets/images/burger-met-aardappelpartjes-en-champignons.jpg)

- Totale tijd: 35 - 45 min.
- Caloriebewust

## Benodigdheden
4 personen

| Ingredient | Hoeveelheid |
|------------|-------------|
| Aardappelen | 1000 g |
| Rode ui | 2 stuks |
| Champignons | 500 g |
| Tomaat | 2 stuks |
| Mesclun | 80 g |
| Verse rozemarijn | 2 takjes |
| Half-om-half hamburger | 4 stuks |
| Extra vierge olijfolie | 2 el |
| Zonnebloemolie | 2 el |
| Honing | 4 tl |
| Mosterd | 4 tl |
| Wittewijnazijn | 2 el |
| Roomboter | 2 el |
| Peper en zout | naar smaak |

## 1 Voorbereiden
- Haal de burger alvast uit de koelkast zodat hij op kamertemperatuur kan komen. Was de aardappelen grondig en snijd in partjes. Snijd de ui in halve ringen. Ris de blaadjes van de rozemarijntakjes en snijd grof.

## 2 Aardappelen bakken
- Verhit de zonnebloemolie in een hapjespan met deksel op middelhoog vuur. Bak de aardappelpartjes met de rozemarijn, afgedekt, 20 - 25 minuten. Schep regelmatig om. Haal het deksel van de pan en breng op smaak met peper en zout. Bak nog 10 minuten, of tot de aardappelen gaar zijn. Snijd ondertussen de champignons in plakjes.

## 3 Salade maken
- Snijd de tomaat in partjes. Maak in een saladekom een dressing van de extra vierge olijfolie, wittewijnazijn, honing en mosterd. Breng op smaak met peper en zout. Voeg de tomaat en mesclun toe aan de saladekom en meng met de dressing.

## 4 Groenten bakken
- Verhit de helft van de roomboter in een koekenpan op middelhoog vuur en bak de ui en champignons 7 - 9 minuten. Breng op smaak met peper en zout.

## 5 Burger bakken
- Verhit de overige roomboter in een andere koekenpan op middelhoog vuur. Bak de burger 2 - 3 minuten per kant. Breng op smaak met peper en zout.

## 6 Serveren
- Serveer de burger met de aardappelpartjes. Serveer de gebakken groenten en de salade ernaast.





# Fusion risotto met misopaddenstoelen en paksoi

![Fusion risotto met misopaddenstoelen en paksoi](/receptenboek/assets/images/fusion-risotto-met-misopaddenstoelen-en-paksoi.jpg)

- Totale tijd: 35 - 45 min.
- Caloriebewust

## Benodigdheden
4 personen

| Ingredient | Hoeveelheid |
|------------|-------------|
| Risottorijst | 300g |
| Rode ui | 1 stuk |
| Knoflookteen | 2 stuks |
| Witte miso | 50g |
| Roomkaas | 100g |
| Paksoi | 2 stuks |
| Rode peper | 1 stuk |
| Koreaanse kruidenmix | 10g (paprika, sesamzaad, gember, peper, ui, knoflook, sojasauspoeder) |
| Geroosterde cashewnoten | 50g |
| Kastanjechampignons | 500g |
| Sesamzaad | genoeg ter garnering |
| Bosui | genoeg ter garnering |
| Roomboter | om in te bakken |
| Zoutarme groentebouillon | 1200ml |
| Zonnebloemolie | om in te bakken |
| Olijfolie | om in te bakken |
| Peper en zout | naar smaak |

## 1 Voorbereiden
- Bereid de bouillon
- Snijd de ui in halve ringen. Pers de knoflook of snijd fijn. Verwijder de zaadlijsten van de rode peper en snijd fijn.
- Snijd de champignons in plakjes. Snijd de bosui in fijne ringen en bewaar het witte en groene gedeelte apart van elkaar.
- Verwijder de steelaanzet van de paksoi en snijd zowel de stelen als het blad van de paksoi klein. Houd de stelen apart van de groene bladeren.

## 2 Risotto bereiden
- Verhit een klontje boter in een pan op middelhoog vuur.
- Bak de knoflook en het witte gedeelte van de bosui 1 minuut.
- Roer de risottorijst erdoor en bak 1 minuut.
- Voeg 1/3 van de bouillon toe en laat de rijstkorrels de bouillon langzaam opnemen. Roer regelmatig door.

## 3 Risotto afmaken
- Voeg, zodra het vocht door de risottokorrels is opgenomen, weer 1/3 van de bouillon toe en herhaal dit met de overige bouillon.
- De risotto is gaar zodra de korrel zacht is van buiten en nog een lichte bite heeft vanbinnen. Dit duurt ongeveer 25 - 30 minuten.
- Voeg eventueel extra water toe om de rijst nog verder te garen.

## 4 Champignons bakken
- Verhit een klontje roomboter in een koekenpan op middelhoog vuur.
- Bak de champignons en ui 3 minuten.
- Voeg de rode peper toe en bak 2 - 3 minuten verder.
- Haal de pan van het vuur, roer de miso erdoor en voeg toe aan een kom. Bewaar apart tot serveren.

## 5 Paksoi bakken
- Verhit een klein scheutje zonnebloemolie in dezelfde koekenpan op middelhoog vuur.
- Bak de paksoistelen 1 - 2 minuten.
- Voeg de paksoibladeren toe en bak nog 1 minuut.

## 6 Serveren
- Haal de risotto van het vuur. Voeg de paksoi, roomkaas, Koreaanse kruidenmix toe en meng goed. Breng op smaak met peper en zout.
- Verdeel de risotto over diepe borden en leg de misochampignons erbovenop.
- Garneer met het sesamzaad, de cashewstukjes en het groene gedeelte van de bosui.





# Zoete-aardappelstoof met zure room en jalapeño

![Zoete-aardappelstoof met zure room en jalapeño](/receptenboek/assets/images/zoete-aardappelstoof-met-zure-room-en-jalapeno.jpg)

- Totale tijd: 25 - 30 min.
- Caloriebewust

## Benodigdheden
4 personen

| Ingredient | Hoeveelheid |
|------------|-------------|
| Basmatirijst | 200g |
| Zoete aardappel | 150g |
| Rode splitlinzen | 200g |
| Knoflookteen | 2 stuks |
| Rode ui | 2 stuks |
| Rode puntpaprika | 4 stuks |
| Tomaat | 6 stuks |
| Dadelstukjes | 80g |
| Peruaanse kruidenmix | genoeg (paprika, koriander, kurkuma, peper, chilies, komijn, ui, knoflook, citroensapconcentraat) |
| Gemalen komijnzaad | 1tl |
| Verse koriander | 20g |
| Limoen | 2 stuks |
| Jalapeño | 2 stuks |
| Zure room | 200g |
| Pompoenpitten | 20g |
| Zoutarme groentebouillon | 700ml |
| Olijfolie | 2el |
| Water voor rijst | 600ml |


## 1 Voorbereiden
- Bereid de bouillon
- Snipper de ui en pers de knoflook of snijd fijn.
- Snijd het steeltje van de jalapeño en haal zaadjes eruit. Snijd in ringetjes.
- Houd 2 ringetjes per persoon apart ter garnering.

## 2 Groenten snijden
- Schil de zoete aardappel of was grondig en snijd in grove stukken van maximaal 2cm.
- Snijd de tomaat in blokjes en de puntpaprika in dunne reepjes.
- Verhit een scheutje olijfolie in een steelpan op middelhoogvuur. Bak de knoflook, ui en dadels 1 - 2 minuten.

## 3 Rijst koken
- Voeg de jalapeño, puntpaprika, tomaat, zoete aardappel en Peruaanse kruidenmix toe en bak nog 2 minuten. Breng op smaak met peper en zout.
- Voeg de rijst en de aangegeven hoeveelheid water toe aan een pan.
- Kook, afgedekt, 10 - 12 minuten. Zet daarna het vuur uit en laat 5 minuten afgedekt staan.

## 4 Pompoenpitten roosteren
- Voeg de bouillon, de linzen en het komijnzaad toe aan de groenten.
- Laat 1 minuut koken. Verlaag dan het vuur en dek de pan af. Laat 8 - 10 minuten zachtjes koken. Roer af en toe door.
- Verhit ondertussen een koekenpan zonder olie op hoog vuur en rooster de pompoenpitten tot ze beginnen te poffen. Haal uit de pan en houd apart.

## 5 Garnering snijden
- Snijd de koriander grof.
- Rasp de limoen met een fijne rasp. Snijd de limoen in 4 partjes.
- Voeg de koriander en per persoon: 1tl limoenrasp en het sap van 1 limoenpartje toe aan de rijst. Meng goed.

## 6 Serveren
- Serveer de rijst en de stoof in kommen of diepe borden.
- Schep de zure room erbovenop. Garneer met de pompoenpitten en de achtergehouden jalapeño.
- Serveer met de limoenpartjes.





# Linzencurry met zoete aardappel en naan

![Linzencurry met zoete aardappel en naan](/receptenboek/assets/images/linzencurry-met-zoete-aardappel-en-naan.jpg)

- Totale tijd: 35 - 45 min.
- Caloriebewust
- Veggie

## Benodigdheden
4 personen

| Ingredient | Hoeveelheid |
|------------|-------------|
| Zoete aardappel | 300g |
| Knoflookteen | 4 stuks |
| Rode ui | 2 stuks |
| Verse gember | 4 tl |
| Spinazie | 250g |
| Pruimtomaat | 4 stuks |
| Verse bladpeterselie en koriander | 10g |
| Linzen | 2 pakken |
| Labne | 80g |
| Gele currykruiden | 8g (kurkuma, laos, koriander, gember, foelie, chili, citroengras, venkelzaad, komijnzaad, kaneel, kruidnagel, ui, knoflook) |
| Kokosmelk | 200ml |
| Naanbrood met kruiden | 2 stuks |
| Komkommer | 1 stuk |
| Zoutarme groentebouillon | 500ml |
| Extra vierge olijfolie | 1 el |
| Wittewijnazijn | 2 tl |
| Roomboter | 2 el |


## 1 Voorbereiden
- Verwarm de oven voor op 200 graden. Bereid de bouillon.
- Schil de zoete aardappel en snijd in blokjes van 1 - 2 cm.
- Snipper de ui. Pers de knoflook of snijd fijn.
- Rasp de gember of snijd fijn.

## 2 Smaakmakers bakken
- Verhit een hapjesplan zonder olie op middelhoog vuur.
- Voeg de currykruiden toe en bak 1 - 2 minuten, of tot ze beginnen te geuren.
- Voeg een klontje roomboter toe en laat smelten.
- Voeg de ui, de gember, en 3/4 van de knoflook toe. Bak nog 2 - 3 minuten.

## 3 Curry maken
- Voeg de zoete aardappel toe aan de hapjespan en bak, afgedekt, nog 1 - 2 minuten op middelhoog vuur.
- Voeg de bouillon en kokosmelk toe en laat het geheel, afgedekt, 10 minuten zachtjes koken op laag vuur.
- Haal de deksel van de pan en kook nog 5 minuten, of kook eventueel langer als de stoof nog erg waterig is.

## 4 Salade maken
- Scheur of snijd ondertussen de spinazie klein.
- Meng in een saladekom de extra vierge olijfolie en wittewijnazijn. Breng op smaak met peper en zout.
- Snijd de komkommer in blokjes en de tomaat in kwarten. Voeg de komkommer, tomaat, en de helft van de spinazie toe aan de saladekom. Meng goed door de dressing heen.
- Snijd de peterselie en koriander grod. Laat de linzen uitlekken in een vergiet.

## 5 Afmaken
- Voeg de linzen en de overige spinazie toe aan de curry. Roer goed door tot de spinazie is geslonken.
- Laat de stoof nog 3 - 5 minuten op laag vuur pruttelen, of langer als de stoof nog te waterig is.
- Meng in een kleine kom de labne met de overige knoflook en 1/3 van de verse kruiden.
- Voeg extra vierge olijfolie naar smaak toe en breng op smaak met peper en zout.

## 6 Serveren
- Bak ondertussen de naan 2 - 3 minuten in de oven.
- Serveer de curry met de naan en salade ernaast.
- Garneer met de overige verse kruiden en serveer de labnesaus ernaast.





# Honing mosterd zalm met geroosterde krieltjes

![Honing mosterd zalm met geroosterde krieltjes](/receptenboek/assets/images/honing-mosterd-zalm-met-geroosterde-krieltjes.jpg)

- Totale tijd: 40 min.
- Caloriebewust, familie, extra groente

## Benodigdheden
4 personen

| Ingredient | Hoeveelheid |
|------------|-------------|
| Krieltjes | 800g |
| Zalmfilet | 4 stuks |
| Wortel | 4 stuks |
| Gele wortel | 4 stuks |
| Rode ui | 2 stuks |
| Knoflookteen | 8 stuks |
| Verse tijm | 20g |
| Honing | 2 el |
| Mosterd | 2 el |
| Bruine basterdsuiker | 4 tl |
| Zoutarme groentebouillon | 200 ml |
| [Plantaardige] boter | 2 el |
| Olijfolie | 2 el |
| Peper en zout | naar smaak |

## 1 Krieltjes roosteren
- Verwarm de oven voor op 220 graden.
- Was de krieltjes en halveer ze. Snijd eventueel grote krieltjes in vieren.
- Meng de krieltjes in een kom met 1/2 el olijfolie per persoon en breng op smaak met peper en zout.
- Verdeel de krieltjes over de helft van een bakplaat met bakpapier en bak 30 - 35 minuten in de oven of tot ze goudbruin zijn. Schep halverwege om.

## 2 Groenten snijden
- Halveer de beide wortelsoorten en snijd in repen van 1 cm breed.
- Snijd de rode ui in halve ringen.
- Pers de knoflook of snijd fijn.
- Ris de blaadjes van de takjes tijm en snijd grof.

## 3 Groenten stoven
- Verhit 1/2 el roomboter per persoon in een hapjespan met deksel en bak rode ui en wortel 1 minuut op middelhoog vuur.
- Voeg de knoflook, verse tijm en per persoon 50 ml groentebouillon en 1 tl basterdsuiker toe.
- Laat afgedekt 10 - 12 minuten koken. Haal de deksel van de pan en verhit de groenten nog 2 min zonder deksel.

## 4 Sausje maken
- Meng in een kleine kom de honing met de mosterd.

## 5 Zalm bakken
- Dep de zalm droog met keukenpapier en wrijf in met peper en zout.
- Smeer de zalm in met het honing mosterd sausje.
- Leg de zalm op de andere helft van de bakplaat met bakpapier en bak de zalm de laatste 10 - 12 minuten met de krieltjes mee in de oven.

## 6 Serveren
- Verdeel de zalm over de borden. Serveer met de geroosterde krieltjes en groenten.





# Sweet & sticky rundergehaktballetjes

![Sweet & sticky rundergehaktballetjes](/receptenboek/assets/images/sweet-sticky-rundergehaktballetjes.jpg)

- Totale tijd: 25 min.
- Caloriebewust, familie

## Benodigdheden
4 personen

| Ingredient | Hoeveelheid |
|------------|-------------|
| Rundergehakt met Italiaanse kruiden | 400g |
| Panko paneermeel | 20g |
| Aardappelen | 1000g |
| Ui | 2 stuks |
| Sperziebonen | 600g |
| Tomatenketchup | 120g |
| Sojasaus | 20ml |
| Verse bladpeterselie en bieslook | 20g |
| Zoutarm groentebouillonblokje | 1 stuk |
| Honing | 4 el |
| Water voor saus | 120ml |
| Mosterd | 2 tl |
| [Plantaardige] boter | 2 el |
| Olijfolie | 2 el |
| Peper en zout | naar smaak |

## 1 Aardappelen koken
- Was of schil de aardappelen en snijd in grove stukken.
- Zet de aardappelen onder water in een pot en verkruimel het bouillonblokje erboven.
- Kook de aardappelen 12 - 15 minuten. Bewaar wat van het kookvocht, giet daarna af en bewaar apart.
- Verwijder de steelaanzet van de sperziebonen en halveer ze.
- Snipper de ui fijn.

## 2 Gehaktballetjes maken
- Schenk een bodempje water in een sauteerpan met deksel. Voeg de sperziebonen toe.
- Breng aan de kook en laat, afgedekt, 4 - 6 minuten zachtjes koken. Giet daarna af en laat uitstomen.
- Meng in een kom het gehakt met de panko. Draai er 3 gehaktballetjes per persoon van.
- Verhit een klein klontje boter in een pan met deksel op hoog vuur en bak de gehaktballetjes in 2 - 3 minuten rondom bruin.
- Verlaag het vuur naar middelmatig en voeg de helft van de ui toe. Bak, afgedekt, 4 - 6 minuten.

## 3 Bakken
- Besprenkel de sperziebonen met olijfolie, voeg de overige ui toe en bak 3 - 4 minuten op middelmatig vuur. Breng op smaak met peper en zout.
- Meng ondertussen in een kleine kom de ketchup met de sojasaus, de honing en de aangegeven hoeveelheid water. Voeg de saus toe aan de gehaktballetjes en bak 2 minuten al roerend. Zet daarna het vuur uit.
- Snijd ondertussen de verse kruiden fijn.

## 4 Serveren
- Stamp de aardappelen met een aardappelstamper tot een grove puree. Voeg de mosterd, de verse kruiden, een klein klontje boter en eventueel een scheutje kookvocht toe en stamp goed door. Breng op smaak met peper en zout.
- Verdeel de puree over de borden. Schep de groenten en de gehaktballetjes ernaast.
- Besprenkel met de saus uit de pan.





# Eén-pot-spaghetti met tomatensaus

![Eén-pot-spaghetti met tomatensaus](/receptenboek/assets/images/een-pot-spaghetti-met-tomatensaus.jpg)

- Totale tijd: 25 min.
- Caloriebewust, veggie, extra groente

## Benodigdheden
4 personen

| Ingredient | Hoeveelheid |
|------------|-------------|
| Spaghetti | 360g |
| Ui | 2 stuks |
| Knoflookteen | 4 stuks |
| Roomkaas | 100g |
| Tomaat | 8 stuks |
| Siciliaanse kruidenmix | 2 zakjes |
| Parmigiano Reggiano DOP | 4 stuks |
| Passata | 400g |
| Verse bladpeterselie & basilicum | 20g |
| Rucola en veldsla | 120g |
| Gedroogde oregano | 2 zakjes |
| Zoutarme groentebouillon | 800ml |
| Olijfolie | 2 el |
| Peper en zout | naar smaak |

## 1 Voorbereiden
- Bereid de bouillon. Snipper de ui. Pers de knoflook of snijd fijn.
- Snijd de tomaat in blokjes. Verhit de olijfolie in een soeppot of grote pot met deksel.
- Fruit de knoflook en ui 1 - 2 minuten.
- Breek de spaghetti in de helft en voeg toe aan de soeppot. Voeg de tomatenblokjes, passata, oregano, Siciliaanse kruidenmix en bouillon toe.

## 2 Saus maken
- Kook de pasta, afgedekt, 3 minuten.
- Kook daarna nog 7 - 9 minuten zonder deksel.
- Roer regelmatig door en verlaag eventueel het vuur of voeg extra water toe als de saus te snel indikt. Breng op smaak met peper en zout.

## 3 Kruidenroomkaas maken
- Snijd de verse kruiden fijn en voeg de helft toe aan een kleine kom.
- Voeg de roomkaas toe aan de kom samen met peper en zout naar smaak. Meng goed door.
- Rasp de Parmigiano Reggiano met een grove rasp.

## 4 Serveren
- Verdeel de rucola en veldsla over de borden.
- Schep de spaghetti erop.
- Garneer met de kruidenroomkaas, de Parmigiano Reggiano, de overige bladpeterselie en het overige basilicum.





# Rijstbowl met gebakken ei en zoete Aziatische saus

![Rijstbowl met gebakken ei en zoete Aziatische saus](/receptenboek/assets/images/rijstbowl-met-gebakken-ei-en-zoete-aziatische-saus.jpg)

- Totale tijd: 25 min.
- Veggie

## Benodigdheden
4 personen

| Ingredient | Hoeveelheid |
|------------|-------------|
| Basmatirijst | 300g |
| Ei | 8 stuks |
| Groentemix met wittekool | 800g |
| Gele currykruiden | 2 zakjes |
| Limoen | 2 stuks |
| Gemberpuree | 20g |
| Knoflookteen | 4 stuks |
| Cashewstukjes | 80g |
| Gemalen kurkuma | 3 tl |
| Munt, koriander en Thais basilicum | 20g |
| Zoete Aziatische saus | 80g |
| Ui | 2 stuks |
| Sojasaus | 40ml |
| Zonnebloemolie | 4 el |
| Peper en zout | naar smaak |

## 1 Voorbereiden
- Breng ruim water aan de kook in een pan. Kook de rijst 12 - 15 minuten. Giet af en laat uitstomen.
- Snijd de ui in halve ringen.
- Verhit een scheutje zonnebloemolie in een wok of hapjespan op middelhoog vuur. Bak de groentemix en de ui 5 - 7 minuten.

## 2 Ei bakken
- Pers de knoflook of snijd fijn.
- Verhit een koekenpan zonder olie op hoog vuur. Rooster de cashewnoten tot ze goudbruin kleuren. Haal uit de pan en bewaar apart.
- Verhit een scheutje zonnebloemolie in dezelfde koekenpan en bak het ei. Breng op smaak met peper en zout.

## 3 Mengen
- Roer de rijst, knoflook, gele currykruiden, kurkuma, gemberpuree en sojasaus door de groenten. Bak 2 - 3 minuten en roer zo min mogelijk door. Breng op smaak met peper en zout.
- Snijd ondertussen de verse kruiden grof. Snijd de limoen in partjes.

## 4 Serveren
- Serveer de rijst op diepe borden. Leg het spiegelei erbovenop en besprenkel met de zoete Aziatische saus.
- Garneer met de verse kruiden en cashewnoten.
- Serveer de limoenpartjes ernaast.





# Spaghetti met champignonroomsaus en spekjes

![Spaghetti met champignonroomsaus en spekjes](/receptenboek/assets/images/spaghetti-met-champignonroomsaus-en-spekjes.jpg)

- Totale tijd: 30 min.

## Benodigdheden
4 personen

| Ingredient | Hoeveelheid |
|------------|-------------|
| Spaghetti | 360g |
| Knoflookteen | 2 stuks |
| Sjalot | 2 stuks |
| Champignons | 240g |
| Portobello | 4 stuks |
| Spekblokjes | 120g |
| Citroen | 1 stuk |
| Verse krulpeterselie | 20g |
| Kookroom | 200ml |
| Geraspte pecorino | 100g |
| Olijfolie | 2 el |
| Roomboter | 2 el |
| Peper en zout | naar smaak |

## 1 Voorbereiden
- Breng ruim water, met een snuf zout, aan de kook in een pan met deksel voor de spaghetti.
- Pers de knoflook of snijd fijn. Snipper de sjalot. Snijd de champignons in kwarten. Snijd de portobello in lange dunne repen.
- Kook de spaghetti, afgedekt, 8 - 10 minuten al dente in de pan met deksel. Giet daarna af maar bewaar het kookvocht.

## 2 Spekblokjes bakken
- Verhit een grote hapjespan zonder olie, op middelhoog vuur en bak de spekblokjes in 4 - 6 minuten knapperig. Haal uit de pan en bewaar apart.
- Rasp ondertussen de schil van een citroen met een fijne rasp en pers de citroen uit. Snijd de verse krulpeterselie fijn.

## 3 Champignons bakken
- Verhit 1/2 el olijfolie per persoon in dezelfde hapjespan op middelhoog vuur.
- Bak de champignons en de portobello 3 - 4 minuten.
- Voeg de sjalot en de knoflook toe en roerbak 1 - 2 minuten. Breng op smaak met peper en zout.

## 4 Roerbakken
- Voeg de spaghetti, de spekblokjes en de kookroom toe aan de hapjespan met de champignons.
- Verhoog het vuur en roerbak 3 - 4 minuten, zodat de saus indikt.

## 5 Afwerken
- Verwijder de hapjespan van het vuur. Voeg per persoon 1/2 tl citroenrasp, 1 el citroensap en 1/2 el roomboter, de helft van de krulpeterselie en de helft van de pecorino toe. Breng op smaak met peper en zout en roer goed door.

## 6 Serveren
- Verdeel de spaghetti over de borden. Garneer met de overige krulpeterselie en de pecorino.





# Kipfilet in spinazie-roomsaus

![Kipfilet in spinazie-roomsaus](/receptenboek/assets/images/kipfilet-in-spinazie-roomsaus.jpg)

- Totale tijd: 50 min.
- Caloriebewust, eiwitrijk

## Benodigdheden
4 personen

| Ingredient | Hoeveelheid |
|------------|-------------|
| Kipfilet met mediterrane kruiden | 4 stuks |
| Ui | 2 stuks |
| Wortel | 4 stuks |
| Knoflookteen | 4 stuks |
| Aardappelen | 800g |
| Kookroom | 300g |
| Spinazie | 200g |
| Verse krulpeterselie en tijm | 20g |
| Zoutarme kippenbouillon | 400ml |
| [Plantaardige] roomboter | 4 el |
| Bloem | 2 el |
| Olijfolie | 2 el |
| Peper en zout | naar smaak |

## 1 Voorbereiden
- Bereid de bouillon. Snipper de ui. Snijd de wortel in dunne schijfjes.
- Pers de knoflook of snijd fijn. Was of schil de aardappelen en snijd in kwarten.
- Snijd de peterselie fijn.

## 2 Aardappelen bakken
- Verhit een scheutje olijfolie in een koekenpan met deksel op middelhoog vuur.
- Bak de aardappelen, afgedekt, 30 - 35 minuten. Haal na 20 minuten het deksel van de pan en schep regelmatig om. Breng op smaak met peper en zout.

## 3 Kipfilet bakken
- Verhit een klontje roomboter in een pan op hoog vuur. Bak de kipfilet 2 - 3 minuten per kant.
- Haal uit de pan en bewaar apart. Bewaar ook de pan met bakvet.

## 4 Laten sudderen
- Verhit opnieuw een klontje roomboter in dezelfde pan op middelmatig vuur.
- Bak de ui, knoflook en wortel 3 - 4 minuten. Voeg de bloem toe en bak 1 minuut.
- Blus af met de bouillon. Voeg de tijmtakjes toe, roer goed door en laat het geheel, afgedekt, 10 minuten sudderen.
- Voeg de kipfilet toe aan de pan en pocheer 5 - 8 minuten, of tot de kip gaar is.

## 5 Spinazie toevoegen
- Haal het deksel van de pan en voeg de room en de spinazie toe. Breng op smaak met peper en zout.
- Roer goed door en laat nog 4 - 6 minuten inkoken zonder deksel. Haal de tijmtakjes uit de pan.

## 6 Serveren
- Verdeel de aardappelen over de borden en schep de kipfilet erbij.
- Serveer met de romige spinaziesaus en garneer met de peterselie.


# Verse conchiglie met mozzarella uit de oven {#verse-conchiglie-met-mozzarella-uit-de-oven}

![Verse conchiglie met mozzarella uit de oven](/receptenboek/assets/images/verse-conchiglie-met-mozzarella-uit-de-oven.jpg)

- Totale tijd: 25 min.
- Tags: Veggie

## Benodigdheden
4 personen

| Ingredient | Hoeveelheid |
|------------|-------------|
| Conchiglie (pasta) | 400 g |
| Cherrytomaten | 300 g |
| Mozzarella (bol) | 250 g |
| Knoflook | 2 teentjes |
| Olijfolie | 2 el |
| Verse basilicum | een handvol |
| Paneermeel (optioneel) | 2 el |
| Zout & peper | naar smaak |

## 1 Voorbereiden
- Verwarm de oven voor op 200 °C.
- Breng een grote pan gezouten water aan de kook en kook de conchiglie circa 8-10 minuten al dente. Giet af en bewaar een scheutje pastawater.

## 2 Saus en samenstellen
- Verhit de olijfolie in een koekenpan en fruit de fijngehakte knoflook 1 minuut.
- Voeg de cherrytomaten toe en bak 3-4 minuten tot ze zacht worden; stamp ze lichtjes zodat er een eenvoudige saus ontstaat. Breng op smaak met zout en peper.
- Meng de gekookte conchiglie door de tomaatjes. Voeg een scheut pastawater toe als het mengsel te droog is.
- Scheur de mozzarella in stukken en meng de helft door de pasta.

## 3 Gratineer
- Doe de pasta in een ovenschaal, verdeel de resterende mozzarella erover en bestrooi eventueel met paneermeel voor een krokant korstje.
- Zet 8-10 minuten in de oven tot de kaas gesmolten en licht goudbruin is.
- Garneer met verse basilicum en serveer direct.


# Bulgogi stir-fry met noedels en varkensboerenworst {#bulgogi-stir-fry-met-noedels-en-varkensboerenworst}

![Bulgogi stir-fry met noedels en varkensboerenworst](/receptenboek/assets/images/bulgogi-stir-fry-met-noedels-en-varkensboerenworst.jpg)

- Totale tijd: 25 min.
- Tags: Caloriebewust, Extra groente, Familie

## Benodigdheden
4 personen

| Ingredient | Hoeveelheid |
|------------|-------------|
| Noedels (e.g. eiernoedels of udon) | 400 g |
| Varkensboerenworst | 300 g |
| Paprika (rood) | 1 stuk |
| Wortel | 1 grote |
| Witte kool of paksoi | 150 g |
| Lente-ui | 2 stuks |
| Knoflook | 2 teentjes |
| Sojasaus | 3 el |
| Sesamolie | 1 el |
| Honing of suiker | 1 tl |
| Rijstazijn of mirin | 1 el |
| Sesamzaad | 1 tl |

## 1 Voorbereiden
- Kook de noedels volgens de verpakking, giet af en zet apart.
- Snijd de varkensboerenworst in plakjes. Snijd paprika en wortel in dunne reepjes en hak de knoflook fijn.

## 2 Saus maken
- Meng sojasaus, sesamolie, honing en rijstazijn in een kom tot een gladde saus.

## 3 Roerbakken
- Verhit een scheut olie in een wok of grote koekenpan en bak de plakjes worst rondom goudbruin.
- Voeg de knoflook, paprika, wortel en kool toe en roerbak 3-4 minuten tot de groenten beetgaar zijn.
- Voeg de gekookte noedels en de saus toe en schep alles goed om. Bak nog 1-2 minuten zodat de smaken zich mengen.
- Bestrooi met gesneden lente-ui en sesamzaad voor het serveren.


# Kipworstjes met wortelpuree {#kipworstjes-met-wortelpuree}

![Kipworstjes met wortelpuree](/receptenboek/assets/images/kipworstjes-met-wortelpuree.jpg)

- Totale tijd: 35 min.
- Tags: Familie, Extra groente, Caloriebewust

## Benodigdheden
4 personen

| Ingredient | Hoeveelheid |
|------------|-------------|
| Kipworstjes | 8 stuks |
| Aardappelen (kruimig) | 800 g |
| Wortelen | 500 g |
| Melk | 50-100 ml |
| Boter of olie | 2 el |
| Verse peterselie | een handvol |
| Zout & peper | naar smaak |

## 1 Voorbereiden
- Schil de aardappelen en snijd in gelijke stukken. Schil de wortelen en snijd in grotere stukken.
- Kook de aardappelen in ruim water circa 12-15 minuten tot ze gaar zijn. Kook de wortelen in een aparte pan 10-12 minuten tot zacht.

## 2 Pureren
- Giet de aardappelen en wortelen af en stamp samen met boter en een scheut melk tot een smeuïge puree. Breng op smaak met zout, peper en fijngehakte peterselie.

## 3 Kipworstjes bereiden
- Verhit een koekenpan met een klein scheutje olie en bak de kipworstjes rondom goudbruin en gaar (ongeveer 8-10 minuten). Draai regelmatig.

## 4 Serveren
- Serveer de kipworstjes op een bedje van wortelpuree. Garneer met extra peterselie en eventueel een scheutje mosterd of jus naar smaak.


# Parelcouscous met geroosterde puntpaprika en witte kaas {#parelcouscous-met-geroosterde-puntpaprika-en-witte-kaas}

![Parelcouscous met geroosterde puntpaprika en witte kaas](/receptenboek/assets/images/parelcouscous-met-geroosterde-puntpaprika-en-witte-kaas.jpg)

- Totale tijd: 40 min.
- Tags: Veggie, Extra groente

## Benodigdheden
4 personen

| Ingredient | Hoeveelheid |
|------------|-------------|
| Parelcouscous | 300 g |
| Puntpaprika (rood/geel) | 3 stuks |
| Witte kaas (feta of vergelijkbaar) | 150 g |
| Rode ui | 1 stuk |
| Peterselie | een handvol |
| Citroen (sap) | 1 stuk |
| Olijfolie | 2 el |
| Groentebouillon | 600 ml |
| Zout & peper | naar smaak |

## 1 Puntpaprika roosteren
- Verwarm de oven naar 200 °C. Halveer de puntpaprika's, verwijder zaad en pitten, besprenkel met olijfolie en rooster 20-25 minuten tot ze zacht en iets gekarameliseerd zijn.

## 2 Parelcouscous koken
- Breng de groentebouillon aan de kook en voeg de parelcouscous toe. Kook volgens verpakking (meestal 10-12 minuten) tot beetgaar. Giet af en laat uitstomen.

## 3 Afmaken
- Snijd de geroosterde paprika in repen. Snijd de rode ui fijn en hak de peterselie.
- Meng de parelcouscous met de paprika, verkruimelde witte kaas, rode ui, citroensap en olijfolie. Breng op smaak met zout en peper.
- Serveer lauwwarm of op kamertemperatuur.


# Pittige udonnoedels met gemarineerde eieren {#pittige-udonnoedels-met-gemarineerde-eieren}

![Pittige udonnoedels met gemarineerde eieren](/receptenboek/assets/images/pittige-udonnoedels-met-gemarineerde-eieren.jpg)

- Totale tijd: 45 min.
- Tags: Veggie

## Benodigdheden
4 personen

| Ingredient | Hoeveelheid |
|------------|-------------|
| Udonnoedels (vers of gedroogd) | 400 g |
| Eieren | 4 stuks |
| Sojasaus | 4 el |
| Mirin of rijstazijn | 2 el |
| Suiker of honing | 1 tl |
| Sesamolie | 1 el |
| Knoflook | 2 teentjes |
| Chili- of sriracha saus | 1-2 el naar smaak |
| Paksoi of spinazie | 150 g |
| Lente-ui | 2 stuks |
| Sesamzaad | 1 tl |

## 1 Eieren marineren
- Kook de eieren 6-7 minuten voor zachtgekookte eieren. Koel ze direct in koud water, pel voorzichtig.
- Meng in een kom sojasaus, mirin en suiker. Leg de gepelde eieren in de marinade en laat minimaal 15 minuten (langer is beter) marineren.

## 2 Noedels en saus
- Kook de udon volgens de verpakking; giet af.
- Verhit sesamolie in een pan, fruit fijngehakte knoflook en voeg de chili saus toe. Voeg een scheutje water, 1-2 eetlepels sojasaus en eventueel wat extra mirin toe om een licht plakkerige saus te maken.

## 3 Roerbakken en serveren
- Roerbak de paksoi kort tot geslonken. Voeg de gekookte udon en saus toe en schep goed om.
- Halveer de gemarineerde eieren en leg ze bovenop de noedels. Bestrooi met gesneden lente-ui en sesamzaad.



---



















































































# Dahl met kokos en paneer met linzen, groenten en naan {#dahl-met-kokos-en-paneer-met-linzen-groenten-en-naan}

![Dahl met kokos en paneer met linzen, groenten en naan](/receptenboek/assets/images/dahl-met-kokos-en-paneer-met-linzen-groenten-en-naan.jpg)

- Totale tijd: 35 min.
- veggie, vis & veggie, veggie, pescatarian, flexitarian, everyday healthy, flexitarian, hoofdgerecht, indiase.
- Bron: https://www.hellofresh.nl/recipes/dahl-met-kokos-en-paneer-6389c9b22bf271b6f70ff612

## Benodigdheden
2 personen

| Ingredient | Hoeveelheid |
|------------|-------------|
| Ui | 1 stuk(s) |
| cm Verse gember | 2.5 |
| Wortel | 2 stuk(s) |
| zakje(s) Kerriepoeder | 1 |
| Tomatenpuree | 1 |
| Kokosmelk | 180 ml |
| Rode splitlinzen | 50 gram |
| Spinazie | 200 gram |
| Paneer | 130 gram |
| Naan met kruiden | 1 stuk(s) |
| Verse koriander | 10 gram |
| Limoen | ½ stuk(s) |
| Olijfolie | 1 el |
| naar smaak Peper en zout |  |
| Zoutarme groentebouillon | 300 ml |
| Zonnebloemolie | 1 el |

## 1 Stap 1
- Verwarm de oven voor op 200 graden en bereid de bouillon. Snipper de ui en rasp de gember (eventueel met schil) fijn. Snijd de wortel in blokjes van ongeveer 1 cm. Tip: Zorg dat je de peen echt goed klein snijdt, anders wordt deze niet gaar.

## 2 Stap 2
- Verhit 1/2 el zonnebloemolie per persoon in een grote hapjespan met deksel op middelhoog vuur. Bak de ui, gember en de wortel 2 - 3 minuten. Voeg het kerriepoeder en de tomatenpuree toe. Roer goed en bak nog 2 minuten. Roer de kokosmelk los of schud het pakje flink zodat eventuele klontjes oplossen. Voeg de kokosmelk en de bouillon toe aan de pan en breng aan de kook.

## 3 Stap 3
- Voeg de rode splitlinzen toe, breng op smaak met peper en zout en kook de dahl, afgedekt, 18 – 20 minuten, of tot de linzen gaar zijn. Roer halverwege door en voeg de spinazie toe. Voeg eventueel wat water toe als de dahl te droog wordt. Tip: Linzen bevatten van alle peulvruchten de grootste hoeveelheid ijzer. Daarnaast zijn ze, net als spinazie, rijk aan vezels en kalium. Kalium helpt bij behoud van een gezonde bloeddruk.

## 4 Stap 4
- Dep ondertussen de paneer droog met keukenpapier en snijd in stukjes van ongeveer 2 cm. Verhit 1/4 el olijfolie per persoon in een koekenpan op middelhoog vuur en bak de paneer in 4 - 6 minuten lichtbruin. Breng op smaak met peper en zout. Leg op een bord met keukenpapier. Tip: Als je de paneer te lang bakt wordt hij droog.

## 5 Stap 5
- Bak de naan 2 - 3 minuten in de voorverwarmde oven. Snijd daarna de naan in punten. Hak de koriander fijn en pers de limoen uit. Meng in een grote kom de koriander met het limoensap en roer de paneer erdoor. Breng op smaak met peper en zout.

## 6 Stap 6
- Voeg de paneer met dressing vlak voor serveren toe aan de dahl en verwarm kort zodat de paneer wat zachter en warm wordt. Verdeel de dahl over kommen en serveer met de naanpunten.

---

# Gekruide kipfilet met champignonroomsaus met witte rijst, broccoli en gomasio {#gekruide-kipfilet-met-champignonroomsaus-met-witte-rijst-broccoli-en-gomasio}

![Gekruide kipfilet met champignonroomsaus met witte rijst, broccoli en gomasio](/receptenboek/assets/images/gekruide-kipfilet-met-champignonroomsaus-met-witte-rijst-broccoli-en-gomasio.jpg)

- Totale tijd: 25 min.
- lekker snel, familie, caloriebewust, veggie, vis & veggie, zonder varkensvlees, klaar in 25 minuten, klaar in 15 minuten, original, flexitarisch, extra veggies, hoofdgerecht, fusion.
- Bron: https://www.hellofresh.nl/recipes/gekruide-kipfilet-met-champignonroomsaus-63f4d970b6ae9e66039dd733

## Benodigdheden
2 personen

| Ingredient | Hoeveelheid |
|------------|-------------|
| Champignons | 250 gram |
| Witte langgraanrijst | 150 gram |
| zakje(s) Gomasio-tuinkruidenmix | 1 |
| Kipfilet met mediterrane kruiden | 2 stuk(s) |
| Kookroom | 150 ml |
| Ui | 1 stuk(s) |
| Broccoli | 200 gram |
| Olijfolie | 1.5 el |
| Zoutarm kippenbouillonblokje | ½ stuk(s) |
| Mosterd | 2 tl |
| naar smaak Peper en zout |  |

## 1 Stap 1
- Breng ruim water aan de kook in een pan met deksel voor de rijst en broccoli. Snijd de champignons in kwarten. Snipper de ui. Snijd de bloem van de broccoli in roosjes en de steel in blokjes. Weetje : Champignons zijn rijk aan het mineraal fosfor, dat samen met calcium zorgt voor stevige botten en tanden. Fosfor zit voornamelijk in vlees, vis en zuivel, maar ook in plantaardige producten zoals peulvruchten, volkoren granen en paddenstoelen.

## 2 Stap 2
- Verhit 1/4 el olijfolie per persoon in een hapjespan met deksel op middelhoog vuur en bak de ui en champignons 4 - 6 minuten, of tot de ui glazig is (zie Tip). Breng op smaak met peper en zout. Roer regelmatig door. Tip : Champignons nemen bij het bakken eerst veel vocht op en laten dit daarna weer los. Het lijkt daardoor alsof ze aanbakken, maar dat gebeurt niet - voeg dus geen extra olie toe.

## 3 Stap 3
- Verhit 1/2 el olijfolie per persoon in een koekenpan op middelhoog vuur. Bak de kipfilet in 3 - 5 minuten rondom bruin. Hij hoeft nog niet helemaal gaar te zijn.

## 4 Stap 4
- Voeg de kookroom en per persoon: 25 ml water, 1/4 kippenbouillonblokje en 1 tl mosterd toe aan de hapjespan met de champignons en ui. Laat de champignonsaus in 5 minuten inkoken (zie Tip). Voeg dan de kipfilet toe en dek de pan af. Kook de saus, afgedekt, nog 8 – 12 minuten. Tip : Proef de champignonsaus goed en roer regelmatig door. Vind je de saus nog te dun? Zet dan het vuur wat hoger, haal het deksel van de pan en laat de saus nog wat langer inkoken. Vind je de saus te dik? Voeg dan wat extra water toe.

## 5 Stap 5
- Kook de rijst, afgedekt, 10 - 12 minuten. Kook de laatste 5 - 7 minuten de broccoli mee. Giet daarna af en laat zonder deksel uitstomen.

## 6 Stap 6
- Verdeel de rijst en broccoli over de borden en garneer met de gomasio-tuinkruidenmix. Leg de kipfilet op de rijst en verdeel de champignonroomsaus erover.

---

# Krokante kikkererwten met kruidige groene currysaus met bruine rijst, Thais basilicum en geroosterde groenten {#krokante-kikkererwten-met-kruidige-groene-currysaus-met-bruine-rijst-thais-basilicum-en-geroosterde-groenten}

![Krokante kikkererwten met kruidige groene currysaus met bruine rijst, Thais basilicum en geroosterde groenten](/receptenboek/assets/images/krokante-kikkererwten-met-kruidige-groene-currysaus-met-bruine-rijst-thais-basilicum-en-geroosterde-groenten.jpg)

- Totale tijd: 35 min.
- plant-based, hoofdgerecht, thais.
- Bron: https://www.hellofresh.nl/recipes/geroosterde-bloemkool-in-groene-currysaus-681236355917498f8bf2ef31

## Benodigdheden
2 personen

| Ingredient | Hoeveelheid |
|------------|-------------|
| Bruine snelkookrijst | 150 gram |
| Knoflookteen | 2 stuk(s) |
| Rode ui | 1 stuk(s) |
| Courgette | 1 stuk(s) |
| Broccoli | 250 gram |
| Limoen | ½ stuk(s) |
| Vers citroengras | 1 stuk(s) |
| Thais basilicum | 10 gram |
| zakje(s) Groene currykruiden | 1 |
| Kokosmelk | 180 ml |
| Ongezouten pinda's | 10 gram |
| pak(ken) Kikkererwten | 1 |
| Gemalen korianderzaad | 2 tl |
| Zoutarme groentebouillon | 150 ml |
| Olijfolie | 3 el |
| Suiker | 2 tl |
| Maiszetmeel [of bloem] | ½ el |
| Water | 1 el |

## 1 Stap 1
- Verwarm de oven voor op 200 graden. Bereid de bouillon. Snijd de bloem van de broccoli in kleine roosjes en de steel in blokjes. Snijd de courgette in halve maantjes. Voeg beide toe aan een bakplaat met bakpapier en besprenkel met een scheutje olijfolie. Breng op smaak met peper en zout. Rooster 18 - 22 minuten. Schep halverwege om.

## 2 Stap 2
- Spoel de kikkererwten onder koud water, laat uitlekken in een vergiet en dep droog met keukenpapier. Voeg toe aan een kom. Voeg de gemalen koriander toe en besprenkel met een scheutje olijfolie. Breng op smaak met peper en zout. Schep goed om. Voeg toe aan een bakplaat met bakpapier en rooster 15 - 20 minuten in de oven.

## 3 Stap 3
- Breng ruim water aan de kook in een pan voor de rijst. Snipper de ui en pers de knoflook of snijd fijn. Snijd de limoen in 4 partjes. Knik de citroengrasstengels op minstens 3 plaatsen. Kook de rijst 10 minuten. Giet daarna af en bewaar apart.

## 4 Stap 4
- Verhit een scheutje olijfolie in een wok of hapjespan op middelhoog vuur. Bak de knoflook en ui 2 minuten. Voeg de groene currykruiden toe en bak 1 minuut. Voeg de kokosmelk, het citroengras, de suiker en de bouillon toe. Breng aan de kook laat 5 minuten zachtjes koken.

## 5 Stap 5
- Meng in een kleine kom het maiszetmeel met de aangegeven hoeveelheid water. Scheur of snijd het Thais basilicum grof. Voeg het maiszetmeelmengsel en de helft van het Thaise basilicum toe aan de curry. Roer goed door en breng op smaak met peper en zout. Laat zachtjes koken tot serveren. Hak de pinda's grof.

## 6 Stap 6
- Haal het citroengras uit de curry. Serveer de rijst en de geroosterde groenten op borden. Verdeel de currysaus en krokante kikkererwten eroverheen. Garneer met de pinda's en het overige Thais basilicum. Serveer de limoenpartjes ernaast.

---

# Gevulde paprika met chili con carne met basmatirijst en labne {#gevulde-paprika-met-chili-con-carne-met-basmatirijst-en-labne}

![Gevulde paprika met chili con carne met basmatirijst en labne](/receptenboek/assets/images/gevulde-paprika-met-chili-con-carne-met-basmatirijst-en-labne.jpg)

- Totale tijd: 40 min.
- veggie, caloriebewust, vis & veggie, familie, zonder varkensvlees, klaar in 25 minuten, klaar in 15 minuten, original, flexitarisch, extra groente, hoofdgerecht, mexicaans.
- Bron: https://www.hellofresh.nl/recipes/gevulde-paprika-met-chili-con-carne-637f44ea35728a6b3702cb8e

## Benodigdheden
2 personen

| Ingredient | Hoeveelheid |
|------------|-------------|
| Paprika | 2 stuk(s) |
| Basmatirijst | 75 gram |
| Ui | 1 stuk(s) |
| Rode peper | ½ stuk(s) |
| Paprika | 1 stuk(s) |
| Tomaat | 2 stuk(s) |
| Half-om-halfgehakt | 200 gram |
| ⅔ zakje(s) Mexicaanse kruiden |  |
| pak(ken) Rode kidneybonen | 1 |
| Labne | 40 gram |
| Geraspte cheddar | 25 gram |
| [Plantaardige] roomboter | 1 el |
| Zwarte balsamicoazijn | 2 tl |
| naar smaak Peper en zout |  |

## 1 Stap 1
- Verwarm de oven voor op 200 graden. Breng ruim water aan de kook in een pan met deksel voor de rijst. Snijd de groene paprika in de lengte doormidden, verwijder de zaadlijsten en leg de groene paprika met de open kant naar beneden op een bakplaat met bakpapier. Bak de groene paprika 15 – 20 minuten in de voorverwarmde oven, of tot hij lichtbruin kleurt.

## 2 Stap 2
- Kook ondertussen de basmatirijst, afgedekt, 12 – 15 minuten in de pan met deksel. Giet daarna af en laat zonder deksel uitstomen.

## 3 Stap 3
- Snipper ondertussen de ui. Verwijder de zaadlijsten van de rode peper en snijd fijn. Snijd de overige paprika en tomaat in blokjes.

## 4 Stap 4
- Verhit de roomboter in een wok of hapjespan met deksel en fruit de ui 2 minuten op middellaag vuur. Voeg het Italiaans gekruide half-om-half gehakt, de rode peper en de Mexicaanse kruiden toe en breng op smaak met peper en zout. Bak het gehakt in 1 – 2 minuten los op middelhoog vuur - het hoeft nog niet gaar te zijn. Tip: Let op: de rode peper is pittig! Eten er kinderen mee of houd je niet zo van pittig? Voeg dan de helft van de rode peper toe, of houd het apart om later mee te garneren.

## 5 Stap 5
- Voeg de tomaat- en paprikablokjes, kidneybonen (afgieten is niet nodig) en de zwarte balsamicoazijn toe aan de wok of hapjespan. Dek de pan af en laat 10 – 12 minuten stoven op middelmatig vuur. Haal de laatste 5 – 6 minuten het deksel van de pan. Roer regelmatig door en breng op smaak met peper en zout. Tip: Wist je dat kidneybonen van alle bonen de meeste vezels bevatten? Het eten van voldoende vezels is niet alleen goed voor je darmen, maar verlaagt ook het risico op hart- en vaatziekten.

## 6 Stap 6
- Verdeel de rijst over de borden en leg de groene paprika's ernaast. Vul de groene paprika's met de chili. Garneer met de labne en de geraspte cheddar. Tip: Wist je dat dit gerecht, voornamelijk door de paprika's, ruim 200% van de ADH vitamine C bevat?

---

# Conchiglie met misochampignons met Grana Padano, spinazie en gomasio {#conchiglie-met-misochampignons-met-grana-padano-spinazie-en-gomasio}

![Conchiglie met misochampignons met Grana Padano, spinazie en gomasio](/receptenboek/assets/images/conchiglie-met-misochampignons-met-grana-padano-spinazie-en-gomasio.jpg)

- Totale tijd: 25 min.
- caloriebewust, veggie, vis & veggie, familie, zonder varkensvlees, klaar in 25 minuten, klaar in 15 minuten, original, flexitarisch, extra groente, lekker snel, hoofdgerecht.
- Bron: https://www.hellofresh.nl/recipes/gigli-met-misochampignons-67b5e8d9381832d770717edb

## Benodigdheden
2 personen

| Ingredient | Hoeveelheid |
|------------|-------------|
| Witte miso | 40 gram |
| Champignons | 250 gram |
| Spinazie | 200 gram |
| Knoflookteen | 2 stuk(s) |
| Grana Padanovlokken DOP | 20 gram |
| Kookroom | 150 gram |
| Rode peper | ½ stuk(s) |
| zakje(s) Gomasio-tuinkruidenmix | 1 |
| Conchiglie | 180 gram |
| Ui | 1 stuk(s) |
| Olijfolie | 1 el |
| naar smaak Peper en zout |  |

## 1 Stap 1
- Breng ruim water aan de kook in een pan voor de pasta. Verwijder de zaadlijsten van de rode peper (let op: pittig! Gebruik naar smaak) en snijd fijn. Snipper de ui. Pers de knoflook of snijd fijn. Snijd de champignons in kwarten. Kook de pasta, afgedekt, 14 - 16 minuten. Giet daarna af, maar bewaar 50 ml kookvocht per persoon.

## 2 Stap 2
- Verhit een scheutje olijfolie in een hapjespan op middelhoog vuur. Bak de champignons 3 - 4 minuten. Roer de knoflook, ui en rode peper erdoor en bak 1 - 2 minuten verder. Voeg de witte miso (let op: zout! Gebruik naar smaak) en room toe en verhit nog 1 - 2 minuten.

## 3 Stap 3
- Roer de spinazie door de saus en kook 2 - 3 minuten verder, of tot de spinazie geslonken is. Roer de pasta door de saus en voeg eventueel wat van het kookvocht toe. Proef en breng eventueel op smaak met peper en zout. Meng ondertussen in een kleine kom de Grana Padano met de gomasio-tuinkruidenmix.

## 4 Stap 4
- Verdeel de pasta over de borden. Garneer met de Grana Padano-gomasiotopping.

---

# Varkenshaas met harissa, granaatappel en pompoen met witte kaas, tahin en bulgur {#varkenshaas-met-harissa-granaatappel-en-pompoen-met-witte-kaas-tahin-en-bulgur}

![Varkenshaas met harissa, granaatappel en pompoen met witte kaas, tahin en bulgur](/receptenboek/assets/images/varkenshaas-met-harissa-granaatappel-en-pompoen-met-witte-kaas-tahin-en-bulgur.jpg)

- Totale tijd: 25 min.
- lekker snel, hoofdgerecht.
- Bron: https://www.hellofresh.nl/recipes/global-cuisine-and-quick-25-min-chicken-or-pork-couscous-or-grains-6644b2c2f3feb95b85903bb1

## Benodigdheden
2 personen

| Ingredient | Hoeveelheid |
|------------|-------------|
| Varkenshaas | 2 stuk(s) |
| Citroen | 1 stuk(s) |
| Bulgur | 150 gram |
| Pompoenblokjes | 150 gram |
| Rode ui | 1 stuk(s) |
| Tahinsaus | 40 gram |
| zakje(s) Za'atar | 1 |
| Spinazie | 100 gram |
| Witte kaas | 50 gram |
| Granaatappel | ½ stuk(s) |
| Verse bladpeterselie | 10 gram |
| zakje(s) Hello Harissa | 1 |
| Olijfolie | 2 el |
| Extra vierge olijfolie | 1 el |
| [Plantaardige] roomboter | 1 el |
| Zoutarm groentebouillonblokje | 1 stuk(s) |
| naar smaak Peper en zout |  |

## 1 Stap 1
- Verwarm de oven voor op 200 graden. Snijd de ui in 8 partjes. Verdeel de ui en pompoen over een bakplaat met bakpapier. Besprenkel met de helft van de olijfolie. Breng op smaak met peper en zout en schep goed om. Rooster de groenten 14 - 16 minuten in de oven. Schep halverwege om. Voeg de bulgur en ruim water toe aan een pan zodat de bulgur goed onder water staat. Verkruimel het bouillonblokje erboven. Breng het water aan de kook en kook de bulgur in 10 minuten op laag vuur gaar. Roer af en toe door.

## 2 Stap 2
- Rasp de schil van de citroen. Snijd de helft van de citroen in partjes en pers de andere helft uit boven een diep bord. Voeg de harissa (let op: pittig! Gebruik naar smaak), de overige olijfolie en 1/2 tl citroenrasp per persoon toe. Roer goed door. Verhit de roomboter in een koekenpan op hoog vuur. Bak de varkenshaas in 2 - 3 minuten rondom bruin. Leg de varkenshaas in een ovenschaal en schenk het harissamengsel erover. Rooster de varkenshaas 6 - 8 minuten in de oven.

## 3 Stap 3
- Rol ondertussen de granaatappel al duwend over het aanrecht zodat je de pitjes hoort kraken. Snijd de granaatappel doormidden en haal de granaatappelpitjes uit de schil. Hak de peterselie grof. Meng in een kleine kom de tahin met het sap van 1 citroenpartje per persoon. Roer de spinazie, za'atar en de extra vierge olijfolie door de bulgur (zie Tip). Meng goed door en breng op smaak met peper en zout. Tip: Zorg ervoor dat de bulgur nog warm is, zodat de spinazie kan slinken.

## 4 Stap 4
- Snijd de varkenshaas in plakken. Verdeel de bulgur over diepe borden en leg de pompoen, ui en varkenshaas erbovenop. Verkruimel de witte kaas eroverheen en besprenkel met de tahinsaus. Garneer met de peterselie en de granaatappelpitjes.

---

# Zelfgemaakte bruschetta-burgers met balsamico-aardappeltjes en komkommersalade {#zelfgemaakte-bruschetta-burgers-met-balsamico-aardappeltjes-en-komkommersalade}

![Zelfgemaakte bruschetta-burgers met balsamico-aardappeltjes en komkommersalade](/receptenboek/assets/images/zelfgemaakte-bruschetta-burgers-met-balsamico-aardappeltjes-en-komkommersalade.jpg)

- Totale tijd: 25 min.
- familie, lekker snel, hoofdgerecht.
- Bron: https://www.hellofresh.nl/recipes/homemade-bruschetta-burgers-65ae461b2052454790628b7e

## Benodigdheden
2 personen

| Ingredient | Hoeveelheid |
|------------|-------------|
| Tomaat | 2 stuk(s) |
| Vers basilicum | 5 gram |
| Knoflookteen | 2 stuk(s) |
| Ui | 1 stuk(s) |
| Geraspte Goudse kaas | 25 gram |
| Rundergehakt met Italiaanse kruiden | 200 gram |
| Aardappelen | 400 gram |
| Komkommer | 1 stuk(s) |
| Hamburgerbol met sesam | 2 stuk(s) |
| Mosterd | 2 tl |
| [Plantaardige] mayonaise | 2 el |
| Witte balsamicoazijn | 2 tl |
| Extra vierge olijfolie | ½ el |
| Olijfolie | ½ el |
| [Plantaardige] roomboter | 1 el |
| Zwarte balsamicoazijn | 4 tl |
| naar smaak Peper en zout |  |

## 1 Stap 1
- Verwarm de oven voor op 200 graden. Snipper de ui. Pel de knoflook, houd de helft apart en pers de overige knoflook of snijd fijn. Schil de aardappelen of was grondig en snijd in plakken van 1/2 cm dik. Zet de aardappelen ruim onder water in een pan en kook, afgedekt, 6 - 7 minuten. Giet af en laat uitstomen.

## 2 Stap 2
- Verhit de roomboter in een koekenpan op middelhoog vuur en bak de aardappelen in 7 minuten goudbruin. Voeg de fijngesneden knoflook toe, samen met de helft van de ui en de helft van de balsamicoazijn. Bak 3 minuten verder en breng op smaak met peper en zout.

## 3 Stap 3
- Snijd de tomaat in blokjes, snijd het basilicum in reepjes en voeg de tomaat en basilicum toe aan een kom. Voeg de extra vierge olijfolie en de overige balsamicoazijn toe en meng goed. Breng op smaak met peper en zout en zet opzij.

## 4 Stap 4
- Snijd de komkommer in dunne reepjes. Meng in een saladekom de komkommerreepjes, de mosterd, de witte balsamicoazijn en de helft van de mayonaise toe. Meng goed, breng op smaak met peper en zout en zet opzij. Meng in een kom het gehakt met de overige ui. Vorm een burger van het gehaktmengsel.

## 5 Stap 5
- Snijd het broodje open en rooster het 4 - 5 minuten in de oven. Verhit de olijfolie in een koekenpan op middelhoog vuur. Bak de burger 2 minuten per kant en beleg met de geraspte kaas. Zet het vuur lager en dek de pan af, zodat de kaas kan smelten.

## 6 Stap 6
- Wrijf de achtergehouden knoflook over de binnenkant van het broodje. Bestrijk met de overige mayonaise en beleg met de burger en de bruschetta-topping. Serveer de burger met de komkommersalade en aardappelschijfjes. Weetje: Wist je dat tomaten veel voordelen hebben voor je gezondheid? Ze zijn rijk aan vitamine A, C en E én lycopeen. Lycopeen is een antioxidant en beschermt onze cellen tegen schadelijke invloeden. Hoe rijper de tomaat, hoe meer lycopeen!

---

# Kip stroganoff met rijst met paprika en champignons {#kip-stroganoff-met-rijst-met-paprika-en-champignons}

![Kip stroganoff met rijst met paprika en champignons](/receptenboek/assets/images/kip-stroganoff-met-rijst-met-paprika-en-champignons.jpg)

- Totale tijd: 35 min.
- familie, hoofdgerecht, frans.
- Bron: https://www.hellofresh.nl/recipes/kip-stroganoff-met-rijst-61cdc6a194c33e6c0c31d952

## Benodigdheden
2 personen

| Ingredient | Hoeveelheid |
|------------|-------------|
| Ui | 1 stuk(s) |
| Knoflookteen | 1 stuk(s) |
| Paprika | 1.5 stuk(s) |
| Kipfilethaasjes | 2 stuk(s) |
| Tomatenpuree | ½ |
| Champignons | 125 gram |
| Witte langgraanrijst | 170 gram |
| Verse bladpeterselie | 10 gram |
| Biologische zure room | 100 gram |
| Mosterd | 2 tl |
| Rodewijnazijn | 1 el |
| Bloem | 1 el |
| naar smaak Peper en zout |  |
| [Plantaardige] roomboter | 2 el |
| Zoutarm kippenbouillonblokje | ½ stuk(s) |

## 1 Stap 1
- Kook 75 ml water per persoon en voeg daaraan 1/4 kippenbouillonblokje per persoon toe. Snipper de ui. Pers de knoflook of snijd fijn. Snijd de paprika in dunne reepjes. Snijd de kipfilethaasjes in gelijke stukken van ongeveer 2 cm. Tip: Paprika is rijk aan vitamine E - een antioxidant dat je organen, ogen en weefsel beschermt. Je vindt vitamine E ook in volkoren granen, pinda's, zonnebloemolie, zonnebloempitten en groene bladgroenten.

## 2 Stap 2
- Breng ruim water met een snuf zout aan de kook in een pan met deksel voor de rijst. Verhit 1/2 el roomboter per persoon in een hapjespan op middelhoog vuur. Wrijf de kipfilethaasjes in met peper en zout en bak ze in 2 - 3 minuten rondom bruin. Haal uit de pan en bewaar apart (de kip hoeft nog niet gaar te zijn). Voeg de knoflook, ui en paprika toe aan dezelfde hapjespan en bak 3 - 4 minuten.

## 3 Stap 3
- Voeg de tomatenpuree toe aan de hapjespan en bak 2 - 3 minuten. Snijd de champignons in kwarten. Voeg opnieuw 1/2 el roomboter per persoon toe en verhoog het vuur. Voeg de champignons toe en bak nog 4 - 5 minuten. Voeg 1/2 el bloem per persoon toe, meng goed en roerbak 1 minuut.

## 4 Stap 4
- Kook ondertussen de rijst, afgedekt, 12 - 15 minuten. Giet daarna af en laat zonder deksel uitstomen. Hak de bladpeterselie grof.

## 5 Stap 5
- Blus de groenten in de hapjespan af met 1/2 el rodewijnazijn per persoon en voeg de bouillon toe. Verlaag het vuur en roer er de zure room, de helft van de peterselie, 1 tl mosterd per persoon, peper en zout door. Voeg de kipfilethaasjes opnieuw toe en breng zachtjes aan de kook. Laat 5 - 6 minuten sudderen.

## 6 Stap 6
- Verdeel de rijst over de borden. Verdeel de saus met groenten en kip over de rijst en garneer met de overige peterselie.

---

# Kipfilet in spinazie-roomsaus met gebakken aardappelen, wortel en verse kruiden {#kipfilet-in-spinazie-roomsaus-met-gebakken-aardappelen-wortel-en-verse-kruiden}

![Kipfilet in spinazie-roomsaus met gebakken aardappelen, wortel en verse kruiden](/receptenboek/assets/images/kipfilet-in-spinazie-roomsaus-met-gebakken-aardappelen-wortel-en-verse-kruiden.jpg)

- Totale tijd: 50 min.
- caloriebewust, eiwitrijk, hoofdgerecht, frans.
- Bron: https://www.hellofresh.nl/recipes/kipfilet-in-roomsaus-met-spinazie-en-wortel-67911660be277a0e68061a6e

## Benodigdheden
2 personen

| Ingredient | Hoeveelheid |
|------------|-------------|
| Ui | 1 stuk(s) |
| Wortel | 2 stuk(s) |
| Knoflookteen | 2 stuk(s) |
| Aardappelen | 400 gram |
| Kipfilet met mediterrane kruiden | 2 stuk(s) |
| Kookroom | 150 gram |
| Spinazie | 100 gram |
| Verse krulpeterselie en tijm | 10 gram |
| Olijfolie | 1 el |
| Zoutarme kippenbouillon | 200 ml |
| [Plantaardige] roomboter | 2 el |
| Bloem | 1 el |
| naar smaak Peper en zout |  |

## 1 Stap 1
- Bereid de bouillon. Snipper de ui. Snijd de wortel in dunne schijfjes. Pers de knoflook of snijd fijn. Was of schil de aardappelen en snijd in kwarten. Snijd d e peterselie en fijn.

## 2 Stap 2
- Verhit een scheutje olijfolie in een koekenpan met deksel op middelhoog vuur. Bak de aardappelen, afgedekt, 30 - 35 minuten. Haal na 20 minuten het deksel van de pan en schep regelmatig om. Breng op smaak met peper en zout.

## 3 Stap 3
- Verhit een klontje roomboter in een pan op hoog vuur. Bak de kipfilet 2 - 3 minuten per kant. Haal uit de pan en bewaar apart. Bewaar ook de pan met bakvet.

## 4 Stap 4
- V erhit opnieuw een klontje roomboter in dezelfde pan op middelmatig vuur. Bak de ui, knoflook en wortel 3 - 4 minuten. Voeg de bloem toe en bak 1 minuut. Blus af met de bouillon. Voeg de tijmtakjes toe, roer goed door en laat het geheel, afgedekt, 10 minuten sudderen. Voeg de kipfilet toe aan de pan en pocheer 5 - 8 minuten, of tot de kip gaar is.

## 5 Stap 5
- Haal het deksel van de pan en voeg de room en de spinazie toe. Breng op smaak met peper en zout. Roer goed door en laat nog 4 - 6 minuten inkoken zonder deksel. Haal de tijmtakjes uit de pan. Weetje: Spinazie bevat veel voedingsstoffen, waaronder ijzer. IJzer is essentieel voor het vervoeren van zuurstof in ons lichaam, wat bijdraagt aan een energiek gevoel.

## 6 Stap 6
- Verdeel de aardappelen over de borden en schep de kipfilet erbij. Serveer met de romige spinaziesaus en garneer met de peterselie.

---

# Pittige gebakken rijst met kimchi met vissaus, gebakken ei, furikake en sesamzaad {#pittige-gebakken-rijst-met-kimchi-met-vissaus-gebakken-ei-furikake-en-sesamzaad}

![Pittige gebakken rijst met kimchi met vissaus, gebakken ei, furikake en sesamzaad](/receptenboek/assets/images/pittige-gebakken-rijst-met-kimchi-met-vissaus-gebakken-ei-furikake-en-sesamzaad.jpg)

- Totale tijd: 30 min.
- nieuw ingrediënt, veggie, vis & veggie, veggie, pescatarian, hoofdgerecht, koreaans.
- Bron: https://www.hellofresh.nl/recipes/open-briefing-use-nid-kimchi-66d57484946ad7f4e0839b04

## Benodigdheden
2 personen

| Ingredient | Hoeveelheid |
|------------|-------------|
| Basmatirijst | 150 gram |
| Ei | 2 stuk(s) |
| Ui | 1 stuk(s) |
| bosje(s) Bosui | 1 |
| Wortel | 1 stuk(s) |
| Champignons | 125 gram |
| Sesamolie | 10 ml |
| Kimchi | 50 gram |
| Knoflookteen | 2 stuk(s) |
| zakje(s) Furikake | 1 |
| zakje(s) Sesamzaad | 1 |
| Rode peper | ½ stuk(s) |
| Vissaus | 20 ml |
| Zonnebloemolie | 3 el |
| Zoutarm groentebouillonblokje | ¾ stuk(s) |
| Bruine basterdsuiker | 1 el |
| Water | 360 ml |
| [Zoutarme] sojasaus | 1 tl |
| Wittewijnazijn | 1 el |

## 1 Stap 1
- Breng de aangegeven hoeveelheid water aan de kook in een pan. Verkruimel 2/3 van het bouillonblokje erboven. Kook de rijst, afgedekt, 8 minuten. Zet het vuur uit en laat 10 minuten uitstomen. Snijd de bosui in fijne ringen en bewaar het witte en groene gedeelte apart van elkaar. Rasp de wortel en snijd de champignons in plakjes. Snijd de ui in halve ringen. Snijd het steeltje van de rode peper (let op: pittig! Gebruik naar smaak). Rol de peper tussen je handen zodat de zaadjes eruit vallen. Snijd de peper in ringetjes en bewaar een deel apart ter garnering.

## 2 Stap 2
- Verhit 1/3 van de zonnebloemolie in een wok op hoog vuur. Voeg, wanneer de wok goed heet is, het witte gedeelte van de bosui, de ui, champignons, wortel en rode peper toe. Bak 4 - 6 minuten. Haal uit de pan en bewaar apart. Snijd ondertussen de kimchi (let op: pittig! Gebruik naar smaak) grof. Pers de knoflook of snijd fijn.

## 3 Stap 3
- Meng in een kleine kom de knoflook met de kimchi, sojasaus, wittewijnazijn, bruine suiker en vissaus. Voeg het overige bouillonblokje toe en bewaar de saus apart (zie Tip). Verhit opnieuw 1/3 van de zonnebloemolie in een koekenpan op middelhoog vuur en bak het ei. Gezondheidstip: Let jij op je zoutinname? Voeg dan de helft van de vissaus toe. Wie wil kan na het serveren naar smaak meer toevoegen.

## 4 Stap 4
- Verhit de sesamolie en de overige zonnebloemolie in dezelfde wok op hoog vuur. Voeg, wanneer de olie goed heet is, de rijst toe en bak 2 - 3 minuten. Roer zo min mogelijk door de rijst. Voeg de saus toe en bak 1 minuut, zodat de saus licht karamelliseert. Roer vervolgens de groenten erdoor. Serveer de gebakken rijst in kommen en leg het ei erbovenop. Garneer met de bosui, de achtergehouden rode peper, de sesamzaadjes en de furikake.

---

# Sweet & sticky biefstukreepjes met rijst, gebakken groenten en sesamzaadjes {#sweet-en-sticky-biefstukreepjes-met-rijst-gebakken-groenten-en-sesamzaadjes}

![Sweet & sticky biefstukreepjes met rijst, gebakken groenten en sesamzaadjes](/receptenboek/assets/images/sweet-en-sticky-biefstukreepjes-met-rijst-gebakken-groenten-en-sesamzaadjes.jpg)

- Totale tijd: 20 min.
- caloriebewust, lekker snel, eiwitrijk, hoofdgerecht, aziatisch.
- Bron: https://www.hellofresh.nl/recipes/sweet-and-sticky-biefstukreepjes-66d6d702946ad7f4e083b4a6

## Benodigdheden
2 personen

| Ingredient | Hoeveelheid |
|------------|-------------|
| Biefstukreepjes | 200 gram |
| Witte langgraanrijst | 150 gram |
| Uienchutney | 40 gram |
| Wortel | 1 stuk(s) |
| Paksoi | 1 stuk(s) |
| zakje(s) Nasi-bamikruidenmix | 1 |
| Zoete Aziatische saus | 35 gram |
| Paprika | 1 stuk(s) |
| zakje(s) Sesamzaad | 1 |
| Zoutarm groentebouillonblokje | 1 stuk(s) |
| Zonnebloemolie | 1 el |
| [Plantaardige] roomboter | 1 el |
| [Zoutarme] sojasaus | 4 tl |
| Water voor saus | 1 el |
| naar smaak Peper en zout |  |

## 1 Stap 1
- Breng ruim water aan de kook in een pan en verkruimel het bouillonblokje erboven. Kook de rijst 12 - 15 minuten. Giet daarna af en laat uitstomen. Verwijder de steelaanzet van de paksoi, snijd zowel de stelen als het blad van de paksoi klein en houd de stelen apart van de groene bladeren. Snijd de wortel in dunne halve maantjes en snijd de paprika in blokjes.

## 2 Stap 2
- Verhit een sch eutje zonnebloemolie in een wok of hapjespan op middelhoog vuur. Roerbak de wortel, de paprika en de paksoistelen 6 - 8 minuten. Voeg de paksoibladeren, de nasi-bamikruidenmix en de helft van de sojasaus toe. Meng goed en bak 1 minuut. Breng op smaak met peper en zout.

## 3 Stap 3
- Verhit een klontje roomboter in een koekenpan op hoog vuur en bak de biefstukreepjes 1 minuut. Voeg de zoete Aziatische saus, de uienchutney, de aangegeven hoeveelheid water voor de saus en de overige sojasaus toe. Meng goed en bak nog 1 minuut (zie Tip). Breng op smaak met peper. Tip: Voeg sambal naar smaak toe als je het pittiger wilt maken.

## 4 Stap 4
- Serveer de rijst in kommen. Leg alles erbovenop. Besprenkel met de eventuele achtergebleven saus uit de koekenpan. Garneer met de sesamzaadjes.

---

# Tomatenrisotto met garnalen met rucolasalade, basilicum en limoen {#tomatenrisotto-met-garnalen-met-rucolasalade-basilicum-en-limoen}

![Tomatenrisotto met garnalen met rucolasalade, basilicum en limoen](/receptenboek/assets/images/tomatenrisotto-met-garnalen-met-rucolasalade-basilicum-en-limoen.jpg)

- Totale tijd: 35 min.
- caloriebewust, familie, hoofdgerecht, italiaans.
- Bron: https://www.hellofresh.nl/recipes/tomatenrisotto-met-garnalen-685aca005bd0c120800370ad

## Benodigdheden
2 personen

| Ingredient | Hoeveelheid |
|------------|-------------|
| Knoflookteen | 2 stuk(s) |
| Ui | 1 stuk(s) |
| Tomatenpuree | ½ |
| ⅔ blik(ken) Cherrytomaten in blik |  |
| Garnalen | 160 gram |
| Vers basilicum | 5 gram |
| Rucola | 40 gram |
| Risottorijst | 150 gram |
| Limoen | ½ stuk(s) |
| Olijfolie | 2 el |
| Extra vierge olijfolie | 1 tl |
| Zoutarme groentebouillon | 600 ml |
| [Plantaardige] roomboter | 1 el |
| Zwarte balsamicoazijn | 1 el |
| naar smaak Peper en zout |  |

## 1 Stap 1
- Verwarm de oven voor op 200 graden. Bereid de bouillon. Snipper de ui. Pers de knoflook of snijd fijn. Rasp de schil van de limoen en snijd de limoen in 6 partjes. Pers 1 limoenpartje per persoon uit boven een kleine kom. Dep de garnalen droog met keukenpapier en voeg toe aan een kom. Besprenkel met een scheutje olijfolie. Voeg de helft van de knoflook en de helft van de limoenrasp toe. Roer goed door.

## 2 Stap 2
- Verhit een klontje roomboter in een grote pan op middelhoog vuur. Bak de ui en overige de knoflook 1 - 2 minuten. Voeg de risottorijst toe en bak 1 - 2 minuten mee. Voeg de tomatenpuree toe en roer goed door.

## 3 Stap 3
- Voeg 1/3 van de bouillon toe en laat de risottorijst de bouillon langzaam opnemen. Roer regelmatig door. Voeg, zodra de bouillon is opgenomen, weer 1/3 van de bouillon toe en herhaal dit nog 2 keer met de overige bouillon. De risotto is gaar zodra de korrel vanbuiten zacht is en nog een lichte bite heeft vanbinnen. Dit duurt ongeveer 20 - 25 minuten. Kook de risotto langer met meer bouillon als je een zachtere risotto wilt.

## 4 Stap 4
- Giet de cherrytomaten in blik af en voeg toe aan een ovenschaal. Besprenkel met een scheutje olijfolie. Voeg de zwarte balsamicoazijn toe en breng op smaak met peper en zout. Rooster 15 minuten in de oven. Meng ondertussen in een saladekom het limoensap met de rucola en de extra vierge olijfolie. Breng op smaak met peper en zout.

## 5 Stap 5
- Verhit een koekenpan zonder olie op middelhoog vuur. Bak de garnalen in 3 minuten gaar. Haal daarna uit de pan en bewaar apart. Snijd het basilicum fijn en meng in een kom met de overige limoenrasp. Voeg de helft van het kruiden-limoenmengsel toe aan de risotto samen met de kerstomaten en garnalen, inclusief het bakvocht. Roer goed door.

## 6 Stap 6
- Serveer de risotto over de borden. Serveer de rucolasalade ernaast. Garneer met het overige basilicum-limoenmengsel. Serveer met de limoenpartjes.

---

# Tuna melt naanpizza met Siciliaanse kruiden, bieslook en knapperige salade {#tuna-melt-naanpizza-met-siciliaanse-kruiden-bieslook-en-knapperige-salade}

![Tuna melt naanpizza met Siciliaanse kruiden, bieslook en knapperige salade](/receptenboek/assets/images/tuna-melt-naanpizza-met-siciliaanse-kruiden-bieslook-en-knapperige-salade.jpg)

- Totale tijd: 25 min.
- veggie, caloriebewust, vis & veggie, familie, zonder varkensvlees, klaar in 25 minuten, klaar in 15 minuten, original, flexitarisch, extra groente, lekker snel, hoofdgerecht.
- Bron: https://www.hellofresh.nl/recipes/tuna-melt-naanpizza-6894800fcc90c7911daf3083

## Benodigdheden
2 personen

| Ingredient | Hoeveelheid |
|------------|-------------|
| Knoflookteen | 1 stuk(s) |
| blik(ken) Tonijn in water | 1 |
| Naan | 2 stuk(s) |
| Geraspte Goudse kaas | 50 gram |
| Mini-komkommer | 1 stuk(s) |
| Pruimtomaat | 2 stuk(s) |
| Passata | 200 gram |
| zakje(s) Siciliaanse kruidenmix | 1 |
| Rode ui | 1 stuk(s) |
| Verse bieslook | 10 gram |
| Extra vierge olijfolie | 1 el |
| Wittewijnazijn | 1 el |
| Suiker | 2 tl |
| Mosterd | 1 tl |
| Olijfolie | ½ el |
| Zwarte balsamicoazijn | 1 tl |
| naar smaak Peper en zout |  |

## 1 Stap 1
- Verwarm de oven voor op 200 graden. Snijd de ui in halve ringen. Pers de knoflook of snijd fijn. Verhit een klein scheutje olijfolie in een koekenpan op middelhoog vuur. Bak de knoflook, passata, Siciliaanse kruiden, de zwarte balsamicoazijn en de helft van de suiker 4 - 5 minuten. Breng op smaak met peper en zout.

## 2 Stap 2
- Leg ondertussen de naan op een bakplaat met bakpapier en bak 4 - 5 minuten voor in de oven. Laat ondertussen de tonijn uitlekken. Besmeer de naan met de tomatensaus. Beleg met de tonijn en de helft van de ui. Verdeel de geraspte belegen kaas over de naanpizza's. Bak de naanpizza's 5 - 8 minuten in de oven.

## 3 Stap 3
- Snijd ondertussen de komkommer in dunne halve maantjes. Snijd de tomaat in partjes. Snijd de bieslook fijn. Meng in een grote saladekom de wittewijnazijn met de extra vierge olijfolie, de mosterd en de overige suiker. Breng op smaak met peper en zout.

## 4 Stap 4
- Voeg, vlak voor serveren, de tomaat, komkommer en bieslook toe aan de saladekom. Voeg de overige ui toe en meng goed met de dressing. Serveer de naanpizza's met de salade ernaast.

---


<!-- template -->


# Template

- Totale tijd: 0 - 1 min.
- Caloriebewust

## Benodigdheden
4 personen

| Ingredient | Hoeveelheid |
|------------|-------------|
| Aardappelen | 1000 g |


## 1 Voorbereiden




<!-- end of template -->


{::nomarkdown}
<button class="back-to-top" id="backToTop" onclick="scrollToTop()">↑</button>

<script>
// Show/hide back to top button
window.onscroll = function() {
  const button = document.getElementById('backToTop');
  if (document.body.scrollTop > 300 || document.documentElement.scrollTop > 300) {
    button.style.display = 'block';
  } else {
    button.style.display = 'none';
  }
};

function scrollToTop() {
  document.body.scrollTop = 0;
  document.documentElement.scrollTop = 0;
}

// Enhanced search functionality
function filterRecipes() {
  const searchTerm = document.getElementById('recipeSearch').value.toLowerCase();
  const recipeCards = document.querySelectorAll('.recipe-card');
  const recipeHeaders = document.querySelectorAll('h1');

  // Filter recipe cards
  recipeCards.forEach(card => {
    const title = card.querySelector('h3 a').textContent.toLowerCase();
    const tags = Array.from(card.querySelectorAll('.recipe-tag')).map(tag => tag.textContent.toLowerCase()).join(' ');
    const searchText = title + ' ' + tags;

    if (searchText.includes(searchTerm)) {
      card.style.display = 'block';
    } else {
      card.style.display = 'none';
    }
  });

  // Filter recipe sections if searching
  if (searchTerm && searchTerm.length > 2) {
    recipeHeaders.forEach(header => {
      const title = header.textContent.toLowerCase();
      let recipeSection = header;
      let nextElement = header.nextElementSibling;
      let recipeContent = title;

      // Collect content until next h1 or hr
      while (nextElement && nextElement.tagName !== 'H1' && nextElement.tagName !== 'HR') {
        recipeContent += ' ' + nextElement.textContent.toLowerCase();
        nextElement = nextElement.nextElementSibling;
      }

      if (title.includes(searchTerm) || recipeContent.includes(searchTerm)) {
        // Show this recipe section
        let element = header;
        while (element && element.tagName !== 'HR') {
          element.style.display = 'block';
          element = element.nextElementSibling;
        }
        if (element && element.tagName === 'HR') {
          element.style.display = 'block';
        }
      } else {
        // Hide this recipe section
        let element = header;
        while (element && element.tagName !== 'HR') {
          element.style.display = 'none';
          element = element.nextElementSibling;
        }
        if (element && element.tagName === 'HR') {
          element.style.display = 'none';
        }
      }
    });
  } else {
    // Show all recipe sections when not searching
    recipeHeaders.forEach(header => {
      let element = header;
      while (element && element.tagName !== 'HR') {
        element.style.display = 'block';
        element = element.nextElementSibling;
      }
      if (element && element.tagName === 'HR') {
        element.style.display = 'block';
      }
    });
  }
}
</script>
{:/}
