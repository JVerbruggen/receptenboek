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
  padding: 1rem;
  background: #f9f9f9;
  transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.recipe-card:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(0,0,0,0.1);
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

Welkom bij mijn collectie van heerlijke recepten! Hier vind je een uitgebreide verzameling van gerechten die ik heb uitgeprobeerd en verzameld.

<input type="text" class="search-box" id="recipeSearch" placeholder="🔍 Zoek recepten..." onkeyup="filterRecipes()">

<div class="recipe-grid" id="recipeGrid">
  <div class="recipe-card">
    <h3><a href="#krieltjessalade-met-mediterrane-kipfilet">Krieltjessalade met Mediterrane kipfilet</a></h3>
    <div class="recipe-meta">⏰ 20-25 min</div>
    <div class="recipe-tags">
      <span class="recipe-tag">Lekker snel</span>
      <span class="recipe-tag">Caloriebewust</span>
      <span class="recipe-tag">Familie</span>
    </div>
  </div>

  <div class="recipe-card">
    <h3><a href="#piri-piri-garnalen-met-tomatensalsa">Piri-piri garnalen met tomatensalsa</a></h3>
    <div class="recipe-meta">⏰ 25-30 min</div>
    <div class="recipe-tags">
      <span class="recipe-tag">Lekker snel</span>
      <span class="recipe-tag">Caloriebewust</span>
    </div>
  </div>

  <div class="recipe-card">
    <h3><a href="#aubergine-fatteh-met-krokante-kikkererwten">Aubergine fatteh met krokante kikkererwten</a></h3>
    <div class="recipe-meta">⏰ 25-30 min</div>
    <div class="recipe-tags">
      <span class="recipe-tag">Lekker snel</span>
      <span class="recipe-tag">Caloriebewust</span>
      <span class="recipe-tag">Veggie</span>
    </div>
  </div>

  <div class="recipe-card">
    <h3><a href="#mujaddara-met-harissa-cherrytomaten-en-komkommeryoghurt">Mujaddara met harissa, cherrytomaten en komkommeryoghurt</a></h3>
    <div class="recipe-meta">⏰ 25-30 min</div>
    <div class="recipe-tags">
      <span class="recipe-tag">Lekker snel</span>
      <span class="recipe-tag">Caloriebewust</span>
      <span class="recipe-tag">Veggie</span>
    </div>
  </div>

  <div class="recipe-card">
    <h3><a href="#bulgur-met-harissa-portobello-knapperige-kikkererwten-en-tomaat-komkommersalade">Bulgur met harissa-portobello</a></h3>
    <div class="recipe-meta">⏰ 25-30 min</div>
    <div class="recipe-tags">
      <span class="recipe-tag">Lekker snel</span>
      <span class="recipe-tag">Caloriebewust</span>
      <span class="recipe-tag">Veggie</span>
    </div>
  </div>

  <div class="recipe-card">
    <h3><a href="#linguine-met-grote-garnalen">Linguine met grote garnalen</a></h3>
    <div class="recipe-meta">⏰ 35-45 min</div>
    <div class="recipe-tags">
      <span class="recipe-tag">Caloriebewust</span>
      <span class="recipe-tag">Familie</span>
    </div>
  </div>

  <div class="recipe-card">
    <h3><a href="#parelcouscous-met-chorizo-en-courgette">Parelcouscous met chorizo en courgette</a></h3>
    <div class="recipe-meta">⏰ 20-25 min</div>
    <div class="recipe-tags">
      <span class="recipe-tag">Lekker snel</span>
      <span class="recipe-tag">Caloriebewust</span>
    </div>
  </div>

  <div class="recipe-card">
    <h3><a href="#burger-met-aardappelpartjes-en-champignons">Burger met aardappelpartjes en champignons</a></h3>
    <div class="recipe-meta">⏰ 35-45 min</div>
    <div class="recipe-tags">
      <span class="recipe-tag">Caloriebewust</span>
    </div>
  </div>

  <div class="recipe-card">
    <h3><a href="#fusion-risotto-met-misopaddenstoelen-en-paksoi">Fusion risotto met misopaddenstoelen en paksoi</a></h3>
    <div class="recipe-meta">⏰ 35-45 min</div>
    <div class="recipe-tags">
      <span class="recipe-tag">Caloriebewust</span>
    </div>
  </div>

  <div class="recipe-card">
    <h3><a href="#zoete-aardappelstoof-met-zure-room-en-jalapeño">Zoete-aardappelstoof met zure room en jalapeño</a></h3>
    <div class="recipe-meta">⏰ 25-30 min</div>
    <div class="recipe-tags">
      <span class="recipe-tag">Caloriebewust</span>
    </div>
  </div>

  <div class="recipe-card">
    <h3><a href="#linzencurry-met-zoete-aardappel-en-naan">Linzencurry met zoete aardappel en naan</a></h3>
    <div class="recipe-meta">⏰ 35-45 min</div>
    <div class="recipe-tags">
      <span class="recipe-tag">Caloriebewust</span>
      <span class="recipe-tag">Veggie</span>
    </div>
  </div>

  <div class="recipe-card">
    <h3><a href="#honing-mosterd-zalm-met-geroosterde-krieltjes">Honing mosterd zalm met geroosterde krieltjes</a></h3>
    <div class="recipe-meta">⏰ 40 min</div>
    <div class="recipe-tags">
      <span class="recipe-tag">Caloriebewust</span>
      <span class="recipe-tag">Familie</span>
      <span class="recipe-tag">Extra groente</span>
    </div>
  </div>

  <div class="recipe-card">
    <h3><a href="#sweet--sticky-rundergehaktballetjes">Sweet & sticky rundergehaktballetjes</a></h3>
    <div class="recipe-meta">⏰ 25 min</div>
    <div class="recipe-tags">
      <span class="recipe-tag">Caloriebewust</span>
      <span class="recipe-tag">Familie</span>
    </div>
  </div>

  <div class="recipe-card">
    <h3><a href="#eén-pot-spaghetti-met-tomatensaus">Eén-pot-spaghetti met tomatensaus</a></h3>
    <div class="recipe-meta">⏰ 25 min</div>
    <div class="recipe-tags">
      <span class="recipe-tag">Caloriebewust</span>
      <span class="recipe-tag">Veggie</span>
      <span class="recipe-tag">Extra groente</span>
    </div>
  </div>

  <div class="recipe-card">
    <h3><a href="#rijstbowl-met-gebakken-ei-en-zoete-aziatische-saus">Rijstbowl met gebakken ei en zoete Aziatische saus</a></h3>
    <div class="recipe-meta">⏰ 25 min</div>
    <div class="recipe-tags">
      <span class="recipe-tag">Veggie</span>
    </div>
  </div>

  <div class="recipe-card">
    <h3><a href="#spaghetti-met-champignonroomsaus-en-spekjes">Spaghetti met champignonroomsaus en spekjes</a></h3>
    <div class="recipe-meta">⏰ 30 min</div>
    <div class="recipe-tags">
    </div>
  </div>

  <div class="recipe-card">
    <h3><a href="#kipfilet-in-spinazie-roomsaus">Kipfilet in spinazie-roomsaus</a></h3>
    <div class="recipe-meta">⏰ 50 min</div>
    <div class="recipe-tags">
      <span class="recipe-tag">Caloriebewust</span>
      <span class="recipe-tag">Eiwitrijk</span>
    </div>
  </div>
</div>

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

---

*Laatst bijgewerkt: {{ site.time | date: "%B %d, %Y" }}*

