from webscraper import webscraper
from video_creator import Video_Creator
from audio_manager import audio_manager
from data_manager import secret, data_object, save_data_object

# webscraper.authenticate()
# audio_manager.authenticate()
# webscraper.clear_data()
# post_url = "https://reddit.com/" + webscraper.get_todays_url() + "?sort=top"
# data = webscraper.get_data(post_url, 200)

data = {
   "title":{
      "text":"What isn't a cult but feels like a cult?",
      "img":"./data/img/title.png",
      "audio":"./data/audio/title.mp3",
      "length":2.985333333333333
   },
   "total_length":202.57266666666663,
   "comments":[
      {
         "text":" Being a fan of certain movies or shows. Some people just take it way too far.",
         "img":"./data/img/comment_0a.png",
         "audio":"./data/audio/comment_0a.mp3",
         "upvotes":33900,
         "length":4.758,
         "replies":[
            {
               "text":" The Office anyone?",
               "img":"./data/img/comment_0b.png",
               "audio":"./data/audio/comment_0b.mp3",
               "upvotes":15500,
               "length":1.5448333333333333
            }
         ]
      },
      {
         "text":" My gym",
         "img":"./data/img/comment_1a.png",
         "audio":"./data/audio/comment_1a.mp3",
         "upvotes":20400,
         "length":1.1268333333333334,
         "replies":[
            {
               "text":" At Globo Gym we’re better than you and we know it.",
               "img":"./data/img/comment_1b.png",
               "audio":"./data/audio/comment_1b.mp3",
               "upvotes":16400,
               "length":2.772666666666667
            }
         ]
      },
      {
         "text":" All of those do-it-at-home, online marketing that I see a lot of women in my life get sucked into, where you make a ton of posts and hype up whatever occupation you\\'re in as a \"lifestyle\", with promises of good pay, great social circles, and fulfilling incentives",
         "img":"./data/img/comment_2a.png",
         "audio":"./data/audio/comment_2a.mp3",
         "upvotes":19900,
         "length":13.796333333333333,
         "replies":[
            {
               "text":" MLM and cryptobros.",
               "img":"./data/img/comment_2b.png",
               "audio":"./data/audio/comment_2b.mp3",
               "upvotes":8800,
               "length":2.0411666666666664
            }
         ]
      },
      {
         "text":" Hustle Culture. I used to work with a guy who bragged he \"only sleeps 10 minutes a night\" because as soon as he got off he\\'d go do gigs or play with crypto all night. The only things in his life, supposedly, was \"banging bitches and getting bags.\" He\\'s far from the only person who thinks it\\'s \"Chad\" to run yourself ragged and never take care of yourself.",
         "img":"./data/img/comment_3a.png",
         "audio":"./data/audio/comment_3a.mp3",
         "upvotes":19200,
         "length":18.655,
         "replies":[
            {
               "text":" Crypto has definitely gotten a little culty.",
               "img":"./data/img/comment_3b.png",
               "audio":"./data/audio/comment_3b.mp3",
               "upvotes":7500,
               "length":2.7203333333333335
            }
         ]
      },
      {
         "text":" Employers who express themselves as a unit, such as we are a family/pack, etc.",
         "img":"./data/img/comment_4a.png",
         "audio":"./data/audio/comment_4a.mp3",
         "upvotes":14400,
         "length":5.567666666666667,
         "replies":[
            {
               "text":" My boss told me that once and I told him he was full of shit. Needless to say, my dad no longer required my services in the family business.",
               "img":"./data/img/comment_4b.png",
               "audio":"./data/audio/comment_4b.mp3",
               "upvotes":14000,
               "length":8.258333333333333
            }
         ]
      },
      {
         "text":" Kpop fandoms",
         "img":"./data/img/comment_5a.png",
         "audio":"./data/audio/comment_5a.mp3",
         "upvotes":9100,
         "length":1.5971666666666666,
         "replies":[
            {
               "text":" Kpop industry in general. These companies are training idols as kids and after years of training to be a \"perfect\" idol it isn\\'t even certain that you would debut. Also, companies tend to fixate on weight and causes a lot of idols to have eating disorders. Plus, most idols can\\'t even date because the companies don\\'t allow it, the fans freak out like they fucking own the idol, and media shames them for having a relationship out on the public. The way I see it is if you are an idol in the kpop industry, they basically own you.",
               "img":"./data/img/comment_5b.png",
               "audio":"./data/audio/comment_5b.mp3",
               "upvotes":4900,
               "length":27.562833333333334
            }
         ]
      },
      {
         "text":" Texas A&M University",
         "img":"./data/img/comment_6a.png",
         "audio":"./data/audio/comment_6a.mp3",
         "upvotes":8900,
         "length":2.067333333333333,
         "replies":[
            {
               "text":" Am an Aggie. Our fave saying is “From the outside looking in, you can’t understand it. From the inside looking out, you can’t explain it.” 100% a cult.",
               "img":"./data/img/comment_6b.png",
               "audio":"./data/audio/comment_6b.mp3",
               "upvotes":5400,
               "length":9.956333333333333
            }
         ]
      },
      {
         "text":" Blue Öysters. Those sons of bitches are hard as hell.",
         "img":"./data/img/comment_7a.png",
         "audio":"./data/audio/comment_7a.mp3",
         "upvotes":6300,
         "length":3.5301666666666667,
         "replies":[
            {
               "text":" They don't even fear the reaper!",
               "img":"./data/img/comment_7b.png",
               "audio":"./data/audio/comment_7b.mp3",
               "upvotes":2400,
               "length":1.9628333333333334
            }
         ]
      },
      {
         "text":" AA",
         "img":"./data/img/comment_8a.png",
         "audio":"./data/audio/comment_8a.mp3",
         "upvotes":6200,
         "length":1.0746666666666667,
         "replies":[
            {
               "text":" My dumbass just got home from a terrible trip the other day. I read this and was confused as to why American Airlines is considered a cult.",
               "img":"./data/img/comment_8b.png",
               "audio":"./data/audio/comment_8b.mp3",
               "upvotes":4900,
               "length":7.683666666666666
            }
         ]
      },
      {
         "text":" LulaRoe lovers",
         "img":"./data/img/comment_9a.png",
         "audio":"./data/audio/comment_9a.mp3",
         "upvotes":4600,
         "length":1.6755,
         "replies":[
            {
               "text":" Any kind of pyramid scheme, for that matter",
               "img":"./data/img/comment_9b.png",
               "audio":"./data/audio/comment_9b.mp3",
               "upvotes":2200,
               "length":3.1121666666666665
            }
         ]
      },
      {
         "text":" Nickocado Avodaco subscribers",
         "img":"./data/img/comment_10a.png",
         "audio":"./data/audio/comment_10a.mp3",
         "upvotes":4400,
         "length":2.4591666666666665,
         "replies":[
            {
               "text":" I feel like a lot of people have subbed to him to watch him slowly kill himself/to laugh at him. I've never actually seen anyone talk positively about him in his current state",
               "img":"./data/img/comment_10b.png",
               "audio":"./data/audio/comment_10b.mp3",
               "upvotes":2400,
               "length":9.303166666666666
            }
         ]
      },
      {
         "text":" Any kind of brand loyalty",
         "img":"./data/img/comment_11a.png",
         "audio":"./data/audio/comment_11a.mp3",
         "upvotes":4300,
         "length":1.989,
         "replies":[
            {
               "text":" “I’d rather push a Ford than drive a Chevy!” But… why though!?",
               "img":"./data/img/comment_11b.png",
               "audio":"./data/audio/comment_11b.mp3",
               "upvotes":1700,
               "length":4.209333333333333
            }
         ]
      },
      {
         "text":" Army",
         "img":"./data/img/comment_12a.png",
         "audio":"./data/audio/comment_12a.mp3",
         "upvotes":4000,
         "length":1.0485,
         "replies":[
            {
               "text":" Every Marine I've spoken to gave me cultish vibes too.",
               "img":"./data/img/comment_12b.png",
               "audio":"./data/audio/comment_12b.mp3",
               "upvotes":2200,
               "length":3.3473333333333333
            }
         ]
      },
      {
         "text":" Politics",
         "img":"./data/img/comment_13a.png",
         "audio":"./data/audio/comment_13a.mp3",
         "upvotes":4000,
         "length":1.362,
         "replies":[
            {
               "text":" So many people have made their political party of choice into their personality and it's unbearable. Agree or gtfo is pretty much what it has become. So yeah pretty cult like.",
               "img":"./data/img/comment_13b.png",
               "audio":"./data/audio/comment_13b.mp3",
               "upvotes":1400,
               "length":10.113
            }
         ]
      },
      {
         "text":" Peloton",
         "img":"./data/img/comment_14a.png",
         "audio":"./data/audio/comment_14a.mp3",
         "upvotes":3500,
         "length":1.4403333333333332,
         "replies":[
            {
               "text":" I've been saying this for like two years!! I know someone with a peloton and I am very happy that it got them to lose weight and be active, but man they way they talked about it and posted on Facebook about it made me feel like it was a cult lmao",
               "img":"./data/img/comment_14b.png",
               "audio":"./data/audio/comment_14b.mp3",
               "upvotes":1100,
               "length":12.542333333333334
            }
         ]
      },
      {
         "text":" Apple.",
         "img":"./data/img/comment_15a.png",
         "audio":"./data/audio/comment_15a.mp3",
         "upvotes":3100,
         "length":0.9963333333333333,
         "replies":[
            {
               "text":" I worked as callcenter agent, internet helpdesk once. Sometimes I\\'d ask people to do something on their laptop, and they would say \"I don\\'t have a laptop, I have a macbook\" If I once more said \"laptop\" in the conversation, while being focussed on solving the problem, they would shout at me \"I DONT HAVE A LAPTOP I HAVE A MACBOOK.\" I guess, if you pay that much you want some acknowledgement? It didn\\'t happen just once. It happend often. Edit: wow. 1.9k upvotes. Glad its not just me who thinks its cringy.",
               "img":"./data/img/comment_15b.png",
               "audio":"./data/audio/comment_15b.mp3",
               "upvotes":2000,
               "length":29.313
            }
         ]
      }
   ]
}
print(data)

data_object["characters_used"] += len(data["title"]["text"])
save_data_object()

for i in data["title"]["comments"]:
   


video_creator = Video_Creator(data)
video_creator.create()
