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



def db_update_bio(username, new_bio):
    with connection.cursor() as cursor:
        cursor.execute(
            "UPDATE user SET bio = %s WHERE username = %s",
            [new_bio, username]
        )
    #     cursor.execute(
    #         "SELECT bio FROM user WHERE username = %s",
    #         [username]
    #     )
    #     row = cursor.fetchone()
    # return row[0] if row else None
        print("Bio updated Successfully!")


def db_update_email(username, new_email):
    with connection.cursor() as cursor:
        cursor.execute(
            "UPDATE user SET email = %s WHERE username = %s",
            [new_email, username]
        )
        print("Email updated Successfully!")

def db_update_password(username, new_password):
    with connection.cursor() as cursor:
        cursor.execute(
            "UPDATE person SET password = %s WHERE username = %s",
            [new_password, username]
        )
        print("Password updated Successfully!")

def db_update_skill(username, skill_id, type):
    with connection.cursor() as cursor:
        cursor.execute(
            "INSERT INTO user_skills (username, skill_id, skill_type) VALUES (%s, %s, %s)",
            [username, skill_id, type]
        )
        print("skill updated Successfully!")


def get_user_full_profile(username):
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT p.password, u.name, u.email, u.average_rating, u.total_credits, u.experience_level, u.join_date, u.bio, us.skill_type, s.skill_name
            FROM person p
            JOIN user u ON p.username = u.username
            LEFT JOIN user_skills us ON u.username = us.username
            LEFT JOIN skill s ON us.skill_id = s.skill_id
            WHERE u.username = %s
        """, [username])
        
        rows = cursor.fetchall()
        
        if not rows:
            return None

        # Basic info is the same in every row
        profile = {
            'password': rows[0][0],
            'name': rows[0][1],
            'email': rows[0][2],
            'rating': rows[0][3],
            'credits': rows[0][4],
            'experience': rows[0][5],
            'join': rows[0][6],
            'bio': rows[0][7],
            'teaching': [],
            'learning': []
        }

        # Loop to sort the skills
        for row in rows:
            skill_type = row[8] # 'TEACH' or 'LEARN'
            skill_name = row[9]
            
            if skill_type == 'TEACH':
                profile['teaching'].append(skill_name)
            elif skill_type == 'LEARN':
                profile['learning'].append(skill_name)
                
        return profile
    

def db_get_all_skills():
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM skill")
        rows = cursor.fetchall()
    skill_list = []
    for row in rows:
        skill_list.append(
            {
                'id': row[0],
                'skill_name': row[1],
                'desc': row[2]
            }
        )
    return skill_list