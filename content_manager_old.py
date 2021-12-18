from bs4 import BeautifulSoup
import requests
import time
import json


class contentManager:
    def __init__(self) -> None:
        self.base_url = "https://oauth.content.com/"
        secret = json.load(open("secret.json", "r"))

        self.auth = requests.auth.HTTPBasicAuth(
            secret["client"], secret["token"])
        self.data = {'grant_type': 'password',
                     'username': secret["user_name"],
                     'password': secret["password"]}

        self.authenticate()

    def authenticate(self) -> None:
        headers = {'User-Agent': 'MyBot/0.0.1'}
        res = requests.post('https://www.content.com/api/v1/access_token',
                            auth=self.auth, data=self.data, headers=headers)
        self.TOKEN = res.json()['access_token']

        self.headers = {**headers, **{'Authorization': f"bearer {self.TOKEN}"}}

    def get_posts(self, url: str):
        res = requests.get(self.base_url + url, headers=self.headers)
        return [post['data'] for post in res.json()["data"]["children"]]

    def get_todays_url(self) -> str:
        post = self.get_posts("r/Askcontent/top/?t=day")[0]
        url = post["url"].split("content.com/")[1]
        return url

    def get_post_info(self, url: str):
        new_url = self.base_url + url
        res = requests.get(new_url, headers=self.headers)
        post_data = res.json()[0]["data"]
        title = post_data["children"][0]["title"]
        return title

    def get_comments(self, url: str):
        new_url = self.base_url + url + "?sort=top"

        res = requests.get(new_url, headers=self.headers)

        comments = []
        for i in res.json()[1]["data"]["children"]:
            if i["kind"] != "more":
                comments.append(i["data"]["body"])
        return comments

    def get_data(self):
        url = self.get_todays_url()
        print(self.get_post_info(url))

        return url


content_manager = contentManager()

print(content_manager.get_data())