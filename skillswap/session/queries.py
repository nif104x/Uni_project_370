from django.db import connection
from datetime import date

def get_skill_id(skill_name):
    with connection.cursor() as cursor:
        cursor.execute("SELECT skill_id FROM skill WHERE skill_name = %s", [skill_name])
        row = cursor.fetchone()
        return row[0] if row else None

def db_create_session(username, user, offer, rqst, schedule_time, session_id):
    offer_id = get_skill_id(offer)
    rqst_id = get_skill_id(rqst)
    with connection.cursor() as cursor:
            query = """
                INSERT INTO session (
                    session_id, 
                    initiator_username, 
                    partner_username, 
                    initiator_offered_skill_id, 
                    partner_offered_skill_id, 
                    schedule_time, 
                    status, 
                    credit_used
                ) 
                VALUES (%s, %s, %s, %s, %s, %s, 'pending', 5)
            """
            
            params = [
                session_id, 
                username,   
                user,      
                offer_id,      
                rqst_id,       
                schedule_time
            ] 
            cursor.execute(query, params) 


"""
amar next kaj:
sort the request to handle by partner_id and 'pending'
then if accept then create a session link using session_id
then sort the sessions form the database and show based on accepted and pending
- if can do after handling session when completed then use the review button 
""" 


def db_get_active_sessions(username):
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT 
                u.name AS partner_name,
                CASE 
                    WHEN s.initiator_username = %s THEN sk2.skill_name 
                    ELSE sk1.skill_name 
                END AS learning_skill,
                CASE 
                    WHEN s.initiator_username = %s THEN sk1.skill_name 
                    ELSE sk2.skill_name 
                END AS trading_skill,
                s.schedule_time,
                s.link,
                u.username AS partner_username
            FROM session s
            JOIN user u ON u.username = (
                CASE 
                    WHEN s.initiator_username = %s THEN s.partner_username 
                    ELSE s.initiator_username 
                END
            )
            JOIN skill sk1 ON s.initiator_offered_skill_id = sk1.skill_id
            JOIN skill sk2 ON s.partner_offered_skill_id = sk2.skill_id
            WHERE (s.initiator_username = %s OR s.partner_username = %s)
            AND s.status = 'accepted'
            ORDER BY s.schedule_time ASC
        """, [username, username, username, username, username])
        return cursor.fetchall()
    
def db_get_pending_sessions(username):
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT 
                u.name AS partner_name,
                CASE 
                    WHEN s.initiator_username = %s THEN sk2.skill_name 
                    ELSE sk1.skill_name 
                END AS learning_skill,
                CASE 
                    WHEN s.initiator_username = %s THEN sk1.skill_name 
                    ELSE sk2.skill_name 
                END AS trading_skill,
                s.schedule_time,
                CASE 
                    WHEN s.initiator_username = %s THEN 'SENT' 
                    ELSE 'RECEIVED' 
                END AS direction,
                s.session_id
            FROM session s
            JOIN user u ON u.username = (
                CASE 
                    WHEN s.initiator_username = %s THEN s.partner_username 
                    ELSE s.initiator_username 
                END
            )
            JOIN skill sk1 ON s.initiator_offered_skill_id = sk1.skill_id
            JOIN skill sk2 ON s.partner_offered_skill_id = sk2.skill_id
            WHERE (s.initiator_username = %s OR s.partner_username = %s)
            AND s.status = 'pending'
            ORDER BY s.schedule_time ASC
        """, [username, username, username, username, username, username])
        return cursor.fetchall()
    
def db_delete_session(session_id):
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM session WHERE session_id = %s", [session_id])


def db_accept_session(meeting_link, s_id):
    with connection.cursor() as cursor:
        cursor.execute("""
            UPDATE session 
            SET status = 'accepted', 
                link = %s 
            WHERE session_id = %s
        """, [meeting_link, s_id])


def db_process_session_credits(username):
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT COUNT(*) 
            FROM session 
            WHERE (initiator_username = %s OR partner_username = %s)
            AND status = 'completed'
        """, [username, username])
        
        session_count = cursor.fetchone()[0]


        if session_count > 0 and session_count % 3 == 0:
            
            cursor.execute("""
                UPDATE user 
                SET credits = credits + 10 
                WHERE username = %s
            """, [username])
            return f"Milestone reached! {session_count} sessions completed. 10 credits added."
            
        return f"Current count: {session_count}. Next reward at {((session_count // 3) + 1) * 3}."