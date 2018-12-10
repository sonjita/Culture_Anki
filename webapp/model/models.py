import sqlite3
import bcrypt
import json

DATABASE = "database.db"

CONNECTION_CACHE = None


def _connect(path=DATABASE):
    global CONNECTION_CACHE
    CONNECTION_CACHE = CONNECTION_CACHE or sqlite3.connect(DATABASE)
    return CONNECTION_CACHE


def create_account(email, password):
    binary_password = password.encode('utf-8')
    hashed_password = bcrypt.hashpw(binary_password, bcrypt.gensalt())
    print(f"json looks like this: '{json.dumps({})}'")
    print(type(hashed_password))
    print("hashed password:", hashed_password)
    query = f"INSERT INTO users (email, encrypted_password, proficiencies) VALUES ('{email}', '{hashed_password}', '{json.dumps({})}')"
    conn = _connect()
    c = conn.cursor()
    c.execute(query)
    conn.commit()
    conn.close()
    return


create_account("john@gmail.com", "unsecure_password") 
