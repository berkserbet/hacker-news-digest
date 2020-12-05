import requests
from settings import HACKERNEWS_API_URL, HACKERNEWS_TOP_ARTICLES, OTHER_SITES
import webbrowser

def open_sites():
    urls = get_hackernews_urls()
    urls += OTHER_SITES
    open_urls(urls)

def get_hackernews_urls():
    ''' get top stories urls

    Uses https://github.com/HackerNews/API

    '''
    response = requests.get(HACKERNEWS_API_URL + 'topstories.json?print=pretty')
    story_ids = response.json()

    urls = []
    for idx in range(HACKERNEWS_TOP_ARTICLES):
        story_id = str(story_ids[idx])
        response = requests.get(HACKERNEWS_API_URL + 'item/' + story_id + '.json?print=pretty')
        story = response.json()
        urls.append(story['url'])

    return urls    

def open_urls(urls):
    for link in urls:
        webbrowser.open(link, new=2)

if __name__ == "__main__":
    open_sites()