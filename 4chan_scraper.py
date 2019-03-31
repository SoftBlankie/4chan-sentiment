from bs4 import BeautifulSoup
import requests
import datetime
import json

from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

url = 'http://boards.4channel.org'
headers = {'User-Agent': 'Mozilla/5.0'}

client = language.LanguageServiceClient()

data = []

def generate_pages(board):
    pages = []

    page = url + '/' + board + '/'
    pages.append(page)

    for i in range(2, 10):
        pages.append(page + str(i))

    return pages

def scrape_text(post):
    d = dict()

    d['text'] = post.select_one('blockquote').text.strip()

    document = types.Document(
    content=d['text'],
    type=enums.Document.Type.PLAIN_TEXT)

    sentiment = client.analyze_sentiment(document=document).document_sentiment

    d['sentiment score'] = sentiment.score
    d['sentiment magnitude'] = sentiment.magnitude

    overall_sentiment += sentiment.score
    count += 1

    data.append(d)

def main():
    global overall_sentiment, count

    board = input("Input board acronym: ")

    pages = generate_pages(board)

    print("generated page")

    for page in pages:
        r = requests.get(page,headers=headers)
        soup = BeautifulSoup(r.content, 'html.parser')

        posts = soup.select('.board .thread .postContainer')

        for post in posts:
            scrape_text(post)

            print("finished thread")

    overall_sentiment /= count

    with open('board_a.json', 'w') as f:
        json.dump(data, f)

    data.clear()

    d = dict()
    d['board'] = board
    d['date'] = datetime.datetime.now()
    d['overall_sentiment'] = overall_sentiment
    data.append(d)

    with open('overall_sentiment.json', 'w') as f:
        json.dump(data, f)

main()
