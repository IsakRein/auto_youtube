import requests
import json
import os
from gtts import gTTS

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


class Webscraper:
    def __init__(self) -> None:
        self.base_url = "https://oauth.reddit.com/"
        secret = json.load(open("secret.json", "r"))

        self.auth = requests.auth.HTTPBasicAuth(
            secret["client"], secret["token"])
        self.data = {'grant_type': 'password',
                     'username': secret["user_name"],
                     'password': secret["password"]}

        self.authenticate()

    def authenticate(self) -> None:
        headers = {'User-Agent': 'MyBot/0.0.1'}
        res = requests.post('https://www.reddit.com/api/v1/access_token',
                            auth=self.auth, data=self.data, headers=headers)
        self.TOKEN = res.json()['access_token']

        self.headers = {**headers, **{'Authorization': f"bearer {self.TOKEN}"}}

    def get_posts(self, url: str):
        res = requests.get(self.base_url + url, headers=self.headers)
        return [post['data'] for post in res.json()["data"]["children"]]

    def get_todays_url(self) -> str:
        post = self.get_posts("r/Askreddit/top/?t=day")[0]
        url = post["url"].split("reddit.com/")[1]
        return url

    def clear_data(self):
        os.system("rm -r data")
        os.system("mkdir data")
        os.system("mkdir data/img")
        os.system("mkdir data/audio")

    def get_data(self, url):
        data = {}
        data["title"] = {}
        data["comments"] = []

        img_folder = "./data/img/"
        audio_folder = "./data/audio/"

        # Driver init
        ser = Service("./chromedriver")
        op = webdriver.ChromeOptions()
        prefs = {"profile.default_content_setting_values.notifications": 2}
        op.add_experimental_option("prefs", prefs)
        driver = webdriver.Chrome(service=ser, options=op)

        # Get url
        driver.get(url)
        driver.maximize_window()

        # Click NSFW button
        try:
            nsfw_button = driver.find_element(
                By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[2]/button"
            )
            nsfw_button.click()
            nsfw_button2 = driver.find_element(
                By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div/div[3]/div[1]/div[2]/div[1]/div/div[5]/div/div/button"
            )
            nsfw_button2.click()
        except:
            pass

        # Click cookie button
        cookies_button = driver.find_element(
            By.XPATH, "/html/body/div[1]/div/div[2]/div[3]/div/section/div/section/section/form[2]/button")
        cookies_button.click()

        # Get title
        title_element = driver.find_element(
            By.CSS_SELECTOR, 'div[data-testid=post-container]')
        img_path = img_folder + "title.png"
        audio_path = img_folder + "title.mp3"
        
        text = title_element.find_element(
            By.TAG_NAME, "h1").get_attribute("innerText")   # get text
        title_element.screenshot(img_path)                  # get screenshot

        audio = gTTS(text=text, lang='en', slow=False, tld='ca')    # get audio
        audio.save("welcome.mp3")

        data["title"]["text"] = text
        data["title"]["img"] = img_path
        data["title"]["audio"] = audio_path


        try:
            comments_container = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div/div[3]/div[1]/div[2]/div[5]/div/div/div')
        except:
            comments_container = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div/div[3]/div[1]/div[2]/div[6]/div/div/div')


        xpath = "*"

        for i in range(10):
            data["comments"].append({})

            # Main comment
            comment = comments_container.find_element(By.XPATH, xpath)
            text = comment.find_element(
                By.TAG_NAME, "p").get_attribute("innerText")
            data["comments"][i]["comment"] = text

            # sceenshoot
            driver.execute_script(
                "arguments[0].scrollIntoView();", comment)
            driver.execute_script("scrollBy(0,-250);")
            img_path = img_folder + f"comment_{i}.png"
            comment.screenshot(img_path)
            data["comments"][i]["img"] = img_path

            # Reply 1
            xpath += "/following-sibling::div"
            comment = comments_container.find_element(By.XPATH, xpath)
            text = comment.find_element(
                By.TAG_NAME, "p").get_attribute("innerText")
            data["comments"][i]["reply"] = text

            # sceenshoot
            driver.execute_script(
                "arguments[0].scrollIntoView();", comment)
            driver.execute_script("scrollBy(0,-250);")
            img_path = img_folder + f"comment_{i}_reply_0.png"
            comment.screenshot(img_path)
            data["comments"][i]["reply_img"] = img_path

            while(text[-13:] != ' more replies'):
                xpath += "/following-sibling::div"
                comment = comments_container.find_element(By.XPATH, xpath)

                try:
                    text = comment.find_element(
                        By.TAG_NAME, "p").get_attribute("innerText")
                except:
                    pass

            xpath += "/following-sibling::div"

        return data


webscraper = Webscraper()
