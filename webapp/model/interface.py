import sqlite3

CONNECTION_CACHE = None


def connect(db_path):
    global CONNECTION_CACHE
    CONNECTION_CACHE = CONNECTION_CACHE or sqlite3.connect(db_path)
    return CONNECTION_CACHE


def write_to_db(query, params, db_path):
    conn = connect(db_path)
    c = conn.cursor()
    c.execute(query, params)
    conn.commit()
    return 


def read_from_db(query, params, db_path, want_all_lines):
    conn = connect(db_path)
    c = conn.cursor()
    c.execute(query, params)
    if want_all_lines:
        return c.fetchall()
    else:
        return c.fetchone()