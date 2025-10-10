# Receptenboek 2025

Een persoonlijke collectie van heerlijke recepten, automatisch gepubliceerd op GitHub Pages.

## 🌐 Live Website

Deze receptencollectie is beschikbaar op: [https://jverbruggen.github.io/receptenboek](https://jverbruggen.github.io/receptenboek)

## 📁 Bestandsstructuur

- `Recepten2025.md` - Het hoofdbestand met alle recepten in Markdown formaat
- `_config.yml` - Jekyll configuratie voor GitHub Pages
- `.github/workflows/deploy.yml` - GitHub Actions workflow voor automatische deployment
- `index.md` - Homepage van de website

## 🚀 GitHub Pages Setup

Deze repository is geconfigureerd voor automatische deployment naar GitHub Pages:

1. **GitHub Actions**: Elke push naar de `main` branch triggert automatisch een nieuwe deployment
2. **Jekyll**: De site wordt gebouwd met Jekyll voor mooie opmaak
3. **Responsive Design**: Gebruikt het Minima theme voor een clean, mobiel-vriendelijke interface

## 📝 Recepten Toevoegen

Recepten kunnen worden toegevoegd aan het `Recepten2025.md` bestand in het volgende formaat:

```markdown
<details>
<summary>Recept Naam</summary>

# Recept Naam

- Totale tijd: X min.
- Labels (bijv. Caloriebewust, Veggie, Familie)

## Benodigdheden
4 personen

| Ingredient | Hoeveelheid |
|------------|-------------|
| Ingredient 1 | Hoeveelheid |

## 1 Stap 1
Beschrijving van de eerste stap...

## 2 Stap 2
Beschrijving van de tweede stap...

</details>
```

## 🛠️ Lokale Development

Om de site lokaal te draaien:

```bash
# Installeer Jekyll
gem install jekyll bundler

# Clone de repository
git clone https://github.com/JVerbruggen/receptenboek.git
cd receptenboek

# Draai de lokale server
bundle exec jekyll serve
```

De site zal dan beschikbaar zijn op `http://localhost:4000/receptenboek/`

## 📱 Features

- **Responsive Design**: Werkt goed op desktop, tablet en mobiel
- **Zoekfunctionaliteit**: Recepten zijn makkelijk doorzoekbaar
- **Automatische Updates**: Nieuwe recepten verschijnen automatisch online na een push
- **Clean Interface**: Overzichtelijke presentatie van alle recepten

---

*Gemaakt met ❤️ en Jekyll*