from django.db import connection
from datetime import date

def get_profile(username):
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT u.name, u.average_rating, u.experience_level, u.join_date, u.bio, us.skill_type, s.skill_name
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
            'name': rows[0][0],
            'rating': rows[0][1],
            'experience': rows[0][2],
            'join': rows[0][3],
            'bio': rows[0][4],
            'teaching': [],
            'learning': []
        }

        # Loop to sort the skills
        for row in rows:
            skill_type = row[5] # 'TEACH' or 'LEARN'
            skill_name = row[6]
            
            if skill_type == 'TEACH':
                profile['teaching'].append(skill_name)
            elif skill_type == 'LEARN':
                profile['learning'].append(skill_name)
                
        return profile
    

def db_get_all_user_skills(username):
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT s.skill_name, us.skill_type 
            FROM user_skills us
            JOIN skill s ON us.skill_id = s.skill_id
            WHERE us.username = %s
        """, [username])
        return cursor.fetchall()