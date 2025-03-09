from pydantic import BaseModel
from typing import Optional

class RacketCreate(BaseModel):
    name: str
    overall_rating: Optional[int] = None
    power: Optional[int] = None
    control: Optional[int] = None
    rebound: Optional[int] = None
    maneuverability: Optional[int] = None
    sweet_spot: Optional[int] = None
