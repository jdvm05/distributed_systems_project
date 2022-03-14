import logging
import random
import time

import numpy as np
import psycopg2
import redis


def create_tables():
    """ create tables in the PostgreSQL database"""

    conn = None

    try:
        # connect to the PostgreSQL server;
        conn = psycopg2.connect(
            database="database", user="user", password="password", host="postgres", port="5432")

        cur = conn.cursor()
        # create table one by one
        cur.execute("""
        CREATE TABLE measurement (
            id SERIAL PRIMARY KEY,
            sensor_name VARCHAR(255) NOT NULL,
            sensor_value DOUBLE PRECISION NOT NULL,
            created_at TIMESTAMPTZ DEFAULT Now()
        )
        """)

        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

create_tables()

r = redis.from_url('redis://redis:6379')

logger = logging.getLogger(__name__)

while True:
    logger.info("START PROCESSING")
    for id, (data,) in r.xread({"IOT": "$"}, count=1, block=300):
        logger.info("FO")
        response = data[1]
        print("receive:", response)

        try:
            # connect to the PostgreSQL server
            conn = psycopg2.connect(
                database="database", user="user", password="password", host="postgres", port="5432")

            cur = conn.cursor()

            query = f"""
            INSERT INTO measurement (sensor_name,sensor_value) \
            VALUES ('{str(response[b'sensor'],'utf-8')}', {float(response[b'value'])})
            """

            cur.execute(query)

            cur.close()

            conn.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()
