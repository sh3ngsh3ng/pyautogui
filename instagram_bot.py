import os
import functions as utils
from dotenv import load_dotenv

load_dotenv()

# print(os.environ.get("TEST"))


# # Open up browser
# url = "www.instagram.com"
# utils.open_browser(url)

# # Login Instagram
# username = os.environ.get("INSTA_USERNAME")
# password = os.environ.get("INSTA_PASSWORD")
# utils.login_instagram(username, password)

# Like Posts
utils.scroll_post(10)
import pyautogui as bot
image = bot.screenshot()
