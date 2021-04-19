from behave import *
from tests.acceptance.page_model.base_page import BasePage

use_step_matcher('re')

@when('I click on the "(.*)" link')
def step_impl(context, link_text):
    page = BasePage(context.driver)
    links = page.links
    
    found_links = [l for l in links if l.text == link_text]
    
    if len(found_links) > 0:
        found_links[0].click()
    else:
        raise RuntimeError()