import time
from selenium import webdriver
import page


class RedditScaper:

    def get_subreddit_page(self, subreddit):
        self.driver = webdriver.Chrome('C:\Program Files (x86)\chromedriver.exe')
        self.driver.get('https://old.reddit.com/r/' + subreddit + '/top/?sort=top&t=all')
        return page.SubRedditMainPage(self.driver)

    def get_post_page(self, post_link):
        self.driver = webdriver.Chrome('C:\Program Files (x86)\chromedriver.exe')
        self.driver.get(post_link)
        return page.PostPage(self.driver)


def main():
    redditScaper = RedditScaper()
    software_gore_page = redditScaper.get_subreddit_page("softwaregore")
    software_gore_page.print_posts()
    for i in range(len(software_gore_page.subreddit_posts)):
        post_page = redditScaper.get_post_page(software_gore_page.subreddit_posts[i].get_link())
        time.sleep(2)
        post_page.download_and_close(i)
        time.sleep(2)


# Run main function
if __name__ == '__main__':
    main()
