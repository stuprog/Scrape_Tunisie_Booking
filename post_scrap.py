import time

from bs4 import BeautifulSoup

from news import News
from utils import scroll_down,get_links


def scrap_all_posts(driver):
    driver.get("https://www.tripadvisor.com/")
    scroll_down(driver, 0, 4000)
    src = driver.page_source
    soup = BeautifulSoup(src, 'lxml')
    all_news = [get_smaller_post(soup)]
   # smaller_posts = get_smaller_post(soup)
    #all_news.extend(smaller_posts)

    for post in all_news:
        print(post)
        print(soup)
    return all_news





def get_smaller_post(soup):
    list = []
    other_posts = soup.findAll('div', {'class': 'cgrRL'})
    for post in other_posts:
        news = News()
        get_links(post, news)
        list.append(news)
    try:
        news.title = post.find('p', {'class': 'WlYyy cPsXC biNiR cKUMi dpKLb eYhTT cWWWn fmARL fPuGr'}).get_text().strip()
        strings = [news.title]
    except:
        news.title = "N/A"

    return list