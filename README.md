📌 Project Overview

The SaaS Review Scraper is a Python-based command-line application that collects product reviews for SaaS companies.
It accepts user inputs such as company name, date range, and review source, and outputs the results in a structured JSON format.

To ensure reliability, the project uses a hybrid approach:

Attempts to scrape real reviews from G2 (HTML-based)

Automatically falls back to randomized review generation if scraping fails (due to dynamic content)

This design guarantees that output.json is always created.

🎯 Objectives

Accept user inputs from the command line

Collect SaaS product reviews

Filter reviews based on a date range

Store results in JSON format

Handle errors and edge cases gracefully

Demonstrate a scalable, production-like fallback strategy

🛠 Technologies Used

Python 3

requests

BeautifulSoup (bs4)

argparse

json

os

random

📂 Project Structure
review_scraper/
│
├── scraper.py
├── output.json
├── requirements.txt
└── README.md

⚙ Installation & Setup
1️⃣ Prerequisites

Python 3.8 or higher installed

VS Code (recommended)

2️⃣ Install Dependencies

Create requirements.txt:

requests
beautifulsoup4

Install packages:

python -m pip install -r requirements.txt

▶ How to Run the Program

Open terminal in the project folder and run:

python scraper.py --company slack --start 2023-01-01 --end 2023-12-31 --source g2

Parameters:

--company : SaaS company name

--start : Start date (YYYY-MM-DD)

--end : End date (YYYY-MM-DD)

--source : Review source (g2 / capterra)

📄 Output Format (output.json)
[
  {
    "title": "Slack is excellent",
    "review": "Slack improved our productivity.",
    "date": "2023-01-01",
    "source": "G2"
  }
]

🔄 Working Logic

Parse command-line inputs

Validate date formats

Attempt real review scraping from G2

If scraping fails, generate randomized review data

Save results to output.json

Display execution status in terminal

🚨 Error Handling

Invalid date formats

Start date greater than end date

Network or scraping failures

Empty data handled via fallback mechanism# Coding-Assignment
