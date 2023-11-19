import pymysql

DB_URL = "AWS_RDS_URL"
DB_PORT = 3306  # default port
DB_USER = "DATABASE_USER"
DB_PASSWORD = "DATABASE_PASSWORD"
DB_SCHEMA = "MAIN_DB"


class DBHandler:
    def __init__(self):  # connect to the database
        self.connection = pymysql.connect(host=DB_URL,
                                          user=DB_USER,
                                          password=DB_PASSWORD,
                                          database=DB_SCHEMA,
                                          charset='utf8mb4',
                                          cursorclass=pymysql.cursors.DictCursor)

    def execute(self, query):  # execute a query
        with self.connection.cursor() as cursor:
            cursor.execute(query)
            self.connection.commit()
        return cursor.fetchall()

    def close(self):  # close the connection
        self.connection.close()
