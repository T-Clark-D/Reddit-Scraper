from selenium.webdriver.common.by import By
import selenium

POST_ELEMENT_STRING = "//span[@class='rank'] /.."


class SubRedditMainPageLocators(object):
    UPVOTES_ELEMENT = (By.XPATH, '//div[@class="score unvoted"]')
    POST_ELEMENT = (By.XPATH, POST_ELEMENT_STRING)


class SubRedditPostElementLocators(object):
    RANK_ELEMENT = (By.XPATH, "(//span[@class='rank'] /.. /span) [1]")
