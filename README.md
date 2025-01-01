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
Title (ES): "El cambio climático y las ciudades"
Title (EN): "Climate Change and Cities"
--------------------------------------------------------------------------------
```

### Repeated Words in Translated Headers
```text
{'climate': 3, 'change': 2}
```

---

## Customization

- **Image Download**: Uncomment the image extraction and download section in the code to save images locally.
- **Section Limit**: Adjust the `limit=20` parameter in the BeautifulSoup `find_all` call to scrape more or fewer articles.

---

## Known Issues

1. Popups on the El País website may vary; the script handles common cases but might require adjustments for new popups.
2. Translation accuracy depends on the Rapid Translate API.

---
