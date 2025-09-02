import os
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_URL = os.getenv("TELEGRAM_URL")
INSTAGRAM_URL = os.getenv("INSTAGRAM_URL")
GITHUB_URL = os.getenv("GITHUB_URL")
WEBSITE_URL = os.getenv("WEBSITE_URL")
YOUTUBE_URL = os.getenv("YOUTUBE_URL")
LINKEDIN_URL = os.getenv("LINKEDIN_URL")
print("Muhit o‘zgaruvchilari muvaffaqiyatli yuklandi ✅: ", TELEGRAM_URL)
print("Muhit o‘zgaruvchilari muvaffaqiyatli yuklandi ✅: ", INSTAGRAM_URL)
print("Muhit o‘zgaruvchilari muvaffaqiyatli yuklandi ✅:    ", GITHUB_URL)
print("Muhit o‘zgaruvchilari muvaffaqiyatli yuklandi ✅:    ", WEBSITE_URL)
print("Muhit o‘zgaruvchilari muvaffaqiyatli yuklandi ✅:    ", YOUTUBE_URL)
print("Muhit o‘zgaruvchilari muvaffaqiyatli yuklandi ✅:    ", LINKEDIN_URL)
EXCHANGE_API_KEY = os.getenv("EXCHANGE_API_KEY")
print("Muhit o‘zgaruvchilari muvaffaqiyatli yuklandi ✅: ", EXCHANGE_API_KEY)
