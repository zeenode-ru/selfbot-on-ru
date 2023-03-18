import requests, colorama
from colorama import Fore
from discord.ext import commands as zeenode
from zeenode.config import auth, prefix, nitro_sniper, giveaway_sniper

colorama.init()

bot = zeenode.Bot(command_prefix=prefix, self_bot=True)
bot.remove_command('help')

class load:
    def __init__(self):
        global token
        
        token = self.check_token(auth)

        nsign = ""
        gsign = ""
        nsign, nsniper = self.nitro_sniper(nsign, nitro_sniper)
        gsign, gsniper = self.nitro_sniper(gsign, giveaway_sniper)


        @bot.event
        async def on_ready():

            self.load_cogs()
            print(f'''{Fore.RESET}
                            {Fore.LIGHTBLACK_EX}╔═════════════════════════════╗
                            {Fore.LIGHTBLACK_EX}║ {Fore.GREEN}╔═╗ ╔═╗ ╔═╗ ╔╗╔ ╔═╗ ╔╦╗ ╔═╗ {Fore.LIGHTBLACK_EX}║ 
                            {Fore.LIGHTBLACK_EX}║ {Fore.LIGHTGREEN_EX}╔═╝ ║╣  ║╣  ║║║ ║ ║  ║║ ║╣  {Fore.LIGHTBLACK_EX}║ 
                            {Fore.LIGHTBLACK_EX}║ {Fore.WHITE}╚═╝ ╚═╝ ╚═╝ ╝╚╝ ╚═╝ ═╩╝ ╚═╝ {Fore.LIGHTBLACK_EX}║
                            {Fore.LIGHTBLACK_EX}╚═════════════════════════════╝
                            {Fore.WHITE}Я вошёл в учетку {Fore.LIGHTGREEN_EX}{bot.user}
                            {Fore.WHITE}Ты находишься на {Fore.LIGHTGREEN_EX}{len(list(bot.guilds))}{Fore.WHITE} сервер(ах).
                            {Fore.WHITE}Ты имеешь {Fore.LIGHTGREEN_EX}{len(list(bot.user.friends))}{Fore.WHITE} друзей.
                        {Fore.WHITE}Префикс селфбота {Fore.LIGHTGREEN_EX}{prefix}{Fore.WHITE}, для просмотра всех команд напиши {Fore.LIGHTGREEN_EX}{prefix}help{Fore.WHITE}.
                              {Fore.LIGHTBLACK_EX}[{nsign}{Fore.LIGHTBLACK_EX}] {Fore.WHITE}Снайпер нитро {nsniper}{Fore.WHITE}.
                              {Fore.LIGHTBLACK_EX}[{gsign}{Fore.LIGHTBLACK_EX}] {Fore.WHITE}Снайпер розыгрышей {gsniper}{Fore.WHITE}.
                                
                                    ''' + Fore.RESET)

        bot.run(token, bot=False)

    def nitro_sniper(self, nitrosniper_sign, nitrosniper):
        if nitrosniper == "true":
            nitrosniper_sign = f"{Fore.LIGHTGREEN_EX}!"
            nitrosniper = f"{Fore.LIGHTGREEN_EX}включен"
            return nitrosniper_sign, nitrosniper

        elif nitrosniper == "false":
            nitrosniper_sign = f"{Fore.LIGHTRED_EX}-"
            nitrosniper = f"{Fore.LIGHTRED_EX}выключен"
            return nitrosniper_sign, nitrosniper
        else:
            nitrosniper_sign = f"{Fore.LIGHTYELLOW_EX}?"
            nitrosniper = f"{Fore.LIGHTYELLOW_EX}ошибка"
            return nitrosniper_sign, nitrosniper

        
    def giveaway_sniper(self, giveawaysniper_sign, giveawaysniper):
        if giveawaysniper == "true":
            giveawaysniper = f"{Fore.LIGHTGREEN_EX}!"
            giveawaysniper = f"{Fore.LIGHTGREEN_EX}включен"
            return giveawaysniper_sign, giveawaysniper

        elif giveawaysniper == "false":
            giveawaysniper = f"{Fore.LIGHTRED_EX}-"
            giveawaysniper = f"{Fore.LIGHTRED_EX}выключен"
            return giveawaysniper_sign, giveawaysniper
        else:
            giveawaysniper_sign = f"{Fore.LIGHTYELLOW_EX}?"
            giveawaysniper = f"{Fore.LIGHTYELLOW_EX}ошибка"
            return giveawaysniper_sign, giveawaysniper

    def check_token(self, authorization):
        headers = {'Content-Type': 'application/json', 'authorization': authorization}
        url = "https://discordapp.com/api/v6/users/@me/library"
        r = requests.get(url, headers=headers)
        if r.status_code == 200:
            token = authorization
            return token
        else:
            print("Проверь /zeenode/config.py там либо неверный токен, либо его там нету!)")
            print("Напиши тут правильный токен:")
            token_input = input()
            token = token_input
            return token
    def load_cogs(self):
         # Загрузка команд
        bot.load_extension("zeenode.cogs.fun")
        bot.load_extension("zeenode.cogs.main")
        bot.load_extension("zeenode.cogs.activity")
        bot.load_extension("zeenode.cogs.text_encoding")
        bot.load_extension("zeenode.cogs.mass")
        bot.load_extension("zeenode.cogs.currency")
        bot.load_extension("zeenode.cogs.emoticons")
        bot.load_extension("zeenode.cogs.nsfw")
        # Загрузка ивентов
        bot.load_extension("zeenode.events.on_message")
