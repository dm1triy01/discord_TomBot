import mysql.connector
from mysql.connector import Error

import cfg


# Database requests
class db:

    def __init__(self):
        self.connection = mysql.connector.connect(
            host=cfg.server,
            user=cfg.username,
            passwd=cfg.password,
            database=cfg.database,
        )
        self.cursor = self.connection.cursor(buffered=True)
        # cmd = 'select * from guilds'
        # for result in self.cursor.execute(operation=cmd, multi=True):
        #     if result.with_rows:
        #         print("Rows produced by statement '{}':".format(
        #             result.statement))
        #         print(result.fetchall())
        #     else:
        #         print("Number of rows affected by statement '{}': {}".format(
        #             result.statement, result.rowcount))

    def guild_add(self, guild_id, name, status):
        self.check_connection()
        check = self.guild_exist(guild_id=guild_id)
        if check:
            self.cursor.execute('UPDATE guilds SET status=\'' + str(status) + '\' WHERE id_guild=' + str(guild_id),
                                multi=True)
            self.connection.commit()
        else:
            self.cursor.execute(
                'INSERT INTO guilds (id_guild, name_guild, status) VALUES (' + str(guild_id) + ', \'' + str(
                    name) + '\',\'' + str(status) + '\')', multi=True)
            self.connection.commit()

    def guild_remove(self, guild_id, status):
        self.check_connection()
        self.cursor.execute('UPDATE guilds SET status=\'' + str(status) + '\' WHERE id_guild=' + str(guild_id),
                            multi=True)
        self.connection.commit()

    def guild_exist(self, guild_id):
        self.check_connection()
        for result in self.cursor.execute('select id from guilds where id_guild=' + str(guild_id), multi=True):
            if result.with_rows:
                check = result.fetchall()
        return ''.join(map(str, check[0]))

    def voice_commands_get(self, id_g):
        self.check_connection()
        for result in self.cursor.execute('select name from music_commands where id_g=' + str(id_g), multi=True):
            if result.with_rows:
                check = result.fetchall()
        return str(check)

    def voice_path_get(self, id_g, command):
        self.check_connection()
        # test = 'select pic from music_commands where id_g=' + str(id_g) + 'AND command=\'' + str(command) + '\''
        # print(test)
        for result in self.cursor.execute(
                'select path from music_commands where id_g=' + str(id_g) + ' AND name=\'' + str(command) + '\'',
                multi=True):
            if result.with_rows:
                check = result.fetchall()
        return ''.join(map(str, check[0]))

    def voice_pic_get(self, id_g, command):
        self.check_connection()
        for result in self.cursor.execute(
                'select pic from music_commands where id_g=' + str(id_g) + ' AND name=\'' + str(command) + '\'',
                multi=True):
            if result.with_rows:
                check = result.fetchall()
        return ''.join(map(str, check[0]))

    def voice_amount_get(self, id_g, command):
        self.check_connection()
        for result in self.cursor.execute(
                'select amount from music_commands where id_g=' + str(id_g) + ' AND name=\'' + str(command) + '\'',
                multi=True):
            if result.with_rows:
                check = result.fetchall()
        return ''.join(map(str, check[0]))

    def channel_afk_get(self, id_g):
        self.check_connection()
        for result in self.cursor.execute('select id_afk from channels where id_g=' + str(id_g), multi=True):
            if result.with_rows:
                check = result.fetchall()
        return ''.join(map(str, check[0]))

    def channel_general_get(self, id_g):
        self.check_connection()
        for result in self.cursor.execute('select id_general from channels where id_g=' + str(id_g), multi=True):
            if result.with_rows:
                check = result.fetchall()
        return ''.join(map(str, check[0]))

    def check_connection(self):
        if self.connection.is_connected():
            pass
        else:
            self.connection = mysql.connector.connect(
                host=cfg.server,
                user=cfg.username,
                passwd=cfg.password,
                database=cfg.database,
            )
            self.cursor = self.connection.cursor(buffered=True)

    def bot_status_get(self):
        self.check_connection()
        for result in self.cursor.execute('select status from bot_info', multi=True):
            if result.with_rows:
                check = result.fetchall()
        return ''.join(map(str, check[0]))

    def bot_status_mod(self, text):
        self.check_connection()
        self.cursor.execute('UPDATE bot_info SET status=\'' + str(text) + '\' WHERE id=1', multi=True)
        self.connection.commit()
