import psycopg2

class PostgreSQLDatabase:
    def __init__(self, dbname, user, password, host='localhost', port=5432):
        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.conn = None

    def connect(self):
        self.conn = psycopg2.connect(
            dbname=self.dbname,
            user=self.user,
            password=self.password,
            host=self.host,
            port=self.port
        )
        self.conn.autocommit = True

    def close(self):
        if self.conn is not None:
            self.conn.close()
            self.conn = None

    def execute(self, query, *params):
        with self.conn.cursor() as cur:
            cur.execute(query, params)
            return cur.fetchall()


test = PostgreSQLDatabase('postgres' , 'postgres' , '1234')
test.connect()
print(test.execute(''''''))


