# run via ~/Dropbox/RC/Vocabulary project/vocabulary_through_culture$ python -m pytest tests/
# import os
import pytest
# import webapp.model.models as models
import webapp.model.manage_authentification as models
import random




# def where_am_i():
#     print('current directory:', os.path.dirname(os.path.realpath(__file__)))
#     assert True

TEST_DATABASE = "webapp/model/test_db.db" # FIXME: use some library to generate test db

print("test database:", TEST_DATABASE)

def test_create_account():
    num_char_in_mail = random.randint(3, 10)
    mail_as_list_of_ints = random.sample(range(1114112), num_char_in_mail)
    mymail = ''.join(map(chr, mail_as_list_of_ints)) + "@generic_provider.com"
    num_char_in_password = random.randint(5, 15)
    password_as_list_of_ints = random.sample(range(1114112), num_char_in_mail)
    password = ''.join(map(chr, password_as_list_of_ints))
    models.create_account(mymail, password, TEST_DATABASE)

    query = "SELECT * FROM users where email=?"
    conn = models.connect(TEST_DATABASE)
    c = conn.cursor()
    c.execute(query, (mymail, ))
    assert c.fetchone()


