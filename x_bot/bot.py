import tweepy
import random
import time
from datetime import datetime, timedelta
import os

# X API Credentials
API_KEY = "bClwKkhHXJAtbCvQHCwVEN4zf"
API_SECRET = "QudRQAVqrzxPHnAwmn1D4NXfn5XRfgrHZsQsZGNUHskx1fIuei"
ACCESS_TOKEN = "1907666383397146624-rouhd0UrW0s0Rqo1uml3BWlUW56xIT"
ACCESS_TOKEN_SECRET = "xNVlNsVEJQdfT4QUMcgs7oLY6ZJq310ssSS4WfuuSvtVy"

# Authenticate with X v2 API
client = tweepy.Client(
    consumer_key=API_KEY,
    consumer_secret=API_SECRET,
    access_token=ACCESS_TOKEN,
    access_token_secret=ACCESS_TOKEN_SECRET
)

# Product list for daily posts
products = [
    {"title": "JBL Go 4 - Ultra Portable, Waterproof, and Dustproof Bluetooth Speaker w/ Punchy bass - 7 hr Battery", "amazon": "https://amzn.to/4clWI3Y", "youtube": "https://youtube.com/shorts/7bGA_VD1iuM?feature=share"},
    {"title": "Fitness Home Gym Mat - Workout Floor Protection for Treadmill, Bike, Yoga, or Standing Desk", "amazon": "https://amzn.to/3DTLTJL", "youtube": "https://youtube.com/shorts/ztqx3LJ-sIg?feature=share"},
    {"title": "Balance Board - Balancing Stability Trainer to Improve Balance, Surf Trainer & Physical Therapy", "amazon": "https://amzn.to/4jafIoc", "youtube": "https://youtube.com/shorts/i4qCUlxmZBk?feature=share"},
    {"title": "Soft Shell Non Slip, Medicine Exercise Ball for Fitness, Plyometrics, Cross Training, & Home Gym", "amazon": "https://amzn.to/3YiPIin", "youtube": "https://youtube.com/shorts/mTksoGDJt6U?feature=share"},
    {"title": "Pull Up Dip Station Assistive Trainer Multi Function Home Gym Strength Training Fitness", "amazon": "https://amzn.to/4cnJMuy", "youtube": "https://youtube.com/shorts/ewHw8xxUnc4?feature=share"},
    {"title": "Soft Kettlebell, Strength Training Kettlebells & Home Workouts, Ideal for Men, Women, & Beginners", "amazon": "https://amzn.to/3XJNFDR", "youtube": "https://youtube.com/shorts/lIeqXL6P6UM?feature=share"},
    {"title": "Wireless Earbuds, Bluetooth 5.4 Headphones, Wireless Earphones, LED, In-Ear, Bluetooth, Waterproof", "amazon": "https://amzn.to/4ianxcQ", "youtube": "https://youtube.com/shorts/HZ9vd2_xC9o?feature=share"},
    {"title": "Rowing Machine, Foldable Rower for Home Use, Tablet Holder and Comfortable Seat Cushion", "amazon": "https://amzn.to/4jjhovS", "youtube": "https://youtube.com/shorts/cRmy2AP0JoU?feature=share"},
    {"title": "Strength Training Equipment - Resistance Bands", "amazon": "https://amzn.to/4jdOuwT", "youtube": "https://youtube.com/shorts/F6vi-UuU1gc?feature=share"},
    {"title": "Massage Gun, Deep Tissue Massager for Athletes, Electric Muscle Percussion Massager for Any Pain", "amazon": "https://amzn.to/4jhkhNI", "youtube": "https://youtube.com/shorts/DN2e7nkxrdY?feature=share"},
    {"title": "Kettlebell Weight Set Strength Training and Weightlifting Equipment for Home Gyms", "amazon": "https://amzn.to/3FNEg8i", "youtube": "https://youtube.com/shorts/z8Ee5UeahzQ?feature=share"},
    {"title": "Massage Table Portable Lash Beds Spa Bed Massage Couch Foldable Spa Tables Adjustable 2 Fold", "amazon": "https://amzn.to/3DTMV8B", "youtube": "https://youtube.com/shorts/RMwYfBeu4hg?feature=share"},
    {"title": "Exercise Ball, Pilates, Stability, Yoga, Heavy Duty Ball for Fitness, Core Workout, Physical Therapy", "amazon": "https://amzn.to/3YajzJJ", "youtube": "https://youtube.com/shorts/vjD6zUD9JzY?feature=share"},
    {"title": "Push Up Bars Strength Training - Home Fitness Training", "amazon": "https://amzn.to/4iOhvQ0", "youtube": "https://youtube.com/shorts/jER_ifnIMC4?feature=share"},
    {"title": "Adjustable Steel Jump Rope Workout with Foam Handles for Fitness, Home Exercise", "amazon": "https://amzn.to/3FUtfBY", "youtube": "https://youtube.com/shorts/yH2sM4Qo-58?feature=share"}
]

