import mysql.connector

# Establish the connection
conn = mysql.connector.connect(
  user = '<username>@<server>', 
  password = '<password>', 
  host = '<server>.mysql.database.azure.com', 
  database = '<demodb>'
)

# Create a cursor object using the cursor() method
cursor = conn.cursor()

# Drop previous table of same name if one exists
cursor.execute("DROP TABLE IF EXISTS library")

# Create a table
cursor.execute("CREATE TABLE library (id INT AUTO_INCREMENT PRIMARY KEY, title VARCHAR(50), author VARCHAR(50), genre VARCHAR(50), quantity INTEGER)")

# Open the file and insert data
fname = 'books.txt'
with open(fname) as fh:
    for line in fh:
        parts = line.strip().split(", ")
        title = parts[0]
        author = parts[1]
        genre = parts[2]
        quantity = parts[3]

        # Insert some data into table
        cursor.execute("INSERT INTO library (title, author, genre, quantity) VALUES (%s, %s, %s, %s)", (title, author, genre, quantity))

# Read data
cursor.execute("SELECT * FROM library")
rows = cursor.fetchall()
print("Read", cursor.rowcount, "row(s) of data.")

# Print all rows
for row in rows:
  print(str(row[0]) + ". " + row[1] + " by " + row[2])
  print("Genre: " + row[3] + " Quantity: " + str(row[4]))

# Update quantity
cursor.execute("UPDATE library SET quantity = quantity - 1 WHERE id = %s", (18, ))
print("Updated",cursor.rowcount,"row(s) of data.")

cursor.execute("UPDATE library SET quantity = quantity + 1 WHERE id = %s OR id = %s", (10, 22))
print("Updated",cursor.rowcount,"row(s) of data.")

# Read data
cursor.execute("SELECT * FROM library")
rows = cursor.fetchall()
print("Read", cursor.rowcount, "row(s) of data.")

# Print all rows
for row in rows:
  print(str(row[0]) + ". " + row[1] + " by " + row[2])
  print("Genre: " + row[3] + " Quantity: " + str(row[4]))

# Cleanup
conn.commit()
cursor.close()
conn.close()
print("Done.")