import psycopg2
import json
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface

from itemadapter import ItemAdapter
from psycopg2._json import Json


def create_tables():
    """ create tables in the PostgreSQL database"""
    commands = (
        """
        CREATE TABLE flats (
            name VARCHAR(255) PRIMARY KEY,
            image url VARCHAR(255) NOT NULL
        ) """
    )
    conn = None
    try:
        # read the connection parameters
        hostname = 'localhost'
        username = 'postgres'
        password = 'ntkntk'  # your password
        database = 'apartments'

        # connect to the PostgreSQL server
        conn = psycopg2.connect(host=hostname, user=username, password=password, dbname=database)
        cur = conn.cursor()
        # create table one by one
        for command in commands:
            cur.execute(command)
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


class ApartmentsPipeline:
    def __init__(self):
        ## Connection Details
        hostname = 'localhost'
        username = 'postgres'
        password = 'ntkntk'  # your password
        database = 'apartments'

        ## Create/Connect to database
        self.connection = psycopg2.connect(host=hostname, user=username, password=password, dbname=database)

        ## Create cursor, used to execute commands
        self.cur = self.connection.cursor()

    def process_item(self, item, spider):
        print("OHOOOOOOOOOOOOOOOO00000000000000OO MOJ ITEM JE:", item)

        name = str(item['name:'])
        img = item['image:']
        postgres_insert_query = """ INSERT INTO apartments (name) VALUES (%s)"""
        record_to_insert = name

        # print(name,img)
        print("ja sam posle")

        ## Define insert statement
        try:
            self.cur.execute(postgres_insert_query, (record_to_insert,))

            ## Execute insert of data into database
            self.connection.commit()
            print("komitovo")
        except (Exception, psycopg2.Error) as error:
            print("Failed to insert record into apartments table", error)

        return item

    def close_spider(self, spider):
        ## Close cursor & connection to database
        self.cur.close()
        print("check connection", self.connection.close())
        print("PostgreSQL connection is closed")