# Hashtags for posts
hashtags = ["#HealthyLifestyle", "#Wellness", "#HealthyLiving", "#HealthAndWellness", "#FitAndHealthy", "#MindBody", "#SelfCare", "#Nutrition"]

# Comment accounts
comment_accounts = ["menshealthmag", "womenshealthmag", "health_com_", "jamesclear", "who"]

# Load or initialize counter
def load_counter():
    if os.path.exists("counter.txt"):
        with open("counter.txt", "r") as f:
            return int(f.read().strip())
    return 0

def save_counter(counter):
    with open("counter.txt", "w") as f:
        f.write(str(counter))

# Daily post function
def daily_post(counter):
    item = products[counter % 15]
    tags = random.sample(hashtags, 2)
    tweet = f"{item['title']}\n{item['amazon']} {item['youtube']}\n{tags[0]} {tags[1]}"
    client.create_tweet(text=tweet)
    print(f"Posted: {tweet}")

# Daily comment function
def daily_comment():
    account = random.choice(comment_accounts)
    user = client.get_user(username=account)
    if user.data:
        tweets = client.get_users_tweets(id=user.data.id, max_results=10, exclude=["replies", "retweets"])
        if tweets.data:
            tweet_id = random.choice(tweets.data).id
            rewrites = [
                "Hey, moving’s no biggie—gym, woods, or couch, just go! Cheap gear, tons of fun moves. Get it done! https://mpro25.github.io/retro_site_latest/",
                "Active? Easy peasy—hit the gym, roam, or chill. Affordable gear, endless workouts. Keep it rockin’! https://mpro25.github.io/retro_site_latest/",
                "Stay fit, no fuss! Gym, nature, or home—cheap gear’s got a million moves. Let’s roll! https://mpro25.github.io/retro_site_latest/"
            ]
            comment = random.choice(rewrites)
            client.create_tweet(text=comment, in_reply_to_tweet_id=tweet_id)
            print(f"Commented on @{account}: {comment}")

# Main loop
counter = load_counter()

while True:
    now = datetime.now() - timedelta(hours=5)  # EST (UTC-5)

    # Daily posts at 10:27 AM and 7:17 PM EST
    if now.hour == 10 and now.minute == 27:
        daily_post(counter)
        counter += 1
        save_counter(counter)
        time.sleep(60)
    elif now.hour == 19 and now.minute == 17:
        daily_post(counter)
        counter += 1
        save_counter(counter)
        time.sleep(60)

    # Daily comments at 11:27 AM and 8:17 PM EST
    if now.hour == 11 and now.minute == 27:
        daily_comment()
        time.sleep(60)
    elif now.hour == 20 and now.minute == 17:
        daily_comment()
        time.sleep(60)

    time.sleep(10)  # Check every 10 seconds