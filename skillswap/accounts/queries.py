from django.db import connection
from datetime import date

def db_registration(username, password, name, email):
    try:
        with connection.cursor() as cursor:
            cursor.execute(
                "INSERT INTO person (username, password) VALUES (%s, %s)", 
                [username, password]
            )

            cursor.execute(
                "INSERT INTO user (username, name, email, join_date) VALUES (%s, %s, %s, %s)", 
                [username, name, email, date.today()]
            )

            print("User successfully registered!")

    except Exception as e:
        print(f"Database Error: {e}")




def get_user_role(u_name, p_word):
    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT username FROM person WHERE username = %s AND password = %s", 
            [u_name, p_word]
        )
        row = cursor.fetchone()

        if row:
            cursor.execute("SELECT username FROM admin WHERE username = %s", [u_name])
            is_admin = cursor.fetchone()
            
            if is_admin:
                return 'admin'
            else:
                return 'user'
        
        return None
    
def get_user_data(username):
    pass