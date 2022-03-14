import logging
import random
import time
import psycopg2
from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'hello world'

@app.route('/sensor/<name>')
def sensor_data(name):
    conn = psycopg2.connect(
            database="database", user="user", password="password", host="postgres", port="5432")
    cur = conn.cursor()
    limit = request.args.get('limit', default =15, type = int)
    query = f"""
    select * from measurement where sensor_name = '{name}' limit {limit} 
    """
    cur.execute(query)
    result = cur.fetchall()
    print('result below')
    print(result)
    return jsonify(result)


if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)

#        try:
#            # connect to the PostgreSQL server
#            conn = psycopg2.connect(
#                database="database", user="user", password="password", host="postgres", port="5432")
#
#            cur = conn.cursor()
#
#            query = f"""
#            INSERT INTO measurement (sensor_name,sensor_value) \
#            VALUES ('{str(response[b'sensor'],'utf-8')}', {float(response[b'value'])})
#            """
#
#            cur.execute(query)
#
#            cur.close()
#
#            conn.commit()
#        except (Exception, psycopg2.DatabaseError) as error:
#            print(error)
#        finally:
#            if conn is not None:
#                conn.close()
