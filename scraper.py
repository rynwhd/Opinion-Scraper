from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException,ElementClickInterceptedException
from bs4 import BeautifulSoup
import time
from rapidfuzz.process import extract
import json
import http.client
from selenium.webdriver.chrome.options import Options as ChromeOptions

## function to translate es to en
def translate_text(text, source_lang='es', target_lang='en'): 
    conn = http.client.HTTPSConnection("rapid-translate-multi-traduction.p.rapidapi.com")

    payload = json.dumps({
        "from": source_lang,
        "to": target_lang,
        "q": text
    }).encode('utf-8')  # Ensure UTF-8 encoding

    headers = {
    'x-rapidapi-key': "9710953fc1msh977a9cc27b72083p1d52afjsnee668c74545f",
    'x-rapidapi-host': "rapid-translate-multi-traduction.p.rapidapi.com",
    'Content-Type': "application/json"
    }

    conn.request("POST", "/t", payload, headers)

    res = conn.getresponse()
    data = res.read() # response from api

    return data.decode("utf-8") #check different latin encoding

#setting up options for ChromeDriver
options = ChromeOptions()
options.set_capability('sessionName', 'BStack Sample Test')
driver = webdriver.Chrome()

# 1. Open El País website
driver.get("https://elpais.com")
time.sleep(1)  # Wait for page to load

# 2. Checking for Pop Up on Home Page
try:
    popup_close_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Aceptar') or contains(text(), 'Close')]")
    popup_close_button.click()
    time.sleep(1)
except NoSuchElementException:
    pass  # No popup detected

time.sleep(1)

# 3. Navigate to the Opinion section
try:
    opinion_section = driver.find_element(By.XPATH, "//a[contains(text(), 'Opinión')]")
    driver.execute_script("arguments[0].scrollIntoView(true);", opinion_section)
    driver.execute_script("arguments[0].click();", opinion_section)
    time.sleep(1)
except ElementClickInterceptedException:
    print("Element click intercepted. Trying JavaScript click.")
    driver.execute_script("arguments[0].click();", opinion_section)
    time.sleep(1)

#Extracting Article Links 
print(" Extract article details")
soup = BeautifulSoup(driver.page_source, 'html.parser')
articles = soup.find_all('article', limit=5)
print(type(articles))

#Checking if Articles ResultSet is retrieved, setting test status as passed for BS dashboard
if articles:
        # Set the status of test as 'passed' if articles are recovered
        driver.execute_script(
            'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "articles recovered"}}')
else:
        # Set the status of test as 'failed' if articles not recovered
        driver.execute_script(
            'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "articles not recovered"}}')

print(" Function Call to translate text using Rapid Translate Multi Traduction API") #for each article in the result set, individual calls will be made to retrieve complete article title


article_data = [] 

for article in articles:
    # Extract title
    title_tag = article.find('h2')
    title = title_tag.text.strip() if title_tag else "No Title"

    # Translate title to English
    translated_title = translate_text(title)

    # Extract content
    link_tag = article.find('a')
    article_url = link_tag['href'] if link_tag else ""

    driver.get(article_url)
    time.sleep(3)

    # Check for popup in article page
    try:
        popup_close_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Aceptar') or contains(text(), 'Close')]")
        popup_close_button.click()
        time.sleep(2)
    except NoSuchElementException:
        pass  # No popup detected

    article_soup = BeautifulSoup(driver.page_source, 'html.parser')
    paragraphs = article_soup.find_all('p')
    content = ' '.join([p.text for p in paragraphs])

    article_data.append({
        "title": title,
        "translated_title": translated_title,
        "content": content
    })

# Close the driver
driver.quit()

# Print results
print("Article Details:")
for data in article_data:
    print(f"Title (ES): {data['title']}")
    print(f"Title (EN): {data['translated_title']}")
    print('-' * 80)

# Analyze Translated Headers
word_count = {}
for data in article_data:
    words = data['translated_title'].split()
    for word in words:
        word = word.lower()
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

#Check reptition in the words and print count of items with value greater than 2
repeated_words = {k: v for k, v in word_count.items() if v > 2}
print("Repeated Words in Translated Headers:")
print(repeated_words)
