from django.db import connection
from datetime import date

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
            INSERT IGNORE INTO connection (requester_username, receiver_username, status) 
            VALUES (%s, %s, 'Pending')
        """, [username, target_user])

        users = sorted([username, target_user])
        conversation_id = f"{users[0]}#{users[1]}"
        cursor.execute(
            """
        INSERT IGNORE INTO conversation (conversation_id, user_one, user_two)
        VALUES (%s, %s, %s)
        """, [conversation_id, users[0], users[1]]
        )

def get_all_messages(user1, user2):
    users = sorted([user1, user2])
    convo_id = f"{users[0]}#{users[1]}"

    with connection.cursor() as cursor:
        cursor.execute(
            """ SELECT 
                c.sender_id,
                c.message_text, 
                c.time_stamp
            FROM chat c
            WHERE c.conversation_id = %s
            ORDER BY c.time_stamp ASC;
            """, [convo_id]
        )
        return cursor.fetchall()




def db_confirm_request(username, target_user):
    
    with connection.cursor() as cursor:
        cursor.execute("""
            INSERT INTO connection (requester_username, receiver_username, status) 
            VALUES (%s, %s, 'accepted')
        """, [username, target_user])

    
def db_get_connection_list(username):
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT 
                CASE 
                    WHEN c.requester_username = %s THEN c.receiver_username 
                    ELSE c.requester_username 
                END AS other_username,
                u.name,
                c.status
            FROM connection c
            JOIN user u ON u.username = (
                CASE 
                    WHEN c.requester_username = %s THEN c.receiver_username 
                    ELSE c.requester_username 
                END
            )
            WHERE c.requester_username = %s OR c.receiver_username = %s
        """, [username, username, username, username])
        raw_requests = cursor.fetchall()
        requesters = list(set([row[0] for row in raw_requests])) 
        return requesters
    
def send_message(user1, user2, text):
    users = sorted([user1, user2])
    convo_id = f"{users[0]}#{users[1]}"
    with connection.cursor() as cursor:
        cursor.execute(
            """INSERT INTO chat (conversation_id, sender_id, message_text)
            VALUES (%s, %s, %s);
            """, [convo_id, user1, text]
        )


        