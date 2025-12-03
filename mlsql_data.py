# import pandas as pd
# import sqlalchemy


# engine = sqlalchemy.create_engine("mysql+pymysql://ArshMohanNishant:anannya3011@@localhost:3306/arsh_mohan")

# query = "SELECT * FROM students;"
# df = pd.read_sql(query, engine)
# df.to_csv("data/students_data.csv", index=False)

# print("Data collected and saved as 'students_data.csv'")
# print(df.head())

import pymysql

try:
    conn = pymysql.connect(
        host="localhost",
        user="ArshMohanNishant",
        password="anannya3011@",
        database="arsh_mohan"
    )
    with conn.cursor() as cur:
        cur.execute("SELECT DATABASE();")
        db_name = cur.fetchone()
        print(f"✅ Connected successfully to database: {db_name[0]}")
except Exception as e:
    print("❌ Connection failed:", e)
finally:
    if 'conn' in locals() and conn.open:
        conn.close()
