import pyautogui as bot
bot.PAUSE = 1
bot.FAILSAFE = True

def open_browser(url):
    # navigate to chrome icon
    bot.moveTo(320, 650)
    bot.doubleClick()

    # choose chrome profile
    bot.moveTo(600, 600)
    bot.doubleClick()

    # navigate to google website
    bot.moveTo(1000,60)
    bot.click()
    bot.write(url)
    bot.press("enter")


def login_instagram(username, password):
    bot.moveTo(1060, 335)
    bot.click()
    bot.write(username)
    bot.moveTo(1060, 385)
    bot.click()
    bot.write(password)
    bot.moveTo(1060, 450)
    bot.click()
    bot.moveTo(380, 130, 5)
    bot.click()

def scroll_post(post_num):
    bot.moveTo(750, 500)
    bot.click()
    for x in range(post_num):
        bot.scroll(-1000)
        bot.doubleClick()