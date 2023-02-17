import sqlite3

# Connect to the database
conn = sqlite3.connect('myapp.db')
c = conn.cursor()

def search_database(command):
    # Execute a SQL query to retrieve data from the database based on the command
    c.execute("SELECT * FROM my_table WHERE command=?", (command,))
    result = c.fetchone()

    # Return the result
    if result:
        return result[1]  # Assuming the response is stored in the second column of the table
    else:
        return "Sorry, I didn't understand your command."

# Close the database connection
conn.close()
