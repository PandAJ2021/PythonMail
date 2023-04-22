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

    @staticmethod
    def create_table(table_name: str, data: dict, database=PostgreSQLDatabase):
        query = f'CREATE TABLE IF NOT EXISTS {table_name} ('
        query += ','.join([f'{col} {data[col]}' for col in data])
        query += ');'

        database.connect()
        database.execute(query)
        database.close()

    @staticmethod
    def insert(table_name: str, data: dict, ddatabase=PostgreSQLDatabase):
        columns = ','.join(data.keys()) 
        values = ','.join(data.values()) 
        query = f"INSERT INTO {table_name}" + \
            f"({columns})" + f'\n VALUES({values});'

        database.connect()
        database.execute(query)
        database.close()

    @staticmethod
    def read(table_name: str, condition=None, database=PostgreSQLDatabase):
        query = f"SELECT * FROM {table_name}"
        if condition:
            query += f' WHERE {condition}'
        query += ';'

        database.connect()
        return database.execute(query)

    @staticmethod
    def update(data: dict, table_name: str, condition: str, database=PostgreSQLDatabase):

        query = f'UPDATE {table_name} SET '
        query += ', '.join([f"{col}=%s" for col in data])
        query += ') '
        query += f' WHERE {condition} ;'

        database.connect()
        database.execute(query)
        database.close()

    @staticmethod
    def delete(condition: str, database=PostgreSQLDatabase):
        query = f'DELETE FROM {table_name} WHERE {condition}'

        database.connect()
        database.execute(query)
        database.close()


test = PostgreSQLDatabase('postgres', 'postgres', '1234')
data = {
    'name': 'varchar(80)',
    'age': 'int'
}
DatabaseHandler.create_table('test' , data , test)
# print(DatabaseHandler.read('test' ,database=test))
insert_data = {


}
DatabaseHandler.insert('test', data)
