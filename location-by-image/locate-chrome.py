import pyautogui as bot
bot.PAUSE = 0.5

# Exit to desktop
bot.keyDown('winleft')
bot.press('d')
bot.keyUp('winleft')


# Locate chrome icon on desktop
# requires opencv for confidence level
chrome_icon = bot.locateCenterOnScreen('./chrome-icon2.png', confidence=0.7)
while chrome_icon == None:
    print("Trying to locate chrome again.")
    chrome_icon = bot.locateCenterOnScreen('./chrome-icon2.png')
bot.moveTo(chrome_icon)
bot.doubleClick()

# Choose chrome profile
chrome_profile = bot.locateCenterOnScreen("./chrome-profile.png", confidence=0.9)
while chrome_profile == None:
    print("Trying to select chrome profile")
    chrome_profile = bot.locateCenterOnScreen("./chrome-profile.png", confidence=0.9)
print(chrome_profile)
bot.moveTo(chrome_profile)
bot.doubleClick()

# Open new tab
bot.keyDown("ctrl")
bot.press("t")
bot.keyUp("ctrl")

# Go to webpage
bot.write("https://www.google.com")
bot.press("enter")


