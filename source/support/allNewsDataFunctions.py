from pygooglenews import GoogleNews
from newspaper import Article
from datetime import datetime
from newspaper import Config
from retry import retry
import nltk
import json
import time

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0'
gn = GoogleNews(lang = 'en', country = 'IN', timeout = 5)
config = Config()
config.browser_user_agent = user_agent
config.request_timeout = 5
config.memoize_articles = False
config.fetch_images = False

nltk.download('punkt')

def listToString(listToConvert):
    oneStr = '\''
    for tempStr in listToConvert:
        oneStr = oneStr + tempStr + ', '
    oneStr = oneStr[:-2] + '\''
    return oneStr

@retry()
def getListOfArticles(newsFor):
    if newsFor == 'BUSINESS' or newsFor == 'NATION' or newsFor == 'WORLD':
        newsData = gn.topic_headlines(newsFor)
    else:
        newsData = gn.search(newsFor, when = '1h')
    time.sleep(1)

    tempArticleList = []

    for articles in newsData['entries']:
        data = {
        'title' : articles['title'],
        'dateTimePublished' : articles['published'],
        'link' : articles['link']
        }
        tempArticleList.append(data)

    del newsData
    
    return tempArticleList

def getArticleData(article, srtQuery):
    articleToParse = Article(article['link'], config=config)

    time.sleep(1)
        
    try:
        articleToParse.download()
        articleToParse.parse()
        articleToParse.nlp()
        text = articleToParse.text
        keywords = articleToParse.keywords
        summary = articleToParse.summary
        author = articleToParse.authors

    except Exception as e:
        text = ''
        keywords = []
        summary = ''
        author = []

    del articleToParse

    dataToStore = {
        'keyword' : srtQuery,
        'title' : article['title'],
        'dateTimePublished' : article['dateTimePublished'],
        'link' : article['link'],
        'text' : text,
        'keywords' : json.dumps(keywords),
        'summary' : summary,
        'author' : json.dumps(author)
    } 
            
    return dataToStore

last1hNewsTitlesList = []

def getAllNewArticles(last1hNewsTitlesList, listOfKeywords):
    last1hNewsTitlesList = last1hNewsTitlesList
    allNewArticles = []
    for srtQuery in listOfKeywords:
        tempArticleList = getListOfArticles(srtQuery)
        for article in tempArticleList:
            if article['title'] not in last1hNewsTitlesList:
                last1hNewsTitlesList.append(article['title'])
                last1hNewsTitlesList = last1hNewsTitlesList[-3500:]
                singleArticleData = getArticleData(article, srtQuery)
                allNewArticles.append(singleArticleData)
    return allNewArticles, last1hNewsTitlesList