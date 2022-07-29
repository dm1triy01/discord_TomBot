import psycopg2


# from itertools import chain
# from datetime import date, datetime
# import re

# Database requests
class db:

    def __init__(self):
        self.connection = psycopg2.connect(
            database="",
            user="postgres",
            password="3400",
            host="127.0.0.1",
            port="5432"
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

    # def check_user(self, id):
    #     with self.connection:
    #         self.cursor.execute("select Score from [User] where Id = '" + str(id) + "'")
    #         result = self.cursor.fetchall()
    #         return bool(len(result))
    #
    # def add_user(self, id):
    #     with self.connection:
    #         return self.cursor.execute("insert into [User] values(" + str(id) + " ,1000, 10)")
    #
    # def get_score(self, id):
    #     self.cursor.execute("select Score from [User] where Id = '" + str(id) + "'")
    #     list = self.cursor.fetchall()
    #     result = ''.join(map(str, chain.from_iterable(list)))
    #     print('get_score')
    #     return result
    #
    # def add_date(self, id, ddate, text):
    #     with self.connection:
    #         self.cursor.execute("")
    #
    # def check_date(self, dd, mm):
    #     with self.connection:
    #         self.cursor.execute("select")
