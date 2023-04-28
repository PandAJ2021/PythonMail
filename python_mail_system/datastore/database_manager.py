from utils.database_connector import PostgreSQLDatabase

class DatabaseHandler:

    def __init__(self, table_name: str, database=PostgreSQLDatabase):
        self.table_name = table_name
        self.database = database

    def create_table(self, data: dict):
        query = f'CREATE TABLE IF NOT EXISTS {self.table_name} ('
        query += ','.join([f'{col} {data[col]}' for col in data])
        query += ');'

        self.database.connect()
        self.database.execute(query)
        self.database.close()

    def insert(self, data: dict):
        columns = ','.join(data.keys())
        values = ','.join(data.values())
        #converter = lambda x : f"'{x}'" if isinstance(x ,str) else str(x)
        #values = ','.join(map( converter, data.values()))
        query = f"INSERT INTO {self.table_name}" + \
            f"({columns})" + f'\n VALUES({values});'
        self.database.connect()
        cur = self.database.conn.cursor()
        cur.execute(query)
        cur.execute("SELECT lastval();") # set this to give the last id.
        inserted_id = cur.fetchone()[0] 
        cur.close()
        self.database.close()

        return inserted_id

    def read(self, columns ="*" ,  condition=None):
        query = f"SELECT {columns} FROM {self.table_name}"
        if condition:
            query += f' WHERE {condition}'
        query += ';'

        self.database.connect()
        return self.database.execute(query)
        # self.cur.close() # i dont check that still

    def update(self, data: dict, condition: str):

        query = f'UPDATE {self.table_name} SET '
        query += ', '.join([f"{col}={data[col]}" for col in data])
        query += f' WHERE {condition} ;'

        self.database.connect()
        self.database.execute(query)
        self.database.close()

    def delete(self, condition: str):
        query = f'DELETE FROM {self.table_name} WHERE {condition}'

        self.database.connect()
        self.database.execute(query)
        self.database.close()

    def join_all(self, columns ="*" ,  condition=None):
        query = f"SELECT {columns} FROM users "
        query += "JOIN emailes ON users.user_id = emailes.sender_id "
        if condition:
            query += f' WHERE {condition}'
        query += ';'

        self.database.connect()
        return self.database.execute(query)
