import tweepy
import pymongo

auth = tweepy.OAuthHandler("EpA1GcIuwplHnOlNHr0R3tjhw", "vpIW7n1fIxSAdZiv8Cp0YZSTQbNpgSMoZCkFjIEjophvXt6qvD")
auth.set_access_token("1426152528-w8GnV2Q5GvY6FCt9kssa1wWrZ52p9ze4e8MiCza", "g508BP9xcmokOn9Gkn3rxyK6sCFZViD3sjBK9A6sOmgaN")

api = tweepy.API(auth)
mongoclient = pymongo.MongoClient("mongodb://localhost:27017/")
tweedb = mongoclient["tweets"]
facciamoReteCol = tweedb["facciamoRete"]
for status in tweepy.Cursor(api.search, q='facciamorete').items(100):
    facciamoReteCol.insert_one(status._json)

SalviniChiacchieroneCol = tweedb["SalviniChiacchierone"]
for status in tweepy.Cursor(api.search, q='SalviniChiacchierone').items(100):
    SalviniChiacchieroneCol.insert_one(status._json)

banksyCol = tweedb["banksy"]
for status in tweepy.Cursor(api.search, q='banksy').items(100):
    banksyCol.insert_one(status._json)

myTweets = tweedb["nsfw_tweets"]
for status in api.user_timeline("00simmy"):
    myTweets.insert_one(status._json)