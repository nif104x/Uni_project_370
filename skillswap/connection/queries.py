from django.db import connection

def get_all_connection(username):
    with connection.cursor() as cursor:
        cursor.execute(
            """
            SELECT 
                u.name, 
                u.username,  
            FROM user u
            JOIN connection c ON (u.username = c.requester_username OR u.username = c.receiver_username)
            WHERE (c.requester_username = %s OR c.receiver_username = %s)
              AND u.username != %s
              AND c.status = 'accepted'
            """, 
            [username, username, username]
        )
        return cursor.fetchall()