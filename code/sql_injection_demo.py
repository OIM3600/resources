import sqlite3


def initilize_db():
    """
    Initialize the SQLite database and create the 'users' table if it doesn't exist.
    Insert demo records into the 'users' table.
    """
    # Connect to the SQLite database
    conn = sqlite3.connect(
        "data/sql_injection_example.db",
    )

    # Create a cursor object
    cursor = conn.cursor()

    # create users table
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            password TEXT NOT NULL
        )
    """
    )

    # insert demo records
    cursor.execute(
        "INSERT INTO users (username, password) VALUES (?, ?)", ("user1", "password1")
    )
    cursor.execute(
        "INSERT INTO users (username, password) VALUES (?, ?)", ("user2", "password2")
    )
    conn.commit()

    cursor.close()
    conn.close()


def select_all(cursor):
    """
    Select and print all records from the 'users' table.
    """
    cursor.execute("SELECT * FROM users")
    results = cursor.fetchall()
    for row in results:
        print(row)


def unsafe_login(cursor):
    """
    Simulate an unsafe login attempt by constructing a query with user-provided input.
    This code is susceptible to SQL injection.
    """
    # User-provided input
    username = "John"
    # password = 'password'
    password = "wrong_password' OR '1'='1'--"

    # Unsafe practice: Constructing the query using string concatenation
    query = (
        f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    )

    # Execute the query
    cursor.execute(query)

    # Fetch the results
    result = cursor.fetchall()

    # Process the query results
    if len(result) > 0:
        print("Login successful")
    else:
        print("Login failed")


def safe_login(cursor):
    """
    Simulate a safe login attempt by using a parameterized query to prevent SQL injection.
    """
    # User-provided input
    username = "John"
    # password = 'password'
    password = "wrong_password' OR '1'='1'--"

    # Execute the query using parameterized query
    # Note: In a real application, user input should not be directly inserted into the query
    # We are doing this for demonstration purposes only
    query = "SELECT * FROM users WHERE username = ? AND password = ?"

    # Execute the query
    cursor.execute(query, (username, password))

    # Fetch the results
    result = cursor.fetchall()

    # Process the query results
    if len(result) > 0:
        print("Login successful")
    else:
        print("Login failed")


def main():
    """"""
    # initilize_db()

    with sqlite3.connect("data/sql_injection_example.db") as conn:
        cursor = conn.cursor()
        # select_all(cursor)
        # unsafe_login(cursor)
        # safe_login(cursor)


if __name__ == "__main__":
    main()
