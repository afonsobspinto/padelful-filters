from pydantic import BaseModel
from typing import Optional

class RacketBase(BaseModel):
    name: str
    brand: Optional[str] = None
    year: Optional[int] = None
    power: Optional[int] = None
    control: Optional[int] = None
    rebound: Optional[int] = None
    maneuverability: Optional[int] = None
    sweet_spot: Optional[int] = None
    overall_rating: Optional[int] = None
    original_price: Optional[int] = None
    current_price: Optional[int] = None