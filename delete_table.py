from mysql.connector import connect, Error
import os
from os.path import join, dirname
from dotenv import load_dotenv, find_dotenv
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)


connection = connect(database=os.environ.get("DB_USER"), 
                               user=os.environ.get("DB_USER"), 
                               password=os.environ.get("DB_PASSWORD"), 
                               host=os.environ.get("DB_HOST"))
cursor = connection.cursor()
cursor.execute("TRUNCATE TABLE articles")
connection.commit()
connection.close()