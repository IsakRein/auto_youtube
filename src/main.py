from webscraper import webscraper
from video_creator import Video_Creator
from src.audio_manager import audio_manager

class Main:
    def ask_reddit(self):
        webscraper.authenticate()
        audio_manager.authenticate()
        webscraper.clear_data()
        post_url = "https://reddit.com/" + webscraper.get_todays_url() + "?sort=top"
        
        data = webscraper.get_data(post_url, 200)

        video_creator = Video_Creator(data)
        video_creator.create()

    def print(self):
        print("penis in vagaga")

main = Main()
main.ask_reddit()