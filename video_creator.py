from moviepy import editor


class Video_Creator:
    def __init__(self, data) -> None:
        self.data = data

    def create(self):
        background_video = editor.VideoFileClip(
            "data/background/background0.mp4", audio=False)

        final_video = background_video.resize(width=1920, height=1080)

        background_loop_count = (self.data["total_length"] // final_video.duration) + 1
        final_video = final_video.loop(background_loop_count)

        final_audio = editor.AudioFileClip("data/music/music0.mp3").subclip(0, final_video.duration)
        # title_audio = 

        title_img = (editor.ImageClip(self.data["title"]["img"])
                     .set_duration(10)
                     .resize(width=1400)
                     .set_pos(("center", "center")))
        title_audio = editor.AudioFileClip(self.data["title"]["audio"])

        final_video = editor.CompositeVideoClip([final_video, title_img])
        final_audio = editor.CompositeAudioClip([final_audio, title_audio])


        final_video = final_video.set_audio(final_audio)
        final_video.write_videofile(
            "data/output/video0.mp4",
            codec='libx264',
            audio_codec='aac',
            temp_audiofile='temp-audio.m4a',
            remove_temp=True
        )
