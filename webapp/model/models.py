import sqlite3
import bcrypt
import json

DATABASE = "database.db"

CONNECTION_CACHE = None


def _connect(dp_path=DATABASE):
    global CONNECTION_CACHE
    CONNECTION_CACHE = CONNECTION_CACHE or sqlite3.connect(DATABASE)
    return CONNECTION_CACHE


def _write_to_db(query, params, db_path):
    conn = _connect()
    c = conn.cursor()
    c.execute(query, params)
    conn.commit()
    return 


def _read_from_db(query, params, db_path, want_all_lines):
    conn = _connect()
    c = conn.cursor()
    c.execute(query, params)
    if want_all_lines:
        return c.fetchall()
    else:
        return c.fetchone()


def mail_exists(email, db_path=DATABASE):
    query = f"SELECT * from users where email=?"
    param = (email, )
    return _read_from_db(query, param, db_path, want_all_lines=False)


def encrypt(s, salt):
    binary = s.encode('utf-8')
    hashed = bcrypt.hashpw(binary, salt)
    return hashed


def password_correct(email, password, db_path=DATABASE):
    query = f"SELECT encrypted_password, salt FROM users WHERE email=?"
    param = (email, )
    user_info = _read_from_db(query, param, db_path, want_all_lines=False)
    if user_info:
        encrypted_stored_password, salt = _read_from_db(query, param, db_path, want_all_lines=False)
        return encrypt(password, salt) == encrypted_stored_password
    else:
        return "Email doesn't exist."


def create_account(email, password, db_path=DATABASE):
    salt = bcrypt.gensalt()
    hashed_password = encrypt(password, salt) 
    query = f'''INSERT INTO users (email, encrypted_password, salt, proficiencies) VALUES (?, ?, ?, ?)'''
    parameters = (email, hashed_password, salt, json.dumps({}))
    _write_to_db(query, parameters, db_path)
    return


# create_account("emily@happymail.com", "super_secure1056")
print('should be correct:', password_correct("emily@happymail.com", "super_secure1056"))
print("shouldn't be correct:", password_correct("emily@happymail.com", "super_secure105"))

# print(mail_exists("emly@gmail.com")) 


# def check_log_in(email, password):

