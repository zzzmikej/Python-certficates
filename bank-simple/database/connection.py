import database as database
import config as config

connection = database.create_server_connection(config.host, config.user, config.passwd)
create_database_query = """CREATE DATABASE IF NOT EXISTS {};""".format(config.bank)

database.create_database(connection, create_database_query)