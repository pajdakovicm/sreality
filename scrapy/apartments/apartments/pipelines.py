import psycopg2
from psycopg2.extras import Json


# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface

class ApartmentsPipeline:

    def __init__(self):
        # print("dal sam tuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu?")
        self.conn = None
        try:
            # read the connection parameters
            hostname = 'localhost'
            username = 'postgres'
            password = 'ntkntk'  # your password
            database = 'apartments'

            # connect to the PostgreSQL server
            self.conn = psycopg2.connect(host=hostname, user=username, password=password, dbname=database)
            self.cur = self.conn.cursor()
            # delete the table if it already exists
            self.cur.execute("DROP TABLE IF EXISTS maki;")
            # create table
            self.cur.execute("CREATE TABLE maki (name VARCHAR(255) , image text);")
            # commit the changes
            self.conn.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

    def process_item(self, item, spider):
        # print("OHOOOOOOOOOOOOOOOO00000000000000OO MOJ ITEM JE:", item)
        # print("JESAM LI PROCESIROOOOOOOOOOOOOOOOOOOOOOOOOO")
        # print("jason item", [Json(item)])
        # define column names
        postgres_insert_query = """ INSERT INTO maki (name,image) VALUES (%s,%s)"""
        # Define insert statement
        print("ITEM IME JE", item['name:'])
        try:
            self.cur.execute(postgres_insert_query, ([Json(item['name:'])], [Json(item['image:'])]))
            self.conn.commit()
            # print("komitovo")
        except (Exception, psycopg2.Error) as error:
            print("Failed to insert record into apartments table", error)
        return item

    def close_spider(self, spider):
        # Close cursor & connection to database
        self.cur.close()
        print("check connection", self.conn.close())
        print("PostgreSQL connection is closed")
