from locator import *


# Element representing an individual post on a subreddit main page
class SubRedditPostElement:

    rank = None
    title = None
    link_element = None
    upvotes = None

    def __init__(self, rank, title, link, upvotes):
        self.rank = rank
        self.title = title
        self.link_element = link
        self.upvotes = upvotes

    # Returns the post's rank as an int
    def get_rank(self):
        return self.rank

    # Returns the title of the post as a string
    def get_title(self):
        return self.title

    # Returns link to the post page
    def get_link(self):
        return self.link_element.get_attribute('href')

    # Returns number of upvotes as an int
    def get_upvotes(self):
        return self.upvotes

    # Convenient to string method
    def to_string(self):
        return str(self.rank) + " " + str(self.upvotes) + " " + self.title + " " + self.link_element.get_attribute('href')


class SubRedditMainPage:

    subreddit_posts = []

    def __init__(self, driver):
        self.driver = driver
        subreddit_posts_element = self.driver.find_elements(*SubRedditMainPageLocators.POST_ELEMENT)
        for i in range(len(subreddit_posts_element)):
            if self.driver.find_element_by_xpath("(//span[@class='rank'] /.. /span)" + "[" + str(i+1) + "]").text != "":
                rank = int(self.driver.find_element_by_xpath("(//span[@class='rank'] /.. /span)" + "[" + str(i+1) + "]").text)
            else:
                rank = 0
            title = self.driver.find_element_by_xpath("(//span[@class='rank'] /.. //p[@class='title'])" + "[" + str(i+1) + "]").text
            link = self.driver.find_element_by_xpath("(//span[@class='rank'] /.. //p[@class='title'] /a)" + "[" + str(i+1) + "]")
            upvotes = int(self.driver.find_element_by_xpath("(//span[@class='rank'] /.. //div[@class='score unvoted'])" + "[" + str(i+1) + "]").get_attribute('title'))
            self.subreddit_posts.insert(i, SubRedditPostElement(rank, title, link, upvotes))

    def print_posts(self):
        for i in range(len(self.subreddit_posts)):
            print(self.subreddit_posts[i].to_string())


class PostPage:

    def __init__(self, driver):
        self.driver = driver

    def download_and_close(self, id):
        try:
            image_link = self.driver.find_element_by_xpath("//img[@class='preview']")
            image_link.screenshot(r"C:\Users\jesse\PycharmProjects\RedditScraper\Posts\Test" + str(id) + ".png")
        except selenium.common.exceptions.NoSuchElementException:
            print("No image in this one bois")
        self.driver.close()