import pymysql

DB_URL = "awseb-e-prhh5r9jvy-stack-awsebrdsdatabase-ylssjjs9wlx5.csuwvducqdwy.eu-west-1.rds.amazonaws.com"
DB_PORT = 3306
DB_USER = "david"
DB_PASSWORD = "extrem0403"
DB_SCHEMA = "ebdb"


class DBHandler:
    def __init__(self):
        self.connection = pymysql.connect(host=DB_URL,
                                          user=DB_USER,
                                          password=DB_PASSWORD,
                                          database=DB_SCHEMA,
                                          charset='utf8mb4',
                                          cursorclass=pymysql.cursors.DictCursor)

    def execute(self, query):
        with self.connection.cursor() as cursor:
            cursor.execute(query)
            self.connection.commit()
        return cursor.fetchall()

    def close(self):
        self.connection.close()
