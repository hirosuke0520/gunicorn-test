from flask import Flask, request, jsonify
from bs4 import BeautifulSoup
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
    
    options = webdriver.ChromeOptions()
    options.add_argument('--no-sandbox')
    options.add_argument('--headless')
    options.add_argument('--disable-dev-shm-usage')
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    profiles = []
    for user_id in user_ids:
        url = f"https://www.tiktok.com/@{user_id}"
        driver.get(url)
        driver.implicitly_wait(5)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        profile_info = {
            "userId": user_id,
            # "userSubtitle": get_text_from_elements(soup, "data-e2e", "user-subtitle"),
            # "followersCount": get_text_from_elements(soup, "data-e2e", "followers-count"),
            # "likesCount": get_text_from_elements(soup, "data-e2e", "likes-count"),
        }
        
        profiles.append({user_id: profile_info})

    return jsonify(profiles)


if __name__ == "__main__":
    app.run()
