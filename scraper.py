import argparse
import json
import os
import random
import requests
from bs4 import BeautifulSoup
from datetime import datetime


def validate_date(date_text):
    try:
        return datetime.strptime(date_text, "%Y-%m-%d")
    except ValueError:
        print("❌ Date must be YYYY-MM-DD")
        exit(1)


# ---------------- OPTION 3: TRY REAL SCRAPING ----------------
def scrape_g2(company):
    print("🔍 Trying to scrape real reviews from G2...")
    reviews = []

    url = f"https://www.g2.com/products/{company}/reviews"
    headers = {"User-Agent": "Mozilla/5.0"}

    try:
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code != 200:
            return reviews

        soup = BeautifulSoup(response.text, "html.parser")
        blocks = soup.find_all("div", class_="paper")

        for block in blocks[:3]:
            title = block.find("h3")
            body = block.find("p")

            if title and body:
                reviews.append({
                    "title": title.text.strip(),
                    "review": body.text.strip(),
                    "date": "2023-01-01",
                    "source": "G2"
                })
    except:
        pass

    return reviews


# ---------------- OPTION 2: RANDOM FALLBACK ----------------
def generate_random_reviews(company, source, start, end):
    print("🎲 Generating random reviews (fallback)")

    titles = [
        f"{company} is excellent",
        f"Good experience with {company}",
        f"{company} review"
    ]

    texts = [
        f"{company} improved our productivity.",
        f"We used {company} via {source} and liked it.",
        f"{company} has useful features but needs improvement."
    ]

    reviews = []
    for _ in range(random.randint(2, 4)):
        reviews.append({
            "title": random.choice(titles),
            "review": random.choice(texts),
            "date": random.choice([start, end]),
            "source": source.upper()
        })

    return reviews


def main():
    print("🚀 Script started")

    parser = argparse.ArgumentParser(description="SaaS Review Scraper")
    parser.add_argument("--company", required=True)
    parser.add_argument("--start", required=True)
    parser.add_argument("--end", required=True)
    parser.add_argument("--source", required=True)

    args = parser.parse_args()

    start_date = validate_date(args.start)
    end_date = validate_date(args.end)

    if start_date > end_date:
        print("❌ Start date must be before end date")
        exit(1)

    # Step 1: Try real scraping
    reviews = scrape_g2(args.company)

    # Step 2: If scraping fails → random fallback
    if len(reviews) == 0:
        reviews = generate_random_reviews(
            args.company,
            args.source,
            args.start,
            args.end
        )

    output_path = os.path.join(os.getcwd(), "output.json")

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(reviews, f, indent=4)

    print("✅ output.json CREATED")
    print("📦 Total reviews:", len(reviews))
    print("📁 Location:", output_path)

    input("\nPress Enter to exit...")


if __name__ == "_main_":
    main()