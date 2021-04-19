from behave import *
from tests.acceptance.page_model.base_page import BasePage
from tests.acceptance.page_model.blog_page import BlogPage

use_step_matcher('re')

@then('There is a title shown on the page')
def step_impl(context):
    page = BasePage(context.driver)
    assert page.title.is_displayed()

@step('The title tag had content "(.*)"')
def step_impl(context, content):
    page = BasePage(context.driver)   
    assert page.title.text == content
    
@then('I can see there is a posts section on the page')
def step_impl(context):
    page = BlogPage(context.driver)
    assert page.posts_section.is_displayed()
    
@then('I can see there is a post with the title "(.*)" in the posts section')
def step_impl(context, title):
    page = BlogPage(context.driver)
    found_posts = page.all_posts
    post_list = [p for p in found_posts if p.text == title]
    
    assert len(post_list) > 0
    assert all([p.is_displayed() for p in post_list])