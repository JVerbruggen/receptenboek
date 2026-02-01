---
layout: default
title: Receptenboek 2026
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

# Receptenboek 2026

*Laatst bijgewerkt: {{ site.time | date: "%B %d, %Y" }}*

---

Welkom bij mijn collectie van heerlijke recepten! Hier vind je een uitgebreide verzameling van gerechten die ik heb uitgeprobeerd en verzameld.

{::nomarkdown}
<input type="text" class="search-box" id="recipeSearch" placeholder="🔍 Zoek recepten..." onkeyup="filterRecipes()">

<div class="recipe-grid" id="recipeGrid">
  <!-- Cards will be rendered here by JS -->
</div>

<script>
let allRecipes = [];
let cardsBySlug = new Map();
let sectionsBySlug = new Map();
let hrsBySlug = new Map();

const BASEURL = '{{ site.baseurl }}' || '';

function withBaseUrl(path) {
  if (!path) return path;
  const p = String(path);
  if (/^https?:\/\//i.test(p)) return p;
  if (BASEURL && p.startsWith(BASEURL + '/')) return p;
  // Legacy hard-coded base path
  if (p.startsWith('/receptenboek/')) return BASEURL + p.slice('/receptenboek'.length);
  if (p.startsWith('/')) return BASEURL + p;
  return BASEURL + '/' + p;
}

function recipeSearchText(recipe, includeContent) {
  const parts = [];
  parts.push(String(recipe?.title || ''));
  parts.push(String(recipe?.time || ''));
  parts.push(Array.isArray(recipe?.tags) ? recipe.tags.join(' ') : '');

  if (includeContent) {
    if (Array.isArray(recipe?.ingredients)) {
      parts.push(
        recipe.ingredients
          .map(i => `${String(i?.name || '')} ${String(i?.amount || '')}`)
          .join(' ')
      );
    }

    if (Array.isArray(recipe?.steps)) {
      const stepParts = [];
      recipe.steps.forEach(s => {
        if (typeof s === 'string') {
          stepParts.push(s);
          return;
        }
        stepParts.push(String(s?.title || ''));
        if (Array.isArray(s?.items)) stepParts.push(s.items.join(' '));
      });
      parts.push(stepParts.join(' '));
    }
  }

  return parts.join(' ').toLowerCase();
}

function renderCards(recipes) {
  const grid = document.getElementById('recipeGrid');
  if (!grid) return;

  cardsBySlug = new Map();
  grid.innerHTML = '';

  recipes.forEach(r => {
    const card = document.createElement('div');
    card.className = 'recipe-card';
    card.dataset.slug = r.slug;

    const placeholder = withBaseUrl('/assets/images/placeholder.svg');

    const img = document.createElement('img');
    img.className = 'recipe-card-image';
    img.src = withBaseUrl(r.image) || placeholder;
    img.alt = r.title;
    img.onerror = () => (img.src = placeholder);

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

    if (r.slug) cardsBySlug.set(r.slug, card);
  });
}

function renderRecipeSections(recipes) {
  const container = document.getElementById('recipeSections');
  if (!container) return;

  sectionsBySlug = new Map();
  hrsBySlug = new Map();
  container.innerHTML = '';

  recipes.forEach(r => {
    const section = document.createElement('section');
    section.dataset.slug = r.slug;
    section.id = r.slug;

    const h1 = document.createElement('h1');
    h1.textContent = r.title || 'Recept';
    section.appendChild(h1);

    const placeholder = withBaseUrl('/assets/images/placeholder.svg');

    const img = document.createElement('img');
    img.src = withBaseUrl(r.image) || placeholder;
    img.alt = r.title || 'Recept afbeelding';
    img.onerror = () => (img.src = placeholder);
    section.appendChild(img);

    const metaList = document.createElement('ul');
    if (r.time) {
      const li = document.createElement('li');
      li.textContent = 'Totale tijd: ' + r.time;
      metaList.appendChild(li);
    }
    if (Array.isArray(r.tags) && r.tags.length) {
      const li = document.createElement('li');
      li.textContent = 'Tags: ' + r.tags.join(', ');
      metaList.appendChild(li);
    }
    if (r.source) {
      const li = document.createElement('li');
      li.appendChild(document.createTextNode('Bron: '));
      const a = document.createElement('a');
      a.href = r.source;
      a.textContent = r.source;
      a.rel = 'noopener noreferrer';
      a.target = '_blank';
      li.appendChild(a);
      metaList.appendChild(li);
    }
    if (r.servings_text || r.servings) {
      const li = document.createElement('li');
      li.textContent = r.servings_text || `${r.servings} personen`;
      metaList.appendChild(li);
    }
    if (metaList.childElementCount) section.appendChild(metaList);

    const hasIngredients = Array.isArray(r.ingredients) && r.ingredients.length;
    const hasSteps = Array.isArray(r.steps) && r.steps.length;

    if (hasIngredients) {
      const h2 = document.createElement('h2');
      h2.textContent = 'Benodigdheden';
      section.appendChild(h2);

      const table = document.createElement('table');
      const thead = document.createElement('thead');
      const headRow = document.createElement('tr');
      const th1 = document.createElement('th');
      th1.textContent = 'Ingredient';
      const th2 = document.createElement('th');
      th2.textContent = 'Hoeveelheid';
      headRow.appendChild(th1);
      headRow.appendChild(th2);
      thead.appendChild(headRow);
      table.appendChild(thead);

      const tbody = document.createElement('tbody');
      r.ingredients.forEach(i => {
        const row = document.createElement('tr');
        const td1 = document.createElement('td');
        td1.textContent = String(i?.name || '');
        const td2 = document.createElement('td');
        td2.textContent = String(i?.amount || '');
        row.appendChild(td1);
        row.appendChild(td2);
        tbody.appendChild(row);
      });
      table.appendChild(tbody);
      section.appendChild(table);
    }

    if (hasSteps) {
      r.steps.forEach(s => {
        if (typeof s === 'string') {
          const p = document.createElement('p');
          p.textContent = s;
          section.appendChild(p);
          return;
        }

        const h2 = document.createElement('h2');
        h2.textContent = String(s?.title || '');
        section.appendChild(h2);

        if (Array.isArray(s?.items) && s.items.length) {
          const ul = document.createElement('ul');
          s.items.forEach(item => {
            const li = document.createElement('li');
            li.textContent = String(item || '');
            ul.appendChild(li);
          });
          section.appendChild(ul);
        }
      });
    }

    if (!hasIngredients && !hasSteps) {
      const p = document.createElement('p');
      p.innerHTML = '<em>Geen details beschikbaar.</em>';
      section.appendChild(p);
    }

    container.appendChild(section);
    const hr = document.createElement('hr');
    container.appendChild(hr);

    if (r.slug) {
      sectionsBySlug.set(r.slug, section);
      hrsBySlug.set(r.slug, hr);
    }
  });
}

// Fetch recipes.json and render cards + sections
async function loadRecipes() {
  try {
    const res = await fetch(withBaseUrl('/assets/recipes.json'));
    if (!res.ok) throw new Error('Failed to load recipes.json');
    allRecipes = await res.json();
    renderCards(allRecipes);
    renderRecipeSections(allRecipes);
    filterRecipes();
  } catch (err) {
    console.error(err);
    const grid = document.getElementById('recipeGrid');
    if (grid) grid.textContent = 'Kan recepten niet laden.';
  }
}

function filterRecipes() {
  const searchTerm = (document.getElementById('recipeSearch')?.value || '').toLowerCase();
  const includeContent = Boolean(searchTerm) && searchTerm.length > 2;

  allRecipes.forEach(r => {
    const match = !searchTerm || recipeSearchText(r, includeContent).includes(searchTerm);

    const card = cardsBySlug.get(r.slug);
    if (card) card.style.display = match ? 'block' : 'none';

    const section = sectionsBySlug.get(r.slug);
    const hr = hrsBySlug.get(r.slug);
    if (section) section.style.display = match ? 'block' : 'none';
    if (hr) hr.style.display = match ? 'block' : 'none';
  });
}

window.addEventListener('DOMContentLoaded', loadRecipes);
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

{::nomarkdown}
<div id="recipeSections">
  <!-- Recipe sections will be rendered here by JS -->
</div>
{:/}




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
</script>
{:/}
