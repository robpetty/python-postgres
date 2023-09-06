import psycopg2

# Connect to the database
conn = psycopg2.connect(
    host="localhost",
    database="test_database",
    user="test_user",
    password="test_password",
)

# Create a cursor
cur = conn.cursor()

# Execute a query
cur.execute("SELECT * FROM users;")

# Fetch and print the results
records = cur.fetchall()
for row in records:
    print(row)

# Close the connection
conn.close()
