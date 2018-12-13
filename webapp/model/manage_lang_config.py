import sqlite3
import constants
import api
import json

DATABASE = "database.db"

def add_language(user_id, language, vocab_proficiency, grammar_proficiency, db_path=DATABASE):
    # if not grammar_proficiency.keys() == constants.LANGUAGES[language]:
    #     raise ValueError("grammar_proficiency doesn't match the languge.")
    query = "SELECT proficiencies FROM users where id=?"
    param = (user_id, )
    configured_langs, = api.read_from_db(query, param, db_path, want_all_lines=False)
    configured_langs = json.loads(configured_langs)
    if configured_langs.get(language):
        raise ValueError("This language is already configured.")
    
    configured_langs[language] = {"vocab_proficiency": vocab_proficiency, "grammar_proficiency": grammar_proficiency}

    query = "UPDATE users SET proficiencies=? WHERE id=?"
    params = (json.dumps(configured_langs), user_id)
    api.write_to_db(query, params, db_path)

add_language(1, "English", 8, {"nouns": "True", "adjectives": "True", "regular verbs": "True", "irregular verbs": "False", "contractions": "True"})