import pymysql


class SQL:
    def __init__(self):
        self.table = None
        self.connect = pymysql.connect(
            host='192.168.1.2',
            user='cleverboss',
            password='clever3366',
            database='biology',
            port=3307
        )
        self.cursor = self.connect.cursor()
        self.info = None

    def tables(self, table: str):
        self.table = table

    def __enter__(self):
        self.__init__()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cursor.close()
        self.connect.close()

    def __add__(self, other: dict):
        if type(other) is not dict:
            raise TypeError('输入一个字典,不是' + str(type(other)))
        for k, v in other.items():
            self.cursor.execute("INSERT INTO " + self.table + " (place,value,info) VALUES ('" + k + "','" + str(v) + "','" + self.info + "');")
