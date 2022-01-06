import sqlite3
from datetime import datetime
from support.allTickerDataFunctions import dataFromAllStreams
from support.allNewsDataFunctions import getAllNewArticles

conn = sqlite3.connect('data.db')
csr = conn.cursor()

# csr.execute("""
# CREATE TABLE IF NOT EXISTS keyWordsToScrape (
#     keywaord TEXT
# )
# """)

class Scrapper:
    def __init__(self):
        self.newsInsertString = f"INSERT INTO newsData VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)"
        self.last1hNewsTitlesList = []
        self.lastTimestamp = str(datetime.now().strftime('%Y-%m-%d %H:%M:00'))

    def getKeywordList(self):
        csr.execute("""
        SELECT * FROM keyWordsToScrape
        """)
        keywordTuple = csr.fetchall()
        keywordList = list()
        for keyword in keywordTuple:
            keywordList.append(keyword[0])
        return keywordList

    def getNewsData(self, keywordList):
        newsData, self.last1hNewsTitlesList = getAllNewArticles(last1hNewsTitlesList = self.last1hNewsTitlesList, listOfKeywords = keywordList)
        return newsData

    def insertNewsData(self):
        keywordList = Scrapper.getKeywordList(self)
        newsData = Scrapper.getNewsData(self, keywordList)
        for singleArticle in newsData:
            csr.execute(self.newsInsertString, (self.newTimestamp, singleArticle['keyword'], singleArticle['title'], singleArticle['dateTimePublished'], singleArticle['link'], singleArticle['text'], singleArticle['keywords'], singleArticle['summary'], singleArticle['author']))
        conn.commit()
        return len(newsData)

    def getAndStoreData(self):
        while True:
            self.newTimestamp = str(datetime.now().strftime('%Y-%m-%d %H:%M:00'))
            if self.newTimestamp > self.lastTimestamp:
                totalNewArticles = Scrapper.insertNewsData(self)
                print(f"{totalNewArticles} Aritlces were inserted at {self.newTimestamp}")

_ = Scrapper()
_.getAndStoreData()