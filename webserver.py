from flask import Flask, json
import mariadb
import time


app = Flask(__name__)


def wait_for_db():
    while True:
        try:
            connection = mariadb.connect(host='db', user='user', password='password', database='database')
            connection.close()
            print("[WEB] Database is ready.")
            return
        except Exception as e:
            print("[WEB] Waiting for the database...")
            time.sleep(1)
    pass


@app.route('/', methods=['GET'])
def get_data():
    wait_for_db()
    connection = mariadb.connect(host='db', user='user', password='password', database='database')
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM users")
    database_users = {}
    for row in cursor:
        name = row[0]
        age = row[1]
        database_users[name] = age
    
    cursor.close()
    connection.close()
    return json.dumps(database_users), 200
    pass


@app.route('/health', methods=['GET'])
def health():
    return json.dumps({"status": "OK"}), 200
    pass


@app.errorhandler(404)
def page_not_found(e):
    return json.dumps({"error": "Not Found"}), 404
    pass


if __name__ == "__main__":
    wait_for_db()
    app.run(host='0.0.0.0', port=8000)
