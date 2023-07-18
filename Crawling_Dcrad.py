import undetected_chromedriver as uc
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import random

def initialize_driver():
    driver = uc.Chrome()
    actions = ActionChains(driver)
    return driver, actions

def scroll_down_page(driver, actions, iterations):
    for _ in range(iterations):
        sleep(random.random()*3)
        for _ in range(4):
            actions.send_keys(Keys.ARROW_DOWN).perform()

def scrape_articles(driver):
    wait = WebDriverWait(driver, 40)
    articles = wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, "article")))
    urls = [article.find_element(By.TAG_NAME, "a").get_attribute("href") for article in articles] #fetch url 
    return urls

def scrape_article_details(driver, urls):
    posts = []
    for url in urls:
        sleep(random.random()*3)
        driver.get(url)
        wait = WebDriverWait(driver, 40)
        article = wait.until(EC.presence_of_element_located((By.TAG_NAME, "article")))
        h1 = article.find_element(By.TAG_NAME, "h1")
        timestamp = article.find_element(By.TAG_NAME, "time").get_attribute("datetime")
        texts = article.find_elements(By.TAG_NAME, "span")
        content = ""
        for j in range(len(texts)):
            content += texts[j].text
        posts.append({"title": h1.text, "url": url, "content": content, "timestamp": timestamp})
    return posts

def save_to_csv(data, filename):
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)
    print(df.head())

def main(query):
    driver, actions = initialize_driver()
    driver.get(f"https://www.dcard.tw/search?query={query}")
    sleep(3)

    urls = set()
    for _ in range(10):  # Adjust this range as needed
        scroll_down_page(driver, actions, 1)
        new_urls = scrape_articles(driver)
        urls.update(new_urls)
        sleep(2)  # Adjust this sleep time as needed

    posts = scrape_article_details(driver, urls)
    driver.close()
    save_to_csv(posts, 'dcard_posts.csv')

# Call the main function with the search query
main("疫苗副作用") #Change this Keyword to query the data you want





