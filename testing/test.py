import pyautogui as bot
# bot.PAUSE=2.5
bot.FAILSAFE = True

# screen_size = bot.size()
bot.moveTo(1000,60, 2)
bot.click()
bot.write("www.google.com")
bot.press("enter")