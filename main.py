from bs4 import BeautifulSoup as bs
import requests


def main():
    #red = requests.get('https://old.reddit.com/r/softwaregore/')
    red = requests.get('https://old.reddit.com/r/softwaregore/comments/shv0kj/pikmin_bloom_gone_wrong/')
    soup = bs(red.text, 'html.parser')

    var = []
    #for link in soup.find_all('a'):
     #   if 'https://old.reddit.com/r/softwaregore/comments/' in str(link):
      #      var.append(link.get('href'))


    print(soup.prettify())
    print(var)

# Run main function
if __name__ == '__main__':
    main()
