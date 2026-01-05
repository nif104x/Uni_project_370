from django.db import connection

def db_admin_get_stats():
    with connection.cursor() as cursor:
        cursor.execute("SELECT username, name, email, (SELECT COUNT(*) FROM user_skills WHERE username = user.username) as skill_count FROM user")
        users = cursor.fetchall()

        cursor.execute("""
            SELECT s.session_id, s.initiator_username, s.partner_username, 
                   sk1.skill_name, sk2.skill_name, s.status 
            FROM session s
            JOIN skill sk1 ON s.initiator_offered_skill_id = sk1.skill_id
            JOIN skill sk2 ON s.partner_offered_skill_id = sk2.skill_id
        """)
        sessions = cursor.fetchall()
        
    return users, sessions

def db_admin_delete(table, pk_col, pk_val):
    with connection.cursor() as cursor:
       
        allowed_tables = {'user', 'session', 'skill'}
        if table in allowed_tables:
            cursor.execute(f"DELETE FROM {table} WHERE {pk_col} = %s", [pk_val])