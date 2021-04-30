import tweepy
import pandas as pd
import numpy as np
import os

# Create a hashtags list
search_list = ["vote",
            "uselection",
            "election",
            "stimulus check",
            "joe biden",
            "stimulus",
            "climate change",
            "environment",
            "global warming"]

# Create a search list
hashtags = ["#stimuluscheck",
            "#biden",
            "#stimulus",
            "#climatechange",
            "#environment",
            "#globalwarming",
            "#uselection",
            "#vote",
            "#election"]


# Get the necessary API information from a text file
#with open('twitter_api.txt') as file:
#    consumer_key, consumer_key_secret, access_token, access_token_secret = [line.strip('\n').split('=')[1] for line in file.readlines()]

consumer_key ="t37dWre7nh5Zl68H0Mhnd5Ptt"
consumer_key_secret="rBlGiKaN9RmsY7b2nq0c9wUUPfrSn4uKC8egA5DS0HKD3c6RiH"
access_token="1369718031769759746-a8vE51K7o8oLf6fD1XNKOnDwz4Gjaz"
access_token_secret= "FR2l4XIdk26k8DEaqqsBVkAXpD9RqAoehRtOvO6eJVRpG"
# Setup tweepy with Twitter credentials
auth = tweepy.OAuthHandler(consumer_key, consumer_key_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

# Define a function to get tweets
def get_tweets(search, isHashtag):
    
    # Create a pandas DataFrame
    df_temp = pd.DataFrame(columns=["Content", "Location", "Username", "Retweet-Count", "Favorites", "Created at"])
    
    # Get the tweets
    tweets = tweepy.Cursor(api.search, q= search+" -filter:retweets",
            lang="en",since="2020-07-01", tweet_mode='extended').items(1500)
    
    # Iterate over tweets
    for tweet in tweets:
        content = tweet.full_text
        username = tweet.user.screen_name
        location = tweet.user.location
        created_at = tweet.created_at
        retweetcount = tweet.retweet_count
        favorites = tweet.favorite_count
        
        # Create a list consists of the features
        retrieved = [content, location, username, retweetcount, favorites, created_at]
        
        # Append list to the DataFrame
        df_temp.loc[len(df_temp)] = retrieved
        
    # Generate unique filename
    path = os.getcwd()
    
    # Generate a filename for hashtags or specific word
    if isHashtag:
        filename = path + '/output/' + search[1:] + '_hashtag.csv'
    else:
        filename = path + '/output/' + search.replace(" ", "") + '_wordsearch.csv'
    # Save the csv file
    df_temp.to_csv(filename)


# Call get_tweets function for each hashtag and search word

for hashtag in hashtags:
    get_tweets(hashtag, isHashtag=True)

#for search in search_list:
#    get_tweets(search, isHashtag=False)
