# Python News Fetcher

This is a Python script that fetches the top 20 news articles related to Python programming from the NewsAPI.

## Installation

1. Clone the repository
2. Install the required packages using pip:

```bash
pip install -r requirements.txt
```

## Usage

Set your NewsAPI key in a .env file:

```bash
SECRET_KEY=your_newsapi_key
```

Run the script:

```bash
python main.py
```

The script will fetch the top 20 news articles related to Python programming and send them to the specified email address.

## Dependencies

- Python 3.6+
- requests
- python-dotenv
- send_email (local module)

## License

This project is licensed under the terms of the MIT license.
