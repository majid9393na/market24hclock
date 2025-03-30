name: Daily Screenshot

on:
  schedule:
    - cron: "0 10 * * *"  # اجرای خودکار هر روز ساعت 10:00 UTC
  workflow_dispatch:  # امکان اجرای دستی

jobs:
  capture_screenshot:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repository
        uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v3
        with:
          python-version: "3.x"

      - name: Install dependencies
        run: pip install playwright && playwright install

      - name: Run screenshot script
        run: python screenshot.py  # اطمینان حاصل کن که این مسیر صحیح باشه

      - name: Commit and push screenshot
        run: |
          git config --global user.name "GitHub Actions"
          git config --global user.email "actions@github.com"
          git add screenshots/
          git commit -m "New screenshot"
          git push
