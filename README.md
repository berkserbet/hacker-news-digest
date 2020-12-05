# Hacker News Digest

Opens up top Hacker News stories in browser tabs. Eventually it will open the stories that are most relevant to you.

# To Run

```
python open_sites.py
```
Tested on python 3.8

# Configurations

Configurations can be changed in [settings.py](settings.py).

Number of top stories opened can be modified using `HACKERNEWS_TOP_ARTICLES`

Training can be toggle on/off using `TRAINING`. Currently it has my data in there but you can delete `data/training.csv` to start your own. In the csv file, adjust rating column for each article based on the following criterea:

| Rating | Meaning                      |
|--------|------------------------------|
| -1     | Unrated                      |
| 0      | Horrible                     |
| 1      | Not for me                   |
| 2      | Only if it's a slow news day |
| 3      | Not bad                      |
| 4      | Pretty Good                  |
| 5      | Love It                      |

# Long Term Goal

The long term goal of this project is to be able to predictably open the stories I'm most interested in. For now I'm just collecting data.