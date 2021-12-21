import requests
import json
import os
import pyautogui

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from audio_manager import audio_manager


class Webscraper:
    def __init__(self) -> None:
        self.base_url = "https://oauth.reddit.com/"
        self.secret = json.load(open("secret.json", "r"))

        self.auth = requests.auth.HTTPBasicAuth(
            self.secret["client"], self.secret["token"])
        self.auth_data = {'grant_type': 'password',
                     'username': self.secret["user_name"],
                     'password': self.secret["password"]}

    def authenticate(self) -> None:
        headers = {'User-Agent': 'MyBot/0.0.1'}
        res = requests.post('https://www.reddit.com/api/v1/access_token',
                            auth=self.auth, data=self.auth_data, headers=headers)
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
        os.system("rm -r data/img")
        os.system("rm -r data/audio")
        os.system("mkdir data/img")
        os.system("mkdir data/audio")

    def get_data(self, url, video_length):
        self.data = {}
        self.data["title"] = {}
        self.data["total_length"] = 0
        self.data["comments"] = []

        self.img_folder = "./data/img/"
        self.audio_folder = "./data/audio/"

        self.driver = self.init_driver(url)
        self.click_reddit_buttons()
        self.get_reddit_title()

        comments_container = self.get_reddit_comments_container()

        xpath = "*"

        index = 0
        while (self.data["total_length"] < video_length):
            text1, img_path1, audio_path1, upvotes1, audio_length1 = self.get_reddit_comment(
                str(index)+"a", xpath, comments_container
            )
            xpath += "/following-sibling::div"
            text2, img_path2, audio_path2, upvotes2, audio_length2 = self.get_reddit_comment(
                str(index)+"b", xpath, comments_container
            )

            self.data["comments"].append({})
            self.data["comments"][index]["text"] = text1
            self.data["comments"][index]["img"] = img_path1
            self.data["comments"][index]["audio"] = audio_path1
            self.data["comments"][index]["upvotes"] = upvotes1
            self.data["comments"][index]["length"] = audio_length1
            self.data["comments"][index]["replies"] = []
            self.data["total_length"] += audio_length1

            if upvotes2/upvotes1 >= 0.3:
                self.data["comments"][index]["replies"].append({})
                self.data["comments"][index]["replies"][0]["text"] = text2
                self.data["comments"][index]["replies"][0]["img"] = img_path2
                self.data["comments"][index]["replies"][0]["audio"] = audio_path2
                self.data["comments"][index]["replies"][0]["upvotes"] = upvotes2
                self.data["comments"][index]["replies"][0]["length"] = audio_length2
                self.data["total_length"] += audio_length2

            text = ""
            # loop through divs until the div that says more replies (end of current comment)
            while(text[-13:] != ' more replies'):
                xpath += "/following-sibling::div"
                comment = comments_container.find_element(By.XPATH, xpath)
                try:
                    text = comment.find_element(
                        By.TAG_NAME, "p").get_attribute("innerText")
                except:
                    pass

            xpath += "/following-sibling::div"
            index += 1
            self.driver.implicitly_wait(0.2)

        self.driver.quit()
        return self.data

    def init_driver(self, url):
        # Driver init
        ser = Service(self.secret["chromedriver"])
        op = webdriver.ChromeOptions()
        prefs = {"profile.default_content_setting_values.notifications": 2}
        op.add_experimental_option("prefs", prefs)
        driver = webdriver.Chrome(service=ser, options=op)

        pyautogui.moveTo(0, 0)

        # Get url
        driver.get(url)
        driver.maximize_window()

        return driver

    def click_reddit_buttons(self):
        # Click NSFW button
        try:
            nsfw_button = self.driver.find_element(
                By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[2]/button"
            )
            nsfw_button.click()
            nsfw_button2 = self.driver.find_element(
                By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div/div[3]/div[1]/div[2]/div[1]/div/div[5]/div/div/button"
            )
            nsfw_button2.click()
        except:
            pass

        # Click cookie button
        cookies_button = self.driver.find_element(
            By.XPATH, "/html/body/div[1]/div/div[2]/div[3]/div/section/div/section/section/form[2]/button")
        cookies_button.click()

    def get_reddit_title(self):
        # Get title
        title_element = self.driver.find_element(
            By.CSS_SELECTOR, 'div[data-testid=post-container]')

        # ---- text
        text = title_element.find_element(
            By.TAG_NAME, "h1").get_attribute("innerText")

        # ---- screenshot
        img_path = self.img_folder + "title.png"
        title_element.screenshot(img_path)

        # ---- audio
        audio_path = self.audio_folder + "title.mp3"
        audio_length = audio_manager.save_audio(text, audio_path)

        self.data["title"]["text"] = text
        self.data["title"]["img"] = img_path
        self.data["title"]["audio"] = audio_path
        self.data["title"]["audio_length"] = audio_length
        self.data["total_length"] += audio_length

    def get_reddit_comments_container(self):
        try:
            return self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div/div[3]/div[1]/div[2]/div[5]/div/div/div')
        except:
            return self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div/div[3]/div[1]/div[2]/div[6]/div/div/div')

    def get_reddit_comment(self, name, xpath, comments_container):
        # Main comment
        comment = comments_container.find_element(By.XPATH, xpath)

        self.driver.execute_script(
            "arguments[0].scrollIntoView();", comment)
        self.driver.execute_script("scrollBy(0,-250);")

        # ---- text
        text = comment.find_element(
            By.TAG_NAME, "p").get_attribute("innerText")

        # ---- screenshot
        img_path = self.img_folder + "comment_" + name + ".png"
        comment.screenshot(img_path)

        # ---- audio
        audio_path = self.audio_folder + "comment_" + name + ".mp3"
        audio_length = audio_manager.save_audio(text, audio_path)

        # ---- upvotes
        try:
            upvotes = comment.find_element(
                By.XPATH, './/button[@aria-label="upvote"]/following-sibling::div').get_attribute("innerText")
        except:
            upvotes = "0"

        if "k" in upvotes:
            if "." in upvotes:
                number_str = upvotes[:-1]
                number = int(number_str.split(".")[0])
                decimal = int(number_str.split(".")[1])
                upvotes = number * 1000 + decimal * 100
            else:
                upvotes = int(upvotes[:-1]) * 1000
        else:
            upvotes = int(upvotes)

        return text, img_path, audio_path, upvotes, audio_length


webscraper = Webscraper()
