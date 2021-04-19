from tests.acceptance.locators.blog_page import BlogPageLocators
from tests.acceptance.page_model.base_page import BasePage

class BlogPage(BasePage):
    @property
    def url(self):
        return super(BlogPage, self).url + '/blog'
    
    @property
    def posts_section(self):
        return self.driver.find_element(*BlogPageLocators.POSTS_SECTION)
    
    @property
    def all_posts(self):
        return self.driver.find_elements(*BlogPageLocators.POSTS)
    
    @property
    def create_post(self):
        return self.driver.find_element(*BlogPageLocators.CREATE_POST)
    
    @property
    def home_link(self):
        return self.driver.find_element(*BlogPageLocators.HOME_LINK)