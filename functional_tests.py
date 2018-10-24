from selenium import webdriver
d = webdriver.Firefox()
# User goes to the page.
d.get('http://0.0.0.0:8000/index.html')

# Users browser displays title "Vocabulary through Culture"
assert "Vocabulary through Culture" in d.title

# User sees text: "Welcome to Vocabulary through Culture!"
body = d.find_element_by_tag_name('body')
assert "Vocabulary through Culture" in body.text

# User sees a form for registering
form = d.find_element_by_id('register-form')

# User sees mail and password text fields
mail_field = d.find_element_by_css_selector('input#mail-id')
assert mail_field.get_attribute('type') == 'text'
password_field = d.find_element_by_css_selector('input#password')
assert password_field.get_attribute('type') == 'text'

# User sees labels for those text fields
print(form.text)
assert 'Email:' in form.text
assert 'Password:' in form.text

# User enters username "John@gmail.com", password "Johnspassword" and clicks the submit button.
mail_field.send_keys('John@gmail.com')
submit_button = d.find_element_by_css_selector(
    'input[value="Create Account!"]')
submit_button.click()

# Thw browser takes John to a New webpage: Title "Welcome"
assert d.title == 'Welcome'
