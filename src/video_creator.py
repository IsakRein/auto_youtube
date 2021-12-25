import os
import random

from typing import final
from moviepy import editor
from moviepy.video.VideoClip import VideoClip
from moviepy.video.fx.all import crop

from data_manager import data_object, save_data_object

HEIGHT = 1080
WIDTH = 1920

class Video_Creator:
    def create(self, data):
        self.data = data

        video_object = self.select_meta_data()

        background_path =  "data/backgrounds/" + video_object["background"]   
        music_path =  "data/music/" + video_object["music"]      

        background_video = editor.VideoFileClip(background_path, audio=False)

        self.final_video = background_video.resize(width=WIDTH, height=HEIGHT)

        background_loop_count = (
            self.data["total_length"] // self.final_video.duration) + 1
        self.final_video = self.final_video.loop(background_loop_count)
        self.final_audio = editor.AudioFileClip(music_path).volumex(0.3)

        if self.final_video.duration < self.final_audio.duration:
            self.final_audio = self.final_audio.subclip(
                0, self.final_video.duration)

        self.current_time = 0

        self.video_clips = [self.final_video]
        self.audio_clips = [self.final_audio]
        
        self.add_clips(
            [editor.ImageClip(self.data["title"]["img"]).resize(width=1400)], 
            [editor.AudioFileClip(self.data["title"]["audio"])],
            [self.data["title"]]
        )

        for comment in self.data["comments"]:
            img_list = [editor.ImageClip(comment["img"]).resize(width=1400)]
            audio_list = [editor.AudioFileClip(comment["audio"])]
            current_data = [comment]
            
            for reply in comment["replies"]:
                img_list.append(editor.ImageClip(reply["img"]).resize(width=1400))
                audio_list.append(editor.AudioFileClip(reply["audio"]))
                current_data.append(reply)

            self.add_clips(img_list, audio_list, current_data)


        self.final_video = editor.CompositeVideoClip(self.video_clips)
        self.final_audio = editor.CompositeAudioClip(self.audio_clips)

        self.final_video = self.final_video.set_audio(self.final_audio)
        self.final_video.write_videofile(
            "data/output/" + video_object["video_name"],
            codec='libx264',
            audio_codec='aac',
            temp_audiofile='data/temp/temp-audio.m4a',
            remove_temp=True,
            fps=24
        )

        video_object["title"] = data["title"]

        return video_object

    def add_clips(self, img_list, audio_list, current_data):
        print(current_data)
        total_height = sum([x.size[1] for x in img_list])
        total_duration = sum([x["length"] for x in current_data])

        current_y = (HEIGHT - total_height) / 2
        time_elapsed = 0

        for i in range(len(img_list)):
            img = img_list[i]
            audio = audio_list[i] 

            img = img.set_position(("center", current_y))
            current_y += img.size[1]


            img = img.set_start(self.current_time)
            img = img.subclip(0, total_duration - time_elapsed)
            
            time_elapsed += current_data[i]["length"]
            
            audio = audio.set_start(self.current_time)

            self.video_clips.append(img)
            self.audio_clips.append(audio)

            self.current_time += current_data[i]["length"]
            
    def select_meta_data(self):
        music_files = os.listdir("data/music")
        background_files = os.listdir("data/backgrounds")
        videos = data_object["videos"]

        go_back = 5

        previous_backgrounds = [x["background"] for x in videos[-go_back:]]
        previous_music = [x["music"] for x in videos[-go_back:]]


        while True:
            background = random.choice(background_files)
            music = random.choice(music_files)
            if (music not in previous_music and background not in previous_backgrounds):
                break 

        video_number = len(data_object)
        video_name = "video" + str(video_number) + ".mp4"

        return {
            "video_number": video_number,
            "background": background,
            "music": music,
            "output": video_name
        }

video_creator = Video_Creator()     