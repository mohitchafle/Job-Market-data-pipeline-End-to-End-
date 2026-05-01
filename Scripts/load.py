import pandas as pd
import mysql.connector
from config.db_config import DB_CONFIG

def load_to_mysql():
    df = pd.read_csv("data/processed_jobs.csv")

    conn = mysql.connector.connect(**DB_CONFIG)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS jobs (
            id INT AUTO_INCREMENT PRIMARY KEY,
            title TEXT,
            company TEXT,
            location TEXT,
            salary_min FLOAT,
            salary_max FLOAT,
            category TEXT,
            created DATETIME
        )
    """)

    for _, row in df.iterrows():
        cursor.execute("""
            INSERT INTO jobs (title, company, location, salary_min, salary_max, category, created)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, tuple(row))

    conn.commit()
    cursor.close()
    conn.close()

    print("Data loaded into MySQL!")

if __name__ == "__main__":
    load_to_mysql()