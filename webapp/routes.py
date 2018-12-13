from flask import Flask, request, session, redirect, flash, render_template, url_for
from pprint import pprint
import sqlite3
from flask import g
print('routes')
import webapp.first_step as first_step
from webapp.model import interface


DATABASE_PATH="webapp/model/user_database.db"




#Whaaat?
#app = Flask(__name__)

#USERNAME = "john@gmail.com"
#Encrypt:
#PASSWORD = "unsecure_password"








def create_app(test_config=None): 
    
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY="dev"      
    )
    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile("config.py", silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # def get_db():
    #     print('getdb called')
    #     return interface.connect(DATABASE_PATH)
        # g._database = getattr(g, "_database", None) or sqlite3.connect(models.DATABASE)
        # db = getattr(g, "_database", None)
        # if db is None:
        #     db = g._database = sqlite3.connect(DATABASE)
        # return db

    @app.teardown_appcontext
    def close_connection(exception):
        db = getattr(g, "_database", None)
        if db is not None:
            db.close()


    @app.before_request
    def make_session_permanent():
        session.permanent = True
    
    @app.route("/")
    def home():
        

        return render_template("home.html")


    @app.route("/create_account")
    def render_account_creation():
        return render_template("home.html")
    
    @app.route("/media")
    def media():
        media_user = {"books": {"english": ["Harry Potter", "Alice in Wonderland"], "spanish": ["100 años de soledad"]}, \
        "movies": {"english": ["inception"], "spanish": ["kamikaze", "el labarinto de Pan", "8 apellidos vascos"]}, \
        "series": {}, "songs" : {"english": ["somwhere over the rainbow"], "spanish": [] }} #FIXME: THIS IS HARD CODED
        
        media_verbs = {"books" : "read", "movies" : "watched", "series": "watched", "song": None}
        return render_template("media.html", media=media_user, verbs=media_verbs)

    @app.route("/languages")
    def languages():
        # TO DO: check that the keys of langs_vocab and Langs_grammar coincide
        usr_langs_vocab = {"English": 8, "Spanish": 3}
        usr_langs_grammar = {"English": {"nouns": "True", "regular verbs": "True", "irregular verbs":"False"}, "Spanish": {"nouns": "True", "adjectives": "True", "regular verbs": "False", "irregular verbs": "False"}}
        all_languages = {"English":["nouns","regular verbs", "irregular verbs"], "Spanish":["nouns","adjectives","regular verbs", "irregular verbs"]}
        test_dict = {"1":"5"}
        return render_template("languages.html", vocab=usr_langs_vocab, grammar=usr_langs_grammar, langs=all_languages, test=test_dict)

#get-request: render different template
    @app.route("/signing_up",)
    def create_account():
        print("request:", request.args)
        mail = request.args.get("username")
        #CHECK IF MAIL IS ALREADY IN THE DB 
        if not mail:
            flash("Please, provide an email!")
            return redirect(url_for("create_account"))
        password = request.args.get("password")
        db = interface.connect(DATABASE_PATH)
        cur = db.cursor()
        query = f"INSERT INTO passwords (email, encrypted_password) VALUES ('{mail}', '{password}')"   
        cur.execute(query)
        db.commit()
        cur.close()
        session["email"] = request.args.get("username")
        return media()

#handle get request (maybe using session, so if the user is logged in, they get redirected to the landing page)
    @app.route("/login", methods=["POST", "GET"])
    def check_success_of_login():
        print("session:", session)
        if request.method == "GET":
            if "email" in session: 
                return redirect(url_for("media"))
            else:
                return redirect(url_for("home"))
        mail = request.form["username"]
        unsecure_password = request.form["password"]
        db = interface.connect(DATABASE_PATH)
        query = f"SELECT * from passwords WHERE email = '{mail}' "  
        cur = db.execute(query)  
        data = cur.fetchall()
        db.commit()
        cur.close()
        print("data:", data)
        if not data:
            flash("Invalid email. Sorry for that.")
            return home()
        elif data[0][2] == unsecure_password:
            session["email"] = mail
            return redirect(url_for("media"))  #new_media()
        else:
            flash("Invalid password. Sorry for that.")
        return home()
            
    @app.route("/logout")
    def logout():
        if "email" in session:
            session.pop("email")
        else:
            flash("No one is logged in.")
            print("session:", session)
        return redirect(url_for("home"))
            
    # @app.route("/new_media")    
    # def new_media():   
    #     #if request.args.get("username") == USERNAME and request.args.get("password") == PASSWORD:
    #     #    return """<!doctype html>
    #     if not session.get("email"):
    #         redirect("/login")
    #     else:
    #         print('first step function about to be used')
    #         MostCommonInChunks = first_step.get_100_words()[0]
    #         return render_template("new_media.html", chunk=MostCommonInChunks)
    # # pprint(vars(app))
    # print("----------------------")
    # pprint(vars(app.url_map))
    # print("app.url_map")
    # print("--------------------")
    # print("app.view_functions:")
    # pprint(app.view_functions["home"])
    # pprint(app.view_functions["static"])



    return app

   
# if __name__ == "__main__":
def start_app():
    print('about to create app')
    app = create_app({})
    print(app.config)
    # def make_session_permanent():
    #     session.permanent = True
    #app.before_request_funcs.setdefault(None, []).append(make_session_permanent) 

    print('finished creating app')
    import os
    print('os.path', os.getcwd())
    app.run("0.0.0.0", debug = True, port = 7000)
    print('running app...')


