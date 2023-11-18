import csv
import mariadb
import time


def wait_for_db():
    while True:
        try:
            connection = mariadb.connect(host='db', user='user', password='password', database='database')
            connection.close()
            print("[FILLER] Database is ready.")
            return
        except Exception as e:
            print("[FILLER] Waiting for the database...")
            time.sleep(1)
    pass


def fill_database():
    print("[FILLER] Start filling database")
    with open("data.csv", 'r') as file:
        reader = csv.DictReader(file)
        connection = mariadb.connect(host='db', user='user', password='password', database='database')
        cursor = connection.cursor()
        
        cursor.execute("CREATE TABLE IF NOT EXISTS users (name VARCHAR(255), age INT)")
        for row in reader:   
            name = str(row['name'])
            age = int(row['age'])
            cursor.execute("SHOW TABLES")
            cursor.execute("INSERT INTO database.users(name, age) VALUES (?, ?)", [name, age])
        connection.commit()
        print("[FILLER] Database filled successfully.")

        cursor.execute("SELECT * FROM users")
        for row in cursor:
            print(row)

        cursor.close()
        connection.close()
    pass


if __name__ == "__main__":
    wait_for_db()
    fill_database()
