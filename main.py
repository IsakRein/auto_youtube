from webscraper import webscraper
from video_creator import Video_Creator
from mutagen.aiff import AIFF

# webscraper.authenticate()
# webscraper.clear_data()
# post_url = "https://reddit.com/" + webscraper.get_todays_url() + "?sort=top"
# print(webscraper.get_data(post_url, 10))

data = {'title': {'text': 'What movie SHOULD have had a sex scene?', 'img': './data/img/title.png', 'audio': './data/audio/title.mp3', 'audio_length': 2.044625850340136}, 'total_length': 111.72353741496597, 'comments': [{'text': 'Cars. I never understood how they fucked or how new cars were born..', 'img': './data/img/comment_0a.png', 'audio': './data/audio/comment_0a.mp3', 'upvotes': '35.1k', 'audio_length': 3.987482993197279, 'replies': [{'text': 'I was a very emotionally conflicted13 year old when I saw the scene where the main guy points out the pinstripe tramp stamp on the blue porsche', 'img': './data/img/comment_0b.png', 'audio': './data/audio/comment_0b.mp3', 'upvotes': '35.1k', 'length': 7.762176870748299}]}, {'text': 'The movie Sex Tape had zero sex scenes.', 'img': './data/img/comment_1a.png', 'audio': './data/audio/comment_1a.mp3', 'upvotes': '35.1k', 'audio_length': 2.69687074829932, 'replies': [{'text': 'Yeah, but the sex scene would have been Cameron Diaz and Jason Segal. Does anyone really need to see that?', 'img': './data/img/comment_1b.png', 'audio': './data/audio/comment_1b.mp3', 'upvotes': '35.1k', 'length': 5.911836734693877}]}, {'text': '“The Island” had a sex scene, but Scarlett Johansson wanted to show her boobs and Michael Bay turned her down.', 'img': './data/img/comment_2a.png', 'audio': './data/audio/comment_2a.mp3', 'upvotes': '35.1k', 'audio_length': 5.847074829931973, 'replies': [{'text': 'I knew I never liked that guy.', 'img': './data/img/comment_2b.png', 'audio': './data/audio/comment_2b.mp3', 'upvotes': '35.1k', 'length': 1.8133333333333332}]}, {'text': 'Monty Python and the Holy Grail came so close', 'img': './data/img/comment_3a.png', 'audio': './data/audio/comment_3a.mp3', 'upvotes': '35.1k', 'audio_length': 2.8078911564625852, 'replies': [{'text': 'I was also quite close', 'img': './data/img/comment_3b.png', 'audio': './data/audio/comment_3b.mp3', 'upvotes': '35.1k', 'length': 1.7670748299319727}]}, {'text': 'The incredibles. We all know we wanted to see how elastagirl got down', 'img': './data/img/comment_4a.png', 'audio': './data/audio/comment_4a.mp3', 'upvotes': '35.1k', 'audio_length': 4.366802721088435, 'replies': [{'text': "Don't worry, the internet has you covered.", 'img': './data/img/comment_4b.png', 'audio': './data/audio/comment_4b.mp3', 'upvotes': '35.1k', 'length': 2.3268027210884354}]}, {'text': "Hear me out: every cheesy rom com should have a nut busting, pussy pounding, furniture snapping sex scene. It's the one thing missing from the love story...the physical pay off of moving to a small town to start a local coffee shop and falling in love with a forlorn cowboy with commitment issues. Like ... Imagine the satisfaction and closure if how to lose a guy in 10 days had Kate Hudson and Matthew McConaughey rolling in the sheets, no pants, penis in vagina. Or if, in the runaway bride, Julia Roberts blows Richard Gere's mind with the sex scene that the 90's fucking deserved to see. We're at the point in our society that Hallmark Christmas movie female protagonists should have an intense, life altering, orgasms that really bring the magic back to Christmas.", 'img': './data/img/comment_5a.png', 'audio': './data/audio/comment_5a.mp3', 'upvotes': '35.1k', 'audio_length': 41.80843537414966, 'replies': [{'text': 'Someone get this guy a beer', 'img': './data/img/comment_5b.png', 'audio': './data/audio/comment_5b.mp3', 'upvotes': '35.1k', 'length': 1.71156462585034}]}, {'text': 'Every single movie that twelve year old me watched when my parents were not home.', 'img': './data/img/comment_6a.png', 'audio': './data/audio/comment_6a.mp3', 'upvotes': '35.1k', 'audio_length': 4.297414965986395, 'replies': [{'text': 'When I was 10, I watched two seasons of sex and the city hoping for some sex scenes.', 'img': './data/img/comment_6b.png', 'audio': './data/audio/comment_6b.mp3', 'upvotes': '35.1k', 'length': 5.268843537414966}]}, {'text': 'Pride and prejudice', 'img': './data/img/comment_7a.png', 'audio': './data/audio/comment_7a.mp3', 'upvotes': '35.1k', 'audio_length': 1.4247619047619047, 'replies': [{'text': 'God yes! I really want to see if Mr Darcy is a gentleman in the streets, a freak in the sheets or not', 'img': './data/img/comment_7b.png', 'audio': './data/audio/comment_7b.mp3', 'upvotes': '35.1k', 'length': 6.235646258503401}]}, {'text': 'The obvious answer is Predator. Just so much packed on mass and sexual tension.', 'img': './data/img/comment_8a.png', 'audio': './data/audio/comment_8a.mp3', 'upvotes': '35.1k', 'audio_length': 4.63047619047619, 'replies': [{'text': 'Mac, I told you we are watching transporter 2!', 'img': './data/img/comment_8b.png', 'audio': './data/audio/comment_8b.mp3', 'upvotes': '35.1k', 'length': 3.0484353741496597}]}, {'text': 'The Bee Movie', 'img': './data/img/comment_9a.png', 'audio': './data/audio/comment_9a.mp3', 'upvotes': '35.1k', 'audio_length': 0.929795918367347, 'replies': [{'text': 'Ya like jizz?', 'img': './data/img/comment_9b.png', 'audio': './data/audio/comment_9b.mp3', 'upvotes': '35.1k', 'length': 1.036190476190476}]}]}
video_creator = Video_Creator(data)
video_creator.create()
