class MySQL:
    registrtion_MySQL = """
            INSERT INTO users (first_name, last_name, email, password)
            VALUES (%s, %s, %s, %s)
        """
    login_MySQL = "SELECT * FROM users WHERE email = %s AND password = %s"
