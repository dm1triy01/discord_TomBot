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

    def guild_add(self, id, name, status):
        # with self.connection:
        # cursor = self.connection.cursor()
        print(status)
        cmd = 'INSERT INTO guilds (id_guild, name_guild, status) VALUES (' + str(id) + ', \'' + str(
            name) + '\',\'' + str(status) + '\')'
        print(cmd)
        self.cursor.execute(operation=cmd, multi=True)
        self.connection.commit()

    def guild_remove(self, id, status):
        self.cursor.execute('UPDATE guilds SET status=\'' + str(status) + '\' WHERE id_guild=' + str(id), multi=True)
        self.connection.commit()
