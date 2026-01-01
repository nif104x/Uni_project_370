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
    

def db_make_request(username, target_user):
    
    with connection.cursor() as cursor:
        cursor.execute("""
            INSERT INTO connection (requester_username, receiver_username, status) 
            VALUES (%s, %s, 'Pending')
        """, [username, target_user])


def db_confirm_request(username, target_user):
    
    with connection.cursor() as cursor:
        cursor.execute("""
            INSERT INTO connection (requester_username, receiver_username, status) 
            VALUES (%s, %s, 'accepted')
        """, [username, target_user])


def db_get_connection_requests(username):
    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT requester_username FROM connection WHERE receiver_username = %s",
            [username]
        ) ###### extract name and last massage letter to show in the frontend
        # Returns a list of tuples like [('user1',), ('user2',)]
        raw_requests = cursor.fetchall()
        requesters = [row[0] for row in raw_requests] #into ['user1', 'user2']
        return requesters




        