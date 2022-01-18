import sqlite3

def init_db(conn):
    conn.execute("""
        create table savings(
            userid text primary key,
            amount integer not null
        )
    """)

def create_user(conn, userid, amount):
    conn.execute("insert into savings(userid, amount) values (?, ?)", (userid, amount))

def get_credit(conn, userid):
    cur = conn.cursor()
    cur.execute("select amount from savings where userid = ?", (userid,))
    return cur.fetchone()[0]

def set_credit(conn, userid, amount):
    conn.execute("update savings set amount = ? where userid = ?", (amount, userid))

def transfer(conn, user_a, user_b, transfer_amount):
    user_a_credit = get_credit(conn, user_a)
    assert user_a_credit >= transfer_amount

    user_b_credit = get_credit(conn, user_b)

    new_user_a_credit = user_a_credit - transfer_amount
    set_credit(conn, user_a, new_user_a_credit)

    new_user_b_credit = user_b_credit + transfer_amount
    set_credit(conn, user_b, new_user_b_credit)
