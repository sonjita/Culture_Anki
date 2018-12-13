# run via ~/Dropbox/RC/Vocabulary project/vocabulary_through_culture$ python -m pytest tests/ 

import pytest
from webapp.routes import create_app




# @pytest.fixture
# def client():
#    # app.config['TESTING'] = True
#     client = app.test_client()

#     app.app_context().push()

#     yield client

#     app.app_context().pop()


def test_that_bad_login_fails():
    app = create_app({'TESTING' : True})
    #app.config['TESTING'] = True
    client = app.test_client()
    with app.app_context():
        response = client.get('/login?username=somethingwrong&password=alsowrong')
    assert response.get_data(as_text=True) == 'goodbye'
    


def test_that_good_login_passes():
    app = create_app({'TESTING' : True})
    #app.config['TESTING'] = True
    client = app.test_client()
    with app.app_context():
        response = client.get('/login?username=john@gmail.com&password=unsecure_password')
    assert response.get_data(as_text = True) == '''<!doctype html>
    <html lang='en'>

    <head>
        <link href='style.css' type='text/css' rel='stylesheet'>
        <title>Welcome</title>
        <meta charset='utf-8'>
    </head>


    </body>

    </html>'''


def test_that_home_page_renders():
    app = create_app({'TESTING' : True})
    #app.config['TESTING'] = True
    client = app.test_client()
    with app.app_context():
        response = client.get('/')
    assert response.get_data(as_text = True) == '''<!doctype html>
    <html lang='en'>

    <head>
        <link href='style.css' type='text/css' rel='stylesheet'>
        <title>Vocabulary through Culture</title>
        <meta charset='utf-8'>
    </head>

    <body>
        <h1>
            Welcome to Vocabulary through Culture!
        </h1>
        <div>
            <p id='test-id'> hello </p>
        </div>
        <form action='/login' id='register-form'>
            <div>
                <span style='float: left; width: 100px'>Email: </span>
                <input type='text' id='mail-id' name='username'>
            </div>
            <div>
                <span style='float: left; width: 100px'>Password: </span>
                <input type='password' id='password' name='password'>
            </div>
            <input type="submit" value="Create Account!">
        </form>




    </body>

    </html>'''

