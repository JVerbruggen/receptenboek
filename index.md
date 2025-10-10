---
layout: default
title: Receptenboek 2025
---

<style>
.recipe-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 1.5rem;
  margin: 2rem 0;
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

Hieronder vind je de volledige receptencollectie uit mijn kookboek:

{% include_relative Recepten2025.md %}

---

*Laatst bijgewerkt: {{ site.time | date: "%B %d, %Y" }}*