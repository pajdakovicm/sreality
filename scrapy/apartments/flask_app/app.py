import os
import psycopg2
from flask import Flask, render_template
#import numpy as np

app = Flask(__name__)

def tuples_to_list(tup):
    arr = []
    for item in tup:
        for i in range(2):
            arr.append(item[i])
    return arr

def get_db_connection():
    conn = psycopg2.connect(host='db',
                            user='postgres',
                            password='ntkntk',
                            port = '5432')
    return conn


@app.route('/')
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM "maki";')
    # save the data into the variable called items
    items = cur.fetchall()
    new_items = tuples_to_list(items)
    cur.close()
    conn.close()
    return render_template('index.html', new_items=new_items)
if __name__ == '__main__':
      app.run(host='0.0.0.0',port=8080,debug=True)