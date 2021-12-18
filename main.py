from webscraper import webscraper

webscraper.clear_data()
post_url = "https://reddit.com/" + webscraper.get_todays_url() + "?sort=top"
print(post_url)
print(webscraper.get_data(post_url))