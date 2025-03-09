from sqlalchemy.orm import Session
from typing import List, Optional
from app.models import Racket

def get_rackets(
    db: Session,
    power_gt: Optional[int] = None,
    power_lt: Optional[int] = None,
    power_eq: Optional[int] = None,
    control_gt: Optional[int] = None,
    control_lt: Optional[int] = None,
    control_eq: Optional[int] = None,
    overall_rating_gt: Optional[int] = None,
    overall_rating_lt: Optional[int] = None,
    overall_rating_eq: Optional[int] = None,
) -> List[Racket]:
    """Fetch rackets based on filter criteria."""
    query = db.query(Racket)

    if power_gt:
        query = query.filter(Racket.power > power_gt)
    if power_lt:
        query = query.filter(Racket.power < power_lt)
    if power_eq:
        query = query.filter(Racket.power == power_eq)

    if control_gt:
        query = query.filter(Racket.control > control_gt)
    if control_lt:
        query = query.filter(Racket.control < control_lt)
    if control_eq:
        query = query.filter(Racket.control == control_eq)

    if overall_rating_gt:
        query = query.filter(Racket.overall_rating > overall_rating_gt)
    if overall_rating_lt:
        query = query.filter(Racket.overall_rating < overall_rating_lt)
    if overall_rating_eq:
        query = query.filter(Racket.overall_rating == overall_rating_eq)

    return query.all()
