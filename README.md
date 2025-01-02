# El País Opinion Article Scraper

This Python script uses Selenium and BeautifulSoup to scrape the latest opinion articles from the El País website, translate their titles from Spanish to English using the Rapid Translate Multi Traduction API, and analyze the translated headers for repeated words. The program also collects the article content for further use.

---

## Features

- **Automated Web Scraping**: Navigates to the El País Opinion section, handles popups, and collects article titles and content.
- **Title Translation**: Uses the Rapid Translate Multi Traduction API to translate Spanish titles to English.
- **Word Analysis**: Analyzes the translated titles to find repeated words.
- **Optional Image Download**: (Commented out in code) Capability to extract and download article images.

---

## Requirements

### Libraries

Ensure you have the following Python libraries installed:

- `selenium`
- `beautifulsoup4`
- `rapidfuzz`
- `http.client`
- `json`

### WebDriver

Install the appropriate version of [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/) for your Chrome browser version and add it to your system path.

---

## Installation

### Step 1: Clone the repository
```bash
git clone https://github.com/rynwhd/opinion-scraper.git
cd el-pais-opinion-scraper
```

### Step 2: Create a virtual environment (optional)
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

### Step 3: Install dependencies
```bash
pip install selenium beautifulsoup4 rapidfuzz
```

### Step 4: Add your API key
Replace the placeholder  "'x-rapidapi-key':" in the code with your actual API key for the Rapid Translate Multi Traduction API.

---

## Usage

### Step 1: Run the script
```bash
python scraper.py
```

### Step 2: Script workflow

The script will:
- Open the El País website.
- Navigate to the Opinion section.
- Extract titles, content, and translate titles.
- Print the results and analyze repeated words in the translated titles.

### Step 3: Review output

Check the console output for:
- Scraped article data.
- Repeated word analysis in translated titles.

---

## Sample Output

### Article Details
```text
Title (ES): El año de todos los peligros
Title (EN): ["The year of all dangers"]
--------------------------------------------------------------------------------
Title (ES): Cinco años con covid
Title (EN): ["Five years with Covid"]
--------------------------------------------------------------------------------
Title (ES): Fotos con Carter
Title (EN): ["Photos with Carter"]
--------------------------------------------------------------------------------
Title (ES): Alice Munro y el hombre del saco
Title (EN): ["Alice Munro and the man in the bag"]
--------------------------------------------------------------------------------
Title (ES): ‘Bonanza (La Línea de la Concepción)’
Title (EN): ["‘Bonanza (the line of conception)’"]
--------------------------------------------------------------------------------
Title (ES): Kafka no te suelta
Title (EN): ["Kafka doesn't let go"]
--------------------------------------------------------------------------------
Title (ES): Polarización ideológica en América Latina y el Caribe
Title (EN): ["Ideological polarization in Latin America and the Caribbean"]
--------------------------------------------------------------------------------
Title (ES): Otro año más
Title (EN): ["Another year"]
--------------------------------------------------------------------------------
Title (ES): Ayuso y Sánchez deberían dar las uvas juntos
Title (EN): ["Ayuso and Sánchez should give grapes together"]
--------------------------------------------------------------------------------
Title (ES): Un año sin química en el cine
Title (EN): ["A year without chemistry in the cinema"]
--------------------------------------------------------------------------------
Title (ES): Oncobierzo
Title (EN): ["Oncobierzo"]
--------------------------------------------------------------------------------
Title (ES): Nicaragua, dictadura por ley
Title (EN): ["Nicaragua, dictatorship by law"]
--------------------------------------------------------------------------------
Title (ES): Blindaje constitucional de derechos: deseo y realidad
Title (EN): ["Constitutional rights shielding: desire and reality"]
--------------------------------------------------------------------------------
Title (ES): El impacto económico real que tendrá la dana
Title (EN): ["The real economic impact that the Dana will have"]
--------------------------------------------------------------------------------
Title (ES): Entre armiños y pelucas: la reforma de la Cámara de los Lores
Title (EN): ["Between armies and wigs: the reform of the House of Lores"]
--------------------------------------------------------------------------------
Title (ES): El Roto
Title (EN): ["The broken"]
--------------------------------------------------------------------------------
Title (ES): Flavita Banana
Title (EN): ["Flavita Banana"]
--------------------------------------------------------------------------------
Title (ES): Riki Blanco
Title (EN): ["White Riki"]
--------------------------------------------------------------------------------
Title (ES): Peridis
Title (EN): ["PERIDIS"]
--------------------------------------------------------------------------------
Title (ES): Sciammarella
Title (EN): ["Sciammarella"]
```

### Repeated Words in Translated Headers
```text
{'["the': 3, 'of': 4, 'and': 5, 'the': 7, 'in': 3}
```
