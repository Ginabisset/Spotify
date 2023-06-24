from bs4 import BeautifulSoup
import requests
import urllib.parse

question = input('What year would you like to travel to?Format YYYY-MM-DD')

URL = f'https://www.billboard.com/charts/hot-100/{question}'

# Scrapes Billboard 100 for the songs at that date
response = requests.get(URL).content
soup = BeautifulSoup(response, 'html.parser')


tag = [item.getText() for item in soup.findAll(name='h3',
                                               id="title-of-a-story",
                                               class_="c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021"
                                                      " lrv-u-font-size-18@tablet lrv-u-font-size-16 u-line-height-125 "
                                                      "u-line-height-normal@mobile-max a-truncate-ellipsis "
                                                      "u-max-width-330"" u-max-width-230@tablet-only")]
# Reformat the HTML to be URL encoded
tag_titles = [item.replace('\n','') for item in tag]
song_titles_format = [item.replace('\t','')for item in tag_titles]
song_titles = [f'remaster%20track:{urllib.parse.quote(item)}%20'
               f'year:{question.split("-")[0]}' for item in song_titles_format]
