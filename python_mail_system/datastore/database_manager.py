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
            if cur.description is not None:  # handle a cursor that has not executed a SELECT statement
                return cur.fetchall()


class DatabaseHandler:

    def __init__(self , table_name:str , database = PostgreSQLDatabase):
        self.table_name = table_name
        self.database = database

    def create_table(self , data: dict):
        query = f'CREATE TABLE IF NOT EXISTS {self.table_name} ('
        query += ','.join([f'{col} {data[col]}' for col in data])
        query += ');'

        self.database.connect()
        self.database.execute(query)
        self.database.close()

    def insert(self, data: dict):
        columns = ','.join(data.keys()) 
        values = ','.join(data.values()) 
        query = f"INSERT INTO {self.table_name}" + \
            f"({columns})" + f'\n VALUES({values});'

        self.database.connect()
        self.database.execute(query)
        self.database.close()

    def read(self, condition=None):
        query = f"SELECT * FROM {self.table_name}"
        if condition:
            query += f' WHERE {condition}'
        query += ';'

        self.database.connect()
        return self.database.execute(query)

    @staticmethod
    def update(self , data: dict,condition: str):

        query = f'UPDATE {self.table_name} SET '
        query += ', '.join([f"{col}=%s" for col in data])
        query += ') '
        query += f' WHERE {condition} ;'

        self.database.connect()
        self.database.execute(query)
        self.database.close()

    def delete(condition: str):
        query = f'DELETE FROM {self.table_name} WHERE {condition}'

        self.database.connect()
        self.database.execute(query)
        self.database.close()


# test = PostgreSQLDatabase('postgres', 'postgres', '1234')
# data = {
#     'id' : 'bigserial',
#     'name': 'varchar(80)',
#     'age': 'int'
# }
# DatabaseHandler('test2' ,test ).create_table(data)
# # print(DatabaseHandler.read('test' ,database=test))
# # insert_data = {


# # }
# # DatabaseHandler.insert('test', data)
