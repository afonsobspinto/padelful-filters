import json
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import Racket
import re

def seed_database_from_json():
    db: Session = SessionLocal()

    with open("rackets.json", "r") as file:
        data = json.load(file)

    for item in data:
        # ✅ Extract and clean prices
        original_price, current_price = extract_prices(item.get("price", "0"))

        # ✅ Prepare data, keeping only valid fields
        filtered_item = {
            "name": item["name"],
            "brand": item.get("brand"),
            "year": item.get("year"),
            "power": item.get("power"),
            "control": item.get("control"),
            "rebound": item.get("rebound"),
            "maneuverability": item.get("maneuverability"),
            "sweet_spot": item.get("sweet_spot"),
            "overall_rating": item.get("overall_rating"),
            "original_price": original_price,
            "current_price": current_price
        }

        racket = Racket(**filtered_item)
        db.add(racket)

    db.commit()
    db.close()
    print("✅ JSON Data Loaded Successfully!")


def extract_prices(price_str):
    """Extracts original and current prices from a price string."""
    try:
        # Find all numbers in the price string
        prices = [int(p) for p in re.findall(r"\d+", price_str)]
        
        if len(prices) == 2:
            return prices[0], prices[1]  # (original_price, current_price)
        elif len(prices) == 1:
            return prices[0], prices[0]  # Same price for both
        else:
            return None, None
    except Exception:
        return None, None


if __name__ == "__main__":
    seed_database_from_json()
