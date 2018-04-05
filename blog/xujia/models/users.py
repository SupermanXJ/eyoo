from django.db import connection
import time
import logging


class Users:
    @staticmethod
    def register(email, password):
        now = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        sql = "insert into users(email, password, createTime) values ('%s', '%s', '%s')" % (email, password, now)
        cursor = connection.cursor()
        cursor.execute(sql)

    @staticmethod
    def get_login_user(email, password):
        sql = "select id, name, email from users where email = '%s' and password = '%s'" % (email, password)
        cursor = connection.cursor()
        cursor.execute(sql)
        return cursor.fetchone()
