# -*- coding: utf-8 -*-


# 오픈한글 감성사전 긍정,부정 JSON 파싱
import requests
import json

word_input = raw_input("word input : ")



sentiment_url = 'http://api.openhangul.com/dic?api_key=20141107174448&q='+word_input
sentiment_request = requests.get(sentiment_url)

try:
    decoded = json.loads(sentiment_request.text)

    # pretty printing of json-formatted string
    print json.dumps(decoded, sort_keys=True, indent=1  )

    print "JSON parsing example: ", decoded['word']
    print "JSON parsing example: ", decoded['type']
    print "JSON parsing example: ", decoded['sentiment']
    print "JSON parsing example: ", decoded['sentiment_score']


except (ValueError, KeyError, TypeError):
    print "JSON format error"