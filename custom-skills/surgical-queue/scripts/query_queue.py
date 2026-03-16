import psycopg2
import sys

conn = psycopg2.connect(
    host="db",
    database="hospital",
    user="user",
    password="password"
)

cur = conn.cursor()

cur.execute("""
SELECT patient_name, procedure, priority, scheduled_date, status
FROM surgical_queue
ORDER BY priority DESC, scheduled_date
LIMIT 20
""")

rows = cur.fetchall()

for r in rows:
    print(f"Patient: {r[0]}")
    print(f"Procedure: {r[1]}")
    print(f"Priority: {r[2]}")
    print(f"Scheduled: {r[3]}")
    print(f"Status: {r[4]}")
    print("------")
