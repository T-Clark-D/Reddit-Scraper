from bs4 import BeautifulSoup as bs
import requests


def main():
    red = requests.get('https://www.reddit.com/r/softwaregore/')
    soup = bs(red.text, 'html.parser')

    print(soup.prettify())

# Run main function
if __name__ == '__main__':
    main()
