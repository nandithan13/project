from flask import Flask
import pyodbc

app = Flask(__name__)

# 🔹 Azure SQL Database connection details
server = 'nanditha13.database.windows.net'   # Always append .database.windows.net
database = 'nan'
username = 'nanditha'
password = 'Nanditha@1314'
driver = '{ODBC Driver 17 for SQL Server}'   # Make sure ODBC Driver 17+ is installed

# 🔹 Establish connection
def get_db_connection():
    conn = pyodbc.connect(
        f'DRIVER={driver};SERVER={server};PORT=1433;DATABASE={database};UID={username};PWD={password}'
    )
    return conn

@app.route('/')
def home():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        # Example query: list first 5 tables
        cursor.execute("SELECT TOP 5 name FROM sys.tables")
        rows = cursor.fetchall()
        conn.close()

        table_names = [row[0] for row in rows]
        return f"<h1>Azure SQL Connected ✅</h1><p>Tables in DB: {table_names}</p>"
    except Exception as e:
        return f"<h1>❌ Connection Failed</h1><p>{str(e)}</p>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
