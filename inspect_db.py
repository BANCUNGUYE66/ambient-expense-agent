import sqlite3

# Connect to the local database file
conn = sqlite3.connect("agent_sessions.db")
cursor = conn.cursor()

# Get list of tables
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()
print("Tables in database:", [t[0] for t in tables])

# Print rows from sessions table if it exists
try:
    cursor.execute("SELECT * FROM sessions;")
    sessions = cursor.fetchall()
    print(f"\nFound {len(sessions)} stored sessions:")
    for row in sessions:
        print(row)
except Exception as e:
    print("\nCould not query sessions table yet:", e)

conn.close()