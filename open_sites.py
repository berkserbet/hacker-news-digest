import requests
from settings import HACKERNEWS_API_URL, HACKERNEWS_TOP_ARTICLES, TRAINING_DATA_PATH, TRAINING
import webbrowser
import pandas as pd
import os

def open_sites():
    news = get_hackernews()
    urls = [story['url'] for story in news]
    open_urls(urls)
    if TRAINING:
        add_to_training_data(news)

def get_hackernews():
    ''' get top stories

    Uses https://github.com/HackerNews/API

    '''
    response = requests.get(HACKERNEWS_API_URL + 'topstories.json?print=pretty')
    story_ids = response.json()

    news = []
    for idx in range(HACKERNEWS_TOP_ARTICLES):
        story_id = str(story_ids[idx])
        response = requests.get(HACKERNEWS_API_URL + 'item/' + story_id + '.json?print=pretty')
        story = response.json()
        if story['type'] == 'story':
            news.append(story)
    return news    

def open_urls(urls):
    for link in urls:
        webbrowser.open(link, new=2)

def add_to_training_data(news):
    '''Creats/adds to a csv that contains stories for the user to enter a rating
    '''
    news_df = pd.DataFrame(news)
    news_df['rating'] = -1

    # add header if new file
    if not os.path.isfile(TRAINING_DATA_PATH):
        news_df.to_csv(TRAINING_DATA_PATH, header=True)
    else:
        news_df.to_csv(f, mode='a', index=False)


if __name__ == "__main__":
    open_sites()