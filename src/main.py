import os
import logging

from webscraper import webscraper
from video_creator import video_creator
from youtube_manager import youtube_manager 
from audio_manager import audio_manager
from data_manager import meta_data
from thumbnail_manager import thumbnail_manager

# GOAL: 
# This script should be run from a terminal with no parameters, and at the end of the process, the video should be uploaded to youtube.
class Main:
    def __init__(self):
        level = logging.INFO
        fmt = '[%(levelname)s] %(asctime)s - %(message)s'
        logging.basicConfig(level=level, format=fmt)

    def ask_reddit(self):
        # # Clear previous temp data
        # logging.info("Clearing data")
        # self.clear_data()
        
        # # Authenticate
        # logging.info("Authenticating")
        # webscraper.authenticate()
        # audio_manager.authenticate()
        
        # # Get data
        # logging.info("Getting data")
        # post_url = f"https://reddit.com/{webscraper.get_todays_url()}?sort=top"
        # content_data = webscraper.get_data(post_url, 200)
        
        # # Create video
        # logging.info("Creating video")
        # video_data = video_creator.create(content_data)

        # # Create thumbnail
        # logging.info("Creating thumbnail")  
        # video_data["thumbnail"] = thumbnail_manager.generate(video_data)
        
        video_data = {
            "video_number": 1,
            "background": "data/backgrounds/background1.mp4",
            "music": "data/music/music4.mp3",
            "video_name": "data/output/video1.mp4",
            "title": "If you were handed 10 billion dollars right now, what would you still never buy?",
            "thumbnail": "data/thumbnails/thumbnail1.png"
        }

        # Update local database
        logging.info("Updating database")  
        meta_data.append("videos", video_data)

        # Upload video
        logging.info("Uploading video")  
        youtube_manager.upload(video_data)

    
    def clear_data(self):
        os.system("rm -r data/img")
        os.system("rm -r data/audio")
        os.system("mkdir data/img")
        os.system("mkdir data/audio")
    
main = Main()
main.ask_reddit()