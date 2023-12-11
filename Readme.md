# Python News Emailer

This is a simple Python script that fetches news related to Python programming from the NewsAPI and sends it as an email.

## How to Use

1. Install the required Python packages by running `pip install -r requirements.txt`.
2. Replace the `api_key` variable in `main.py` with your NewsAPI key.
3. Update the `send_email` function in `send_email.py` with your email credentials and recipient's email.
4. Run the script with `python main.py`.

## Dependencies

- Python 3
- requests
- Your email server's Python library (e.g., smtplib for Gmail)

## Note

This script is set to fetch news from a specific date. You may want to update the date in the URL to fetch the latest news.