import requests
import json
import time
from bs4 import BeautifulSoup
from tqdm import tqdm

BASE_URL = "https://www.padelful.com/en/rackets?page="
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

def scrape_page(page_number):
    """Scrapes a single page and extracts padel racket details."""
    url = f"{BASE_URL}{page_number}"
    response = requests.get(url, headers=HEADERS)
    
    if response.status_code != 200:
        print(f"⚠️ Failed to retrieve page {page_number}")
        return []

    soup = BeautifulSoup(response.text, "html.parser")
    rackets_data = []

    # Find the main div container with class 'grid'
    grid_container = soup.find("div", class_="grid")

    if not grid_container:
        print(f"⚠️ No rackets found on page {page_number}")
        return []

    # Find all divs that contain "relative" (even if they have other classes)
    all_relative_divs = grid_container.find_all("div", class_="relative", recursive=True)

    # Filter to keep only divs where class == ["relative"]
    racket_containers = [div for div in all_relative_divs if div.get("class") == ["relative"]]

    for racket in racket_containers:
        try:
            name_tag = racket.find("h3")
            name = name_tag.text.strip() if name_tag else "Unknown"

            brand_year_tag = racket.find("p", class_="relative font-mono text-sm font-semibold text-white md:text-base")
            brand, year = brand_year_tag.text.strip().split(" / ") if brand_year_tag else ("Unknown", "Unknown")

            # ✅ Extract scores
            scores = racket.find_all("span", class_="text-sm font-bold leading-none text-white sm:text-base")
            scores_list = [int(score.text) for score in scores]

            if len(scores_list) < 5:
                power, control, rebound, maneuverability, sweet_spot = (None, None, None, None, None)
            else:
                power, control, rebound, maneuverability, sweet_spot = scores_list[:5]

            # ✅ Extract rating
            rating_tag = racket.find("span", class_="absolute left-2 top-2 rounded-md px-2 py-1 text-4xl font-bold text-green-800")
            overall_rating = int(rating_tag.text.strip()) if rating_tag else None

            # ✅ Extract price
            price_tag = racket.find("span", class_="absolute left-2 top-14 rounded-md bg-transparent px-2 text-lg font-semibold text-neutral-700")
            price = price_tag.text.strip().replace("€", "") if price_tag else "Unknown"

            # ✅ Store data
            rackets_data.append({
                "name": name,
                "brand": brand,
                "year": year,
                "power": power,
                "control": control,
                "rebound": rebound,
                "maneuverability": maneuverability,
                "sweet_spot": sweet_spot,
                "overall_rating": overall_rating,
                "price": price
            })

        except Exception as e:
            print(f"⚠️ Skipping a racket due to error: {e}")

    return rackets_data

def scrape_all_pages():
    """Scrapes multiple pages and saves results in a JSON file with progress bar."""
    all_rackets = []
    page = 1

    with tqdm(desc="Scraping pages", unit="page") as pbar:  # ✅ Add progress bar
        while True:
            rackets = scrape_page(page)
            if not rackets:
                break  # ✅ Stop if no more rackets found
            
            all_rackets.extend(rackets)
            page += 1
            pbar.update(1)  # ✅ Update tqdm progress bar
            time.sleep(1)  # ✅ Avoid sending too many requests

    # ✅ Save results to JSON file
    with open("rackets.json", "w", encoding="utf-8") as file:
        json.dump(all_rackets, file, indent=4, ensure_ascii=False)
    
    print(f"✅ Scraped {len(all_rackets)} rackets and saved to 'rackets.json'")

if __name__ == "__main__":
    scrape_all_pages()
