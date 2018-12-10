# run via ~/Dropbox/RC/Vocabulary project/vocabulary_through_culture$ python -m pytest tests/test_models.py
# import os
import pytest
import webapp.model.models as models
import random

# def where_am_i():
#     print('current directory:', os.path.dirname(os.path.realpath(__file__)))
#     assert True

TEST_DATABASE = "webapp/model/test_db.db" # FIXME: use some library to generate test db


def test_create_account():
    num_char_in_mail = random.randint(3, 10)
    mymail = ''.join(random.sample(range(1114112), num_char_in_mail)) + '@generic_provider.com'
    # num_char_in_password = random.randint(5, 20)
    password = ''.join(random.sample(range(1114112), 10))
    models.create_account(mymail, password)

    query = "select * from users where email=?"
    conn = models._connect(TEST_DATABASE)
    c = conn.cursor()
    c.execute(query, (mymail), TEST_DATABASE)
    conn.close()
    assert c.fetchone()
