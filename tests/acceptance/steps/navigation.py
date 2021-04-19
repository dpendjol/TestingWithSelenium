from behave import *
from selenium import webdriver
from tests.acceptance.page_model.base_page import BasePage
from tests.acceptance.page_model.home_page import HomePage
from tests.acceptance.page_model.blog_page import BlogPage

use_step_matcher('re')

@given('I am on the homepage')
def step_impl(context):
    driver_options = webdriver.ChromeOptions()
    driver_options.add_argument("--incognito")
    
    context.driver = webdriver.Chrome(chrome_options=driver_options)
    page = HomePage(context.driver)
    context.driver.get(page.url)

@then('I am on the blog page')
def step_impl(context):
    assert context.driver.current_url == BlogPage(context.driver).url

@given('I am on the blogpage')
def step_impl(context):
    driver_options = webdriver.ChromeOptions()
    driver_options.add_argument("--incognito")
    
    context.driver = webdriver.Chrome(chrome_options=driver_options)
    page = BlogPage(context.driver)
    context.driver.get(page.url)

@then('I am on the home page')
def step_impl(context):
    assert context.driver.current_url == HomePage(context.driver).url