from playwright.sync_api import sync_playwright
from datetime import datetime
import os

# تنظیمات
URL = "https://market24hclock.com/"  # آدرس سایتی که می‌خوای اسکرین‌شات بگیری
SAVE_DIR = "screenshots"

# ایجاد پوشه ذخیره در صورت نیاز
os.makedirs(SAVE_DIR, exist_ok=True)

# گرفتن تاریخ و ساعت
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
screenshot_path = f"{SAVE_DIR}/screenshot_{timestamp}.png"

# گرفتن اسکرین‌شات
with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto(URL)
    page.screenshot(path=screenshot_path)
    browser.close()

print(f"Screenshot saved: {screenshot_path}")
