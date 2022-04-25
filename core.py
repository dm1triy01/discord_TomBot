from datetime import date, datetime, timedelta
import re
import random

import answers


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
    return dimatmp


async def message_handler(message):
    channel = message.channel
    if channel == message.channel:  # данный if исключает повторное вызывание команд бота
        today = datetime.today()
        print(today.strftime("%Y.%m.%d %H:%M"))
        print('(' + str(message.channel) + ')' + str(message.author) + ': ' + str(message.content))
        #  if message.content.startswith('Том') or message.content.startswith('Tom'):
        if re.match(r'Том\b', message.content) is not None or re.match(r'Tom\b', message.content) is not None:
            await channel.send(random.choice(answers.hi_list))
        #  if message.content.startswith('том') or message.content.startswith('tom'):
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