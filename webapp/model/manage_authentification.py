import sqlite3
import webapp.model.interface as interface
import bcrypt
import json

DATABASE = "webapp/model/database.db"


def mail_exists(email, db_path=DATABASE):
    query = "SELECT * from users where email=?"
    param = (email, )
    return interface.read_from_db(query, param, db_path, want_all_lines=False)


def encrypt(s, salt):
    binary = s.encode('utf-8')
    hashed = bcrypt.hashpw(binary, salt)
    return hashed


def password_correct(email, password, db_path=DATABASE):
    query = "SELECT encrypted_password, salt FROM users WHERE email=?"
    param = (email, )
    user_info = interface.read_from_db(query, param, db_path, want_all_lines=False)
    if user_info:
        encrypted_stored_password, salt = user_info
        return encrypt(password, salt) == encrypted_stored_password
    else:
        return "Email doesn't exist."


def create_account(email, password, db_path=DATABASE):
    salt = bcrypt.gensalt()
    hashed_password = encrypt(password, salt) 
    query = "INSERT INTO users (email, encrypted_password, salt, proficiencies) VALUES (?, ?, ?, ?)"
    parameters = (email, hashed_password, salt, json.dumps({}))
    interface.write_to_db(query, parameters, db_path)
    return


# create_account("emily@happymail.com", "super_secure1056")
print('should be correct:', password_correct("emily@happymail.com", "super_secure1056"))
print("shouldn't be correct:", password_correct("emily@happymail.com", "super_secure105"))

# print(mail_exists("emly@gmail.com")) 


# def check_log_in(email, password):



print('main: __main__, __<name of file>__', __name__)