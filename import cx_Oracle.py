import cx_Oracle

def connect_to_oracle():
    # Connect to your Oracle Database
    cx_Oracle.init_oracle_client(lib_dir= r"D:\DB\dbhomeXE\bin")
    connection = cx_Oracle.connect("system", "keer")
    return connection

def login():
    connection = connect_to_oracle()
    cursor = connection.cursor()

    # Check user credentials in the database
    query = "SELECT * FROM test"
    cursor.execute(query)
    user = cursor.fetchone()
    print(user)

    cursor.close()
    connection.close()
    return user
login()
