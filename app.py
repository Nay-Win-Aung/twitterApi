from flask import Flask, render_template
import tweepy

app = Flask(__name__)

# Twitter API keys
consumer_key = " kL1XTAwLH1AYwchyvYMfKYvO5"
consumer_secret = "WKONQT6Z7Pma7HYYz0yjaJgqsKfHcpDQ5HWZbsO4tnFdXYQfN3"
access_token = "1484820034522599424-qnvmzEFRbOrCnqeEDRqSGyqgNyMNMd"
access_token_secret = "29XOCqiCIFuXr1c7WR5iqHJkQEAshktDWn4S4w02wNCtq"

# Authenticate with Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

@app.route('/')
def index():
    keyword = "technology"
    tweets = api.search(q=keyword, lang="en", count=5)

    return render_template('index.html', keyword=keyword, tweets=tweets)

if __name__ == '__main__':
    app.run(debug=True)
