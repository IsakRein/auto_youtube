from unsplash.api import Api
from unsplash.auth import Auth
from data_manager import secret
import requests
from bs4 import BeautifulSoup
from PIL import Image

from video_creator import WIDTH

class Thumbnail_Manager:
    def generate(self, search, path):
        self.get_image(search, path)
        self.resize_img(path)
        self.edit_img(path)

    def get_image(self, search, path):
        client_id = secret["unsplash_access_key"]
        client_secret = secret["unsplash_secret_key"]
        redirect_uri = secret["unsplash_secret_key"]
        code = ""

        auth = Auth(client_id, client_secret, redirect_uri, code=code)
        api = Api(auth)

        photo_id = api.search.photos(search)["results"][0].id
        res = requests.get("https://unsplash.com/photos/" + photo_id)
        soup = BeautifulSoup(res.content, 'html.parser')

        images = soup.findAll("img")
        img_url = ""
        for image in images:
            if (image["src"][:33] == "https://images.unsplash.com/photo"):
                img_url = image["src"]
                break

        image_data = requests.get(img_url)

        file = open(path, "wb")
        file.write(image_data.content)
        file.close()

    def resize_img(self, path):
        img = Image.open(path)
        print(img.width, img.height)

        if (img.width / img.height > 1280/620):
            new_height = img.height
            new_width = new_height*1280/620
        else:
            new_width = img.width
            new_height = new_width*620/1280

        left = (img.width - new_width) / 2
        right = left + new_width
        top = (img.height - new_height) / 2
        bottom = top + new_height


        img = img.crop((left, top, right, bottom))

        img = img.resize((1280, 620), Image.ANTIALIAS)

        background = Image.new('RGB', (1280, 720))

        background.paste(img)

        background.save(path)
 
    def edit_img(self, path):
        img = Image.open(path)
        foreground = Image.open("meta/thumbnail_foreground.png")
        img.paste(foreground, (0,0), foreground)
        img.save(path)


thumbnail_manager = Thumbnail_Manager()