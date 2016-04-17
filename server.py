#!usr/bin/python
from flask import Flask, request, render_template
import requests
import json
import tweepy
import time
import datetime as DT
import calendar

consumer_key = "cFXaV6fAhsodXyvqSYNLVUPbE"
consumer_secret = "4vKaMFtIV2OI5FBiaE5qyHsukSg4k7khSMUg5zQO8IAlWZtF0C"
access_token = "721085655779041280-UsI8dIl90HQ8ONGumjVGW5w9108OcWa"
access_token_secret = "MuEv77YTZYRgU3UjTsxUoQyrcy7XdA3WaTg4XzUbTYIaB"

today = DT.date.today()
week_ago = today - DT.timedelta(days=7)

app = Flask('Twitter')

# index template
@app.route('/')
def form():
    return render_template('api.html')

@app.route('/getTime/', methods=['POST'])
def getTime():
    userName = request.form['username']
    userId = request.form['userid']

    if not userName and not userId:
      return render_template('error.html')
    elif not userName:
      screen_name = userId
    else:
      screen_name = userName

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)

    week = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    count = {}
    for day in week:
        count[day]={}
        for h in range(0,24):
            count[day][h] = 0

    ans = 0

    for user in tweepy.Cursor(api.followers, screen_name=screen_name).items():
        username = user.screen_name
        print username
        tweets = api.user_timeline(screen_name = username, count = 10, include_rts = True)
        for tweet in tweets:
            d = tweet.created_at
            hour = int(d.hour + d.minute / 60. + d.second / 3600)
            day = calendar.day_name[d.weekday()]
            count[day][hour] += 1
            if(count[day][hour] > ans):
                ans_day = day
                ans_hour = hour

    return render_template('result.html', ans_day=ans_day, ans_hour=ans_hour)


if __name__=='__main__':
  app.run(debug=True,host='0.0.0.0')