import mysql.connector
from MySQL import *


def db_config():
    dbconfig = {'host': 'localhost',
                'port': '3306',
                'user': 'root',
                'password': 'root',
                'database': 'casino'}
    return dbconfig


def connect_db():
    connection = mysql.connector.connect(**db_config())
    print("Connected to MySQL database")
    return connection

conn = connect_db()



def login_user(connection):
    cursor = connection.cursor(dictionary=True)
    login = input('Enter your login: ')
    password = input('Enter your password: ')
    try:
        # Выполняем запрос с параметрами
        cursor.execute(MySQL.login_MySQL, (login, password))
        user = cursor.fetchone()

        if user:
            print(f"Hello, {user['first_name']} {user['last_name']}!")
        else:
            print("Password or login is incorrect")
    except mysql.connector.Error as err:
        print(f"Error with login: {err}")
    finally:
        cursor.close()


def register_user(connection):
    cursor = connection.cursor()

    first_name = input('Enter your first name: ')
    last_name = input('Enter your last name: ')
    email = input('Enter your email: ')
    password = input('Enter your password: ')
    repeat_password = input('Repeat password: ')

    if password != repeat_password:
        print('----------------------------')
        print('Passwords do not match!')
        print('----------------------------')
        return

    try:
        # Используем параметризованные запросы для безопасности
        cursor.execute(MySQL.registrtion_MySQL, (first_name, last_name, email, password))
        connection.commit()
        print("Registered successfully")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()


def main():
    connection = connect_db()
    while True:
        print('1. Registration')
        print('2. LogIn')
        print('3. Exit')
        command = input()
        if command == '1':
            register_user(conn)
        elif command == '2':
            login_user(conn)
        elif command == '3':
            break
        connection.close()

if __name__ == '__main__':
    main()