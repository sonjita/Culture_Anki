from selenium import webdriver
d = webdriver.Firefox()
#User goes to the page.
d.get('http://0.0.0.0:8000/index.html')

#Users browser displays title "Vocabulary through Culture"
assert "Vocabulary through Culture" in d.title

#User sees text: "Welcome to Vocabulary through Culture!"
print (d.page_source)
body = d.find_element_by_tag_name('body')
assert "Vocabulary through Culture" in body.text

#User sees mail field and password field labeled "e-mail: " and "Password: " and submit button
mail_field = d.find_element_by_css_selector('input#mail-id')
assert mail_field.get_attribute('type')=='text'
print(dir(mail_field))



#User enters username "John@gmail.com", password "Johnspassword" and clicks the submit button.

#Thw browser takes John to a new webpage: Title "Welcome"


