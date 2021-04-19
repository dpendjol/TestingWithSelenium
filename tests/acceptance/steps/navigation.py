from behave import *
from selenium import webdriver

use_step_matcher('re')

@given('I am on the homepage')
def step_impl(context):
    browser_options = webdriver.ChromeOptions()
    browser_options.add_argument("--incognito")
    
    context.browser = webdriver.Chrome(chrome_options=browser_options)
    context.browser.get('http://127.0.0.1:5000')

@then('I am on the blog page')
def step_impl(context):
    assert context.browser.current_url == 'http://127.0.0.1:5000/blog'