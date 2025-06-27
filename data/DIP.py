

class Database:
    def connection(self):
        # This method should return a database connection
        pass    


class MySQLDatabase(Database):
    def connection(self):
        # This method should return a MySQL database connection
        pass


class PostgreSQLDatabase(Database): 
    def connection(self):
        # This method should return a PostgreSQL database connection
        pass

class SQLiteDatabase(Database):
    def connection(self):
        # This method should return a SQLite database connection
        pass


class MongoDBDatabase(Database):
    def connection(self):
        # This method should return a MongoDB database connection
        pass



class GetOrders:
    def __init__(self, db:Database):
        self.db = db  # or PostgreSQLDatabase(), SQLiteDatabase(), MongoDBDatabase() 

    def get_orders(self):
        connection = self.db.connection()
        # Logic to fetch orders from the database using the connection
        pass


def helper():
    db = MySQLDatabase()  # or PostgreSQLDatabase(), SQLiteDatabase(), MongoDBDatabase()
    orders = GetOrders(db)
    orders.get_orders()