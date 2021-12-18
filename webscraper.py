from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

content





chrome_options = webdriver.ChromeOptions()

ser = Service("./chromedriver")
op = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications": 2}
op.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(service=ser, options=op)
driver.get('https://www.reddit.com/r/AskReddit/comments/riujkw/what_tv_show_has_the_best_theme_song_of_all_time/')
driver.maximize_window()

actions = ActionChains(driver)

cookies_button = driver.find_element(
    By.XPATH, "/html/body/div[1]/div/div[2]/div[3]/div/section/div/section/section/form[2]/button")
cookies_button.click()

title_element = driver.find_element(
    By.CSS_SELECTOR, 'div[data-testid=post-container]')
title_element.screenshot("./data/img/title.png")

comments_container = driver.find_element(
    By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div/div[3]/div[1]/div[2]/div[6]/div/div/div")
i = 0

xpath = "*"

while (True):
    try:
        comment = comments_container.find_element(By.XPATH, xpath)
        driver.execute_script("arguments[0].scrollIntoView();", comment)
        driver.execute_script("scrollBy(0,-250);")
        comment.screenshot(f"./data/img/comment_{i}.png")
        xpath += "/following-sibling::div"
        i += 1
    except Exception as e:
        print(e)
        break
