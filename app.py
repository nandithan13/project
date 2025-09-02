from flask import Flask
import pyodbc

app = Flask(__name__)

# 🔹 Azure SQL Database connection details
server = 'nanditha13.database.windows.net'   # Always append .database.windows.net
database = 'nan'
username = 'nanditha'
password = 'chethu@1314'
driver = '{ODBC Driver 17 for SQL Server}'   # Make sure ODBC Driver 17+ is installed
conn_str = (
    "Driver={ODBC Driver 17 for SQL Server};"
    "Server=tcp:nanditha13.database.windows.net,1433;"
    "Database=nan;"
    "Uid=nanditha;"
    "Pwd=Nanditha@1314;"
    "Encrypt=yes;"
    "TrustServerCertificate=no;"
    "Connection Timeout=30;"
)

try:
    conn = pyodbc.connect(conn_str)
    print("✅ Connected to Azure SQL successfully!")
except Exception as e:
    print("❌ Connection failed:", e)
👉 Right now, since your public network access is disabled, your connection will fail.
Would you like me to give you the exact steps (with screenshots) to turn on Allow Azure services and Add client IP so your connection works?








Ask ChatGPT

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
