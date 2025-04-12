import tweepy
import random
import time
from datetime import datetime, timedelta
import os

# Logging function
def log(message):
    with open("bot_log.txt", "a") as f:
        f.write(f"{datetime.now()}: {message}\n")

# X API Credentials
API_KEY = "bClwKkhHXJAtbCvQHCwVEN4zf"
API_SECRET = "QudRQAVqrzxPHnAwmn1D4NXfn5XRfgrHZsQsZGNUHskx1fIuei"
ACCESS_TOKEN = "1907666383397146624-rouhd0UrW0s0Rqo1uml3BWlUW56xIT"
ACCESS_TOKEN_SECRET = "xNVlNsVEJQdfT4QUMcgs7oLY6ZJq310ssSS4WfuuSvtVy"

# Authenticate with X v2 API
try:
    client = tweepy.Client(
        consumer_key=API_KEY,
        consumer_secret=API_SECRET,
        access_token=ACCESS_TOKEN,
        access_token_secret=ACCESS_TOKEN_SECRET
    )
    log("Authenticated with X API")
except Exception as e:
    log(f"Failed to authenticate: {str(e)}")
    raise

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
all_hashtags = ["#HealthyLifestyle", "#Wellness", "#HealthyLiving", "#CleanEating", "#HealthAndWellness", "#FitAndHealthy", "#MindBody", "#HealthyHabits", "#SelfCare", "#Nutrition"]

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
    try:
        item = products[counter % 15]
        tags = random.sample(hashtags, 2)
        tweet = f"{item['title']}\n{item['amazon']} {item['youtube']}\n{tags[0]} {tags[1]}"
        log(f"About to post daily: {tweet}")
        client.create_tweet(text=tweet)
        print(f"Posted: {tweet}")
    except Exception as e:
        log(f"Error posting daily: {str(e)}")

# Bi-weekly retro site post
def biweekly_retro_post():
    try:
        tweet = f"https://mpro25.github.io/retro_site_latest/ {random.choice(all_hashtags)}"
        log(f"About to post retro: {tweet}")
        client.create_tweet(text=tweet)
        print(f"Posted retro site: {tweet}")
    except Exception as e:
        log(f"Error posting retro: {str(e)}")

# Tri-weekly Rumble post with duplicate check
def triweekly_rumble_post(last_rumble_time):
    try:
        tweet = "https://rumble.com/c/c-7682877\n" + " ".join(all_hashtags)
        if (now - last_rumble_time).total_seconds() > 86400:  # 24-hour cooldown
            log(f"About to post Rumble: {tweet}")
            client.create_tweet(text=tweet)
            print(f"Posted Rumble: {tweet}")
            return now
        return last_rumble_time
    except Exception as e:
        log(f"Error posting Rumble: {str(e)}")
        return last_rumble_time

# Main loop
counter = load_counter()
last_biweekly = [datetime.now() - timedelta(days=4), datetime.now() - timedelta(days=4)]
last_triweekly = [datetime.now() - timedelta(days=3), datetime.now() - timedelta(days=2), datetime.now() - timedelta(days=1)]
last_rumble_time = datetime.now() - timedelta(days=1)

while True:
    now = datetime.now() - timedelta(hours=5)  # EST (UTC-5)
    log("Bot is running...")

    try:
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

        # Bi-weekly retro site posts at 11:22 AM EST (2x/week)
        if now.hour == 11 and now.minute == 22:
            if (now - last_biweekly[0]).days >= 3 and random.random() < 0.3:  # ~2x/week
                biweekly_retro_post()
                last_biweekly[0] = now
                time.sleep(60)
            if (now - last_biweekly[1]).days >= 3 and random.random() < 0.3:
                biweekly_retro_post()
                last_biweekly[1] = now
                time.sleep(60)

        # Tri-weekly Rumble posts at 2:36 PM EST (3x/week)
        if now.hour == 14 and now.minute == 36:
            if (now - last_triweekly[0]).days >= 2 and random.random() < 0.5:  # ~3x/week
                last_rumble_time = triweekly_rumble_post(last_rumble_time)
                last_triweekly[0] = now
                time.sleep(60)
            if (now - last_triweekly[1]).days >= 2 and random.random() < 0.5:
                last_rumble_time = triweekly_rumble_post(last_rumble_time)
                last_triweekly[1] = now
                time.sleep(60)
            if (now - last_triweekly[2]).days >= 2 and random.random() < 0.5:
                last_rumble_time = triweekly_rumble_post(last_rumble_time)
                last_triweekly[2] = now
                time.sleep(60)
    except Exception as e:
        log(f"Main loop error: {str(e)}")

    time.sleep(10)  # Check every 10 seconds