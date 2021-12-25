from webscraper import webscraper
from video_creator import video_creator
from youtube_manager import youtube_manager 
from audio_manager import audio_manager
from data_manager import data_object, save_data_object
from thumbnail_manager import thumbnail_manager

class Main:
    def ask_reddit(self):
        webscraper.authenticate()
        audio_manager.authenticate()
        webscraper.clear_data()
        post_url = "https://reddit.com/" + webscraper.get_todays_url() + "?sort=top"
        
        thumbnail_manager.generate("cash", "data/thumbnails/thumbnail0.png")

        input(post_url)

        data = webscraper.get_data(post_url, 200)

        video_obj = video_creator.create(data)

        youtube_manager.upload(video_obj)

        data_object["videos"].append(video_obj)
        save_data_object()

main = Main()
main.ask_reddit()