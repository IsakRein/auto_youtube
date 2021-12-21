from typing import final
from moviepy import editor


class Video_Creator:
    def __init__(self, data) -> None:
        self.data = data

    def create(self):
        background_video = editor.VideoFileClip(
            "data/background/background0.mp4", audio=False)

        self.final_video = background_video.resize(width=1920, height=1080)

        background_loop_count = (
            self.data["total_length"] // self.final_video.duration) + 1
        self.final_video = self.final_video.loop(background_loop_count)
        self.final_audio = editor.AudioFileClip("data/music/music0.mp3")

        if self.final_video.duration < self.final_audio.duration:
            self.final_audio = self.final_audio.subclip(
                0, self.final_video.duration)

        self.current_time = 0

        self.video_clips = [self.final_video]
        self.audio_clips = [self.final_audio]

        self.add_clip(self.data["title"]["img"], self.data["title"]["audio"])

        for comment in self.data["comments"]:
            self.add_clip(comment["img"], comment["audio"])
            for reply in comment["replies"]:
                self.add_clip(reply["img"], reply["audio"])

        self.final_video = editor.CompositeVideoClip(self.video_clips)
        self.final_audio = editor.CompositeAudioClip(self.audio_clips)

        self.final_video = self.final_video.set_audio(self.final_audio)
        self.final_video.write_videofile(
            "data/output/video0.mp4",
            codec='libx264',
            audio_codec='aac',
            temp_audiofile='temp-audio.m4a',
            remove_temp=True,
            fps=24
        )

    def add_clip(self, img_path, audio_path):
        img = (editor.ImageClip(img_path)
                     .resize(width=1400)
                     .set_pos(("center", "center")))
        audio = editor.AudioFileClip(audio_path)

        img = img.set_start(self.current_time)
        img = img.subclip(0, audio.duration)
        audio = audio.set_start(self.current_time)

        self.video_clips.append(img)
        self.audio_clips.append(audio)

        self.current_time += audio.duration
