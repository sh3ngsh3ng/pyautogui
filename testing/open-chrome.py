import pyautogui as bot
bot.PAUSE=2



# navigate to chrome icon
bot.moveTo(320, 650)
bot.doubleClick()

# choose chrome profile
bot.moveTo(600, 600)
bot.doubleClick()

# navigate to google website
bot.moveTo(1000,60)
bot.click()
bot.write("www.spotify.com")
bot.press("enter")