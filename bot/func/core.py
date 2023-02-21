from datetime import date, datetime
import re
import random

# import answers
from bot import answers
import cfg


def datecheck(yy, mm, dd):
    dimadate = date(yy, mm, dd)
    dimatoday = date.today()
    dima = dimadate - dimatoday
    dimatmp: int = dima.days
    d = 0
    while dimatmp < 0:
        dimatmp = dimatmp + 365
        d = d + 1
        if d % 4 == 0:
            dimatmp = dimatmp + 1
    dimalist = list(str(dimatmp))
    if dimatmp < 10:
        number = dimalist[-1]
    else:
        number = dimalist[-2] + dimalist[-1]
    if 11 <= int(number) <= 19:
        word = "дней"
    else:
        if int(dimalist[-1]) == 1:
            word = "день"
        elif 2 <= int(dimalist[-1]) <= 4:
            word = "дня"
        else:
            word = "дней"
    return str(str(dimatmp) + " " + word)


async def message_handler(message):
    channel = message.channel
    if channel == message.channel:  # данный if исключает повторное вызывание команд бота
        today = datetime.today()
        print(today.strftime("%Y.%m.%d %H:%M"))
        print('(' + str(message.channel) + ')' + str(message.author) + ': ' + str(message.content))
        if re.match(r'Том\b', message.content) is not None or re.match(r'Tom\b', message.content) is not None:
            await channel.send(random.choice(answers.hi_list))
        if re.match(r'том\b', message.content) is not None or re.match(r'tom\b', message.content) is not None:
            await channel.send("А может с большой буквы ?")
        if re.match(r'\d+[ ][+][ ]\d+$', message.content) is not None or re.match(r'\d+[+]\d+$', message.content):
            l1 = re.split(r'[+]', message.content)
            l2 = re.split(r'[+]', message.content)
            for i, a in enumerate(l1):
                l1[1] = int(a)
            for j, b in enumerate(l2):
                l2[0] = int(b)
            c = int(a) + int(b)
            await channel.send(c)
        if re.match(r'\d+[ ][-][ ]\d+$', message.content) is not None or re.match(r'\d+[-]\d+$', message.content):
            l1 = re.split(r'[-]', message.content)
            l2 = re.split(r'[-]', message.content)
            for i, a in enumerate(l1):
                l1[1] = int(a)
            for j, b in enumerate(l2):
                l2[0] = int(b)
            c = int(a) - int(b)
            await channel.send(c)
        if re.match(r'\d+[ ][*][ ]\d+$', message.content) is not None or re.match(r'\d+[*]\d+$', message.content):
            l1 = re.split(r'[*]', message.content)
            l2 = re.split(r'[*]', message.content)
            for i, a in enumerate(l1):
                l1[1] = int(a)
            for j, b in enumerate(l2):
                l2[0] = int(b)
            c = int(a) * int(b)
            await channel.send(c)
        if re.match(r'\d+[ ][/][ ]\d+$', message.content) is not None or re.match(r'\d+[/]\d+$', message.content):
            l1 = re.split(r'[/]', message.content)
            l2 = re.split(r'[/]', message.content)
            for i, a in enumerate(l1):
                l1[1] = int(a)
            for j, b in enumerate(l2):
                l2[0] = int(b)
            if int(b) == 0:
                await channel.send('Пошел на хуй!')
            else:
                c = int(a) / int(b)
                await channel.send(c)
        if re.match(r'\d+["^"]\d+$', message.content) or re.match(r'[-]\d+["^"][-]\d+$', message.content) \
                or re.match(r'[-]\d+["^"]\d+$', message.content) or re.match(r'\d+["^"][-]\d+$', message.content):
            l1 = re.split(r'["^"]', message.content)
            l2 = re.split(r'["^"]', message.content)
            for i, a in enumerate(l1):
                l1[1] = int(a)
            for j, b in enumerate(l2):
                l2[0] = int(b)
            c = int(a) ** int(b)
            await channel.send(c)


async def danger_handler(message):
    channel = message.channel
    if channel == message.channel:  # данный if исключает повторное вызывание команд бота
        if channel.id == cfg.main_channel:
            if re.search("(?P<url>https?://[^\s]+)", message.content):
                url = re.search("(?P<url>https?://[^\s]+)", message.content).group(0)
                url = re.split('/', url)[2]
                with open(r'/root/bots/discord/rut/url_black.txt', 'r') as f:
                    url_black = f.readlines()
                    f.close()
                with open(r'/root/bots/discord/rut/url_white.txt', 'r') as f:
                    url_white = f.readlines()
                    f.close()
                if url in url_black:
                    await channel.purge(limit=1)
                    await channel.send(message.author.mention + " этот человек пытался отправить ссылку из черного листа! (Она удалена)")
                elif url in url_white:
                    pass
                else:
                    with open(r'/root/bots/discord/rut/url_tmp.txt', 'w') as f:
                        f.write(str(url))
                        f.close()
                    await channel.send(message.author.mention + " скинул неизвестную ссылку, осторожно!")
