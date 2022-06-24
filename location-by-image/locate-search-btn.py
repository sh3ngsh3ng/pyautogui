import pyautogui as bot

# Two lines of code
# location = bot.locateOnScreen('./search.png')
# search_btn = bot.center(location)
# bot.moveTo(search_btn)

# Using one line
res = bot.locateCenterOnScreen("./search.png")
bot.moveTo(res)