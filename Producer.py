from kafka import KafkaProducer
import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
from transformers import pipeline
import json
import configparser


#Twitter API Authentication credentials
consumer_key = "JP13zwhZ43Fc3HgWqgE0IWQ0f"
consumer_secret = "wSKele66jHJLG63yfmXhCK0Xcgxmxo4ncW2yYxKj5T994cjnjs"
access_token = "2195651750-ba2mJStC1uWrppLz0tsfKrSSkT1E0CFk9NEIfJz"
access_secret = "niTGsCbaE1kqrRp3czoPgrO2sW17kn0gjPbm2Jwfoet8p"





def perform_analysis(tweet):
	transformer_sentiment = classifier(json.loads(tweet)["text"])


	transformer_sentiment = transformer_sentiment[0]['label']

	return transformer_sentiment



# Twitter Stream Listener

class KafkaPushListener(StreamListener):
    def __init__(self):
        # localhost:9092 = Default Zookeeper Producer Host and Port Adresses
        self.producer = KafkaProducer(bootstrap_servers=['localhost:9092'])



    def on_data(self, data):
        # Producer produces data for consumer
        # Data comes from Twitter
        transformer_sentiment = perform_analysis(data)
        self.producer.send(config['arguments']['topic'], transformer_sentiment.encode('utf-8'))
        return True

    def on_error(self, status):
        print("status error - ",status)
        return True



if __name__ == "__main__":


	# TWITTER API AUTH
	auth = OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_secret)
	api = tweepy.API(auth)
	config = configparser.ConfigParser()
	config.read('config.ini')


	# Search String to search on Twitter.
	search_text = config['arguments']['search_string']
	# search_text = "#olympics"

	classifier = pipeline('sentiment-analysis')


	listener = KafkaPushListener()
	twitter_stream = Stream(auth, listener)

	twitter_stream.filter(track=['#olympics'])