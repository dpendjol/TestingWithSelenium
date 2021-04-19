from behave import *
from selenium import webdriver

use_step_matcher('re')

@given('I am on the homepage')
def step_impl(context):
    driver_options = webdriver.ChromeOptions()
    driver_options.add_argument("--incognito")
    
    context.driver = webdriver.Chrome(chrome_options=driver_options)
    context.driver.get('http://127.0.0.1:5000')

@then('I am on the blog page')
def step_impl(context):
    assert context.driver.current_url == 'http://127.0.0.1:5000/blog'

@given('I am on the blogpage')
def step_impl(context):
    driver_options = webdriver.ChromeOptions()
    driver_options.add_argument("--incognito")
    
    context.driver = webdriver.Chrome(chrome_options=driver_options)
    context.driver.get('http://127.0.0.1:5000/blog')

@then('I am on the home page')
def step_impl(context):
    assert context.driver.current_url == 'http://127.0.0.1:5000/'