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

# Authenticate with X
auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

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

# Hashtags
hashtags = ["#HealthyLifestyle", "#Wellness", "#HealthyLiving", "#CleanEating", "#HealthAndWellness", "#FitAndHealthy", "#MindBody", "#HealthyHabits", "#SelfCare", "#Nutrition"]

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
    api.update_status(tweet)
    print(f"Posted: {tweet}")

# Bi-weekly random post
def biweekly_post():
    rewrites = [
        "Stay active easily! Gym, nature, or home—whatever works. Cheap gear, tons of moves. Get it done! https://mpro25.github.io/retro_site_latest/",
        "Moving’s no biggie—gym, sports, or chill at home. Affordable gear, endless exercises. Stay in it! https://mpro25.github.io/retro_site_latest/",
        "Keep active, no fuss! Gym, outdoors, or home—use cheap gear for a million workouts. Let’s go! https://mpro25.github.io/retro_site_latest/"
    ]
    tweet = f"{random.choice(rewrites)} {random.choice(hashtags)}"
    api.update_status(tweet)
    print(f"Bi-weekly posted: {tweet}")

# Weekly Rumble post
def weekly_rumble():
    tweet = "https://rumble.com/c/c-7682877\n" + " ".join(hashtags)
    api.update_status(tweet)
    print(f"Rumble posted: {tweet}")

# Daily comment
def daily_comment():
    account = random.choice(comment_accounts)
    tweets = api.user_timeline(screen_name=account, count=10, exclude_replies=True, include_rts=False)
    if tweets:
        tweet_id = random.choice(tweets).id
        rewrites = [
            "Yo, staying active’s easy—move however! Cheap gear, tons of fun exercises. Get it done! https://mpro25.github.io/retro_site_latest/",
            "Active life? No sweat—gym, home, or wild. Affordable gear, endless moves. Keep it up! https://mpro25.github.io/retro_site_latest/",
            "Move it, no big deal! Gym, nature, or couch—cheap gear works wonders. Let’s roll! https://mpro25.github.io/retro_site_latest/"
        ]
        comment = f"{random.choice(rewrites)}"
        api.update_status(status=comment, in_reply_to_status_id=tweet_id, auto_populate_reply_metadata=True)
        print(f"Commented on @{account}: {comment}")

# Main loop
counter = load_counter()
last_biweekly = [datetime.now() - timedelta(days=4), datetime.now() - timedelta(days=4)]
last_weekly = datetime.now() - timedelta(days=7)
last_comment = datetime.now() - timedelta(days=1)

while True:
    now = datetime.now() - timedelta(hours=5)  # EST (UTC-5)
    today = now.date()

    # Daily posts (10:27 AM EST and 7:17 PM EST)
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

    # Bi-weekly random posts (2x/week)
    if (now - last_biweekly[0]).days >= 3 and random.random() < 0.1:  # ~2x/week
        biweekly_post()
        last_biweekly[0] = now
        time.sleep(60)
    if (now - last_biweekly[1]).days >= 3 and random.random() < 0.1:
        biweekly_post()
        last_biweekly[1] = now
        time.sleep(60)

    # Weekly Rumble post
    if (now - last_weekly).days >= 7 and random.random() < 0.2:  # ~1x/week
        weekly_rumble()
        last_weekly = now
        time.sleep(60)

    # Daily comment
    if (now - last_comment).days >= 1:
        daily_comment()
        last_comment = now
        time.sleep(60)

    time.sleep(10)  # Check every 10 seconds