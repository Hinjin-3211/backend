import pymysql.cursors
import logging

connection = pymysql.connect(
    host="localhost",  # 数据库主机地址
    user="root",  # 数据库用户名
    password="",  # 数据库密码
    database="softwarecup",  # 数据库名称
    charset="utf8mb4",  # 设置字符编码
    cursorclass=pymysql.cursors.DictCursor,  # 返回结果为字典格式
)


def select(sql, params=None):
    try:
        with connection.cursor() as cursor:
            cursor.execute(sql, params)
            logging.info(f"执行{sql},{params}语句")
            return cursor.fetchall()
    except Exception as e:
        logging.error(f"执行{sql},{params}语句异常")
        logging.error(e)
        return []
