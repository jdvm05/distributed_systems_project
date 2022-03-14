import psycopg2
name = 'A'
conn = psycopg2.connect(
         database="database", user="user", password="password", host="localhost", port="5432")
cur = conn.cursor()
query = f"""
    select * from measurement where sensor_name = '{name}' LIMIT 10
    """
cur.execute(query)
result = cur.fetchall()
print('result below')
print(result)


