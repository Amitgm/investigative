import tweepy
from textblob import TextBlob
import csv

#wiki =TextBlob("Amit is a very good guy ")

#print(wiki.tags)

#print(wiki.words)
#print(wiki.sentiment.polarity)


consumer_key='Q9Ar4YJ6gnanrKkVKB8sj2DO2'
consumer_secret='dn2jzWpJQrDWcM0eO6GS6PLwXq01fC8lbYXlGCGJufQJ54VPYf'

access_token='3176895145-VVBj31QO2kpj3w13som5IDQMrRlXlBbbAVtHCjR'
access_secret='RS2wV0T7JOWwtpSzroJ9lnjDYbfxQXBjuvdmcgnESe11c'

auth=tweepy.OAuthHandler(consumer_key,consumer_secret)

auth.set_access_token(access_token,access_secret)

api=tweepy.API(auth)

public_tweets= api.search('Modi')

opinions=[]
tweets=[]

for tweet in public_tweets:
    #print(tweet.text)
    analysis=TextBlob(tweet.text)
    #print(analysis.sentiment)
    tweets.append(tweet.text)
    if analysis.sentiment.polarity>0.5:
        
        opinions.append('pos')
    else:
        opinions.append('neg')
        
if opinions.count("pos")> opinions.count("neg"):  
    print("the tweet is overall positive")
else:
    print("the tweet is overall negative")
