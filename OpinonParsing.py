# -*- coding: utf-8 -*-


# 오픈한글 감성사전 긍정,부정 JSON 파싱
import requests
import json
import urllib
import BeautifulSoup

word_input = raw_input("word input : ")
url = 'http://api.openhangul.com/basic?q=' + word_input


r = requests.get(url)

data = urllib.urlopen(url)
soup = BeautifulSoup.BeautifulSoup(data)
soup_split = soup.prettify()
div = soup_split.split(",")
soup_split2 = div[1]
div2 = soup_split2.split(":")
soup_split3 = div2[1]
div3 = soup_split3.split('"')
basicword = div3[1]


sentiment_url = 'http://api.openhangul.com/dic?api_key=20141107174448&q='+basicword
sentiment_request = requests.get(sentiment_url)

try:
    decoded = json.loads(sentiment_request.text)

    # pretty printing of json-formatted string

    print "JSON parsing example: ", decoded['word']
    print "JSON parsing example: ", decoded['type']
    print "JSON parsing example: ", decoded['sentiment']
    print "JSON parsing example: ", decoded['sentiment_score']


except (ValueError, KeyError, TypeError):
    print "JSON format error"