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
cursor.execute("DROP TABLE IF EXISTS books")

# Create table
cursor.execute("CREATE TABLE books (id INT AUTO_INCREMENT PRIMARY KEY, title VARCHAR(50), author VARCHAR(50), genre VARCHAR(50))")
print("Finished creating table.")

# Insert some data into table
cursor.execute("INSERT INTO books (title, author, genre) VALUES (%s, %s, %s)", ("East of Eden", "John Steinbeck", "Novel"))
cursor.execute("INSERT INTO books (title, author, genre) VALUES (%s, %s, %s)", ("The Alchemist", "Paulo Coelho", "Novel"))
cursor.execute("INSERT INTO books (title, author, genre) VALUES (%s, %s, %s)", ("The Picture of Dorian Gray", "Oscar Wilde", "Drama"))
cursor.execute("INSERT INTO books (title, author, genre) VALUES (%s, %s, %s)", ("1984", "George Orwell", "Novel"))

# Insert multiple rows
sql = "INSERT INTO books (title, author, genre) VALUES (%s, %s, %s)"
values = [
  ("The Grapes of Wrath", "John Steinbeck", "Novel"),
  ("Of Mice and Men", "John Steinbeck", "Novel"),
  ("The Great Gatsby", "F. Scott Fitzgerald", "Novel"),
  ("Animal Farm", "George Orwell", "Political satire"),
  ("The Adventures of Huckleberry Finn", "Mark Twain", "Novel"),
  ("Little Women", "Louisa May Alcott", "Novel"),
  ("Hamlet", "William Shakespeare", "Tragedy"),
  ("The Stranger", "Albert Camus", "Novel"),
  ("Farmer Giles of Ham", "J. R. R. Tolkien", "Children's literature"),
  ("Moby Dick", "Herman Melville", "Novel"),
  ("The Lord of the Rings", "J. R. R. Tolkien", "Fantasy")
]
cursor.executemany(sql, values)

# Read data
cursor.execute("SELECT * FROM books")
rows = cursor.fetchall()

# Print all rows
print("\nBOOKS:\n")
for row in rows:
  print(row)

# Update a data row in the table
cursor.execute("UPDATE books SET genre = %s WHERE title = %s", ("Allegorical novella", "Animal Farm"))

# Read data
cursor.execute("SELECT * FROM books")
rows = cursor.fetchall()

# Print all rows
print("\nBOOKS:\n")
for row in rows:
  print(row)

# Delete a data row in the table
cursor.execute("DELETE FROM books WHERE title = %s", ("Hamlet", ))

# Delete data rows in the table
cursor.execute("DELETE FROM books WHERE author = %s OR author = %s", ("J. R. R. Tolkien", "Mark Twain"))

# Read data
cursor.execute("SELECT * FROM books")
rows = cursor.fetchall()

# Print all rows
print("\nBOOKS:\n")
for row in rows:
  print(row)

# Cleanup
conn.commit()
cursor.close()
conn.close()
print("Done.")