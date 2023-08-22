from flask import Flask, render_template
import tweepy

app = Flask(__name__)

# Twitter API keys
consumer_key = "QUVIeEVNYW1UakktZTdiOHR0a2s6MTpjaQ"
consumer_secret = "VQTBa2riZRO6_PB_N31qcVOrghN5itk8mCo7TLINLiE72s_Y5r"
access_token = "1693714433342889984-n4MudpiOaeSZxsmhQsfVs2IwNwYamD"
access_token_secret = " GEAeewgBRgHMrCbA2E5b4AF3oCS0RK5uEXZ8MUieRbYQG"

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
