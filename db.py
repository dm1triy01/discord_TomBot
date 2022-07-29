import psycopg2

# from itertools import chain
# from datetime import date, datetime
# import re

import cfg


# Database requests
class db:

    def __init__(self):
        self.connection = psycopg2.connect(
            database=cfg.database,
            user=cfg.user,
            password=cfg.password,
            host=cfg.host,
            port=cfg.port
        )
        self.cursor = self.connection.cursor()

    def guild_add(self, id, name):
        with self.connection:
            self.cursor.execute("")
            self.cursor.execute("")
            return 0

    def guild_remove(self, id):
        with self.connection:
            self.cursor.execute("")
            return 0
