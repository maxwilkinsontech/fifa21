from bot import Bot
from config import USER, PLAYER, LOGIN_MANUALLY

bot = Bot()
if LOGIN_MANUALLY:
    bot.login_manually()
else:
    bot.login(USER)

bot.buy_player(PLAYER["name"], PLAYER["cost"])


