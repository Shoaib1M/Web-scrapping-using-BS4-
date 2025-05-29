# 🛒 Amazon Price Tracker

An intermediate-level Python project that tracks the price of a product on Amazon and sends you an email alert when the price drops below a specified threshold.

## 💡 Project Overview

This project uses:
- `requests` and `BeautifulSoup` for web scraping
- Custom headers to simulate a browser request
- Email alerts using the `smtplib` module

You will:
- Scrape the live Amazon page for product title and price
- Set a target price
- Receive an email when the price drops below your target
