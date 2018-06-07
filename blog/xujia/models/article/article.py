import time
from django.db import connection
import pymysql
import logging


class Article:
    @staticmethod
    def get_list(user_id, page_size=10, page_index=0, order_by='create_time desc'):
        sql = "select * from article where user_id = '%s' order by %s limit %d, %d " % (user_id, order_by, page_size * page_index, page_size)
        cursor = connection.cursor()
        cursor.execute(sql)
        desc = cursor.description
        return [
            dict(zip([col[0] for col in desc], row)) for row in cursor.fetchall()
        ]
