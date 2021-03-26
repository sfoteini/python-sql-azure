import mysql.connector

# Establish the connection
conn = mysql.connector.connect(
  user = '<username>@<server>', 
  password = '<password>', 
  host = '<server>.mysql.database.azure.com', 
  database = '<demodb>'
)

print(conn)