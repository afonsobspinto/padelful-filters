from sqlalchemy.orm import Session
from sqlalchemy import desc
from typing import List, Optional
from app.models import Racket

def get_rackets(
    db: Session,
    power_gt: Optional[int] = None, power_lt: Optional[int] = None, power_eq: Optional[int] = None,
    control_gt: Optional[int] = None, control_lt: Optional[int] = None, control_eq: Optional[int] = None,
    rebound_gt: Optional[int] = None, rebound_lt: Optional[int] = None, rebound_eq: Optional[int] = None,
    maneuverability_gt: Optional[int] = None, maneuverability_lt: Optional[int] = None, maneuverability_eq: Optional[int] = None,
    sweet_spot_gt: Optional[int] = None, sweet_spot_lt: Optional[int] = None, sweet_spot_eq: Optional[int] = None,
    overall_rating_gt: Optional[int] = None, overall_rating_lt: Optional[int] = None, overall_rating_eq: Optional[int] = None,
    sort_by: Optional[str] = None,
    order: Optional[str] = "asc",
) -> List[Racket]:
    """Fetch rackets based on filter criteria with sorting support."""
    query = db.query(Racket)

    # ✅ Define filter mapping
    filters = {
        "power": [power_gt, power_lt, power_eq],
        "control": [control_gt, control_lt, control_eq],
        "rebound": [rebound_gt, rebound_lt, rebound_eq],
        "maneuverability": [maneuverability_gt, maneuverability_lt, maneuverability_eq],
        "sweet_spot": [sweet_spot_gt, sweet_spot_lt, sweet_spot_eq],
        "overall_rating": [overall_rating_gt, overall_rating_lt, overall_rating_eq],
    }

    # ✅ Apply filters dynamically
    filter_operators = [">", "<", "=="]
    for attr, values in filters.items():
        for op, value in zip(filter_operators, values):
            if value is not None:
                query = query.filter(getattr(Racket, attr).op(op)(value))

    # ✅ Apply sorting if a valid column is provided
    valid_sort_columns = ["power", "control", "rebound", "maneuverability", "sweet_spot", "overall_rating"]
    if sort_by in valid_sort_columns:
        if order == "desc":
            query = query.order_by(desc(getattr(Racket, sort_by)))
        else:
            query = query.order_by(getattr(Racket, sort_by))

    return query.all()
