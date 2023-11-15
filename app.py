from flask import Flask, request, jsonify
# from tiktok_scraping import get_tiktok_profile_by_selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

app = Flask(__name__)


@app.route("/")
def index():
    args_user_ids = request.args.get('user_ids')
    user_ids = []
    if args_user_ids:
        user_ids = args_user_ids.split(',')  # カンマ区切りのuser_idを分割
    
    # profiles = [get_tiktok_profile_by_selenium(user_id) for user_id in user_ids]

    options = webdriver.ChromeOptions()
    options.add_argument('--no-sandbox')
    options.add_argument('--headless')
    options.add_argument('--disable-dev-shm-usage')
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    profiles = []
    for user_id in user_ids:
        URL = 'https://tonari-it.com/scraping-test/'
        driver.get(URL)
        driver.implicitly_wait(5)
        element = driver.find_element(By.CSS_SELECTOR, "#hoge")
        profiles.append({user_id: user_id})

    return jsonify(profiles)


if __name__ == "__main__":
    app.run()
