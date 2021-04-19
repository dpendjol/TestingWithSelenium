from selenium.webdriver.common.by import By

class BlogPageLocators:
    HOME_LINK = By.ID, 'home-link'
    CREATE_POST = By.ID, 'add-post-link'
    POSTS_SECTION = By.ID, 'posts'
    POSTS = By.CLASS_NAME, 'post_link'
    