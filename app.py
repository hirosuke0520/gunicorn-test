from flask import Flask
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

app = Flask(__name__)


@app.route("/")
def index():
    URL = 'https://tonari-it.com/scraping-test/'
    options = webdriver.ChromeOptions()
    options.add_argument('--no-sandbox')
    options.add_argument('--headless')
    options.add_argument('--disable-dev-shm-usage')
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.get(URL)
    driver.implicitly_wait(5)
    element = driver.find_element(By.CSS_SELECTOR, "#hoge")
    return element.text


if __name__ == "__main__":
    app.run()
