import tweepy

# Set up the Twitter API credentials
consumer_key = "your_consumer_key"
consumer_secret = "your_consumer_secret"
access_token = "your_access_token"
access_token_secret = "your_access_token_secret"

# Authenticate with the Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Create the API object
api = tweepy.API(auth)

# Set the location and language parameters for the trends API call
WOEID = 1 # Set the WOEID to the global location
language = "en" # Set the language to English

# Get the current trending topics
trends = api.trends_place(WOEID, lang=language)

# Loop through the trends and print out the name and tweet volume for each one
for trend in trends[0]["trends"]:
    print(trend["name"] + " - " + str(trend["tweet_volume"]) + " tweets")
