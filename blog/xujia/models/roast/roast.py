import time
from django.db import connection
import pymysql
import logging


class Roast:
    @staticmethod
    def insert(user_id, content):
        now = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        sql = "insert into roast(user_id, content, create_time) values ('%s', '%s', '%s')" % (user_id, content, now)
        cursor = connection.cursor()
        cursor.execute(sql)

    @staticmethod
    def get_list(user_id):
        sql = "select * from roast where user_id = '%s' order by id desc" % user_id
        logging.debug(sql)
        logging.info(sql)
        cursor = connection.cursor()
        cursor.execute(sql)
        desc = cursor.description
        return [
            dict(zip([col[0] for col in desc], row)) for row in cursor.fetchall()
        ]
