from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from typing import List, Optional

from app.database import get_db
from app.crud import get_rackets
from app.schemas import RacketBase

router = APIRouter(prefix="/rackets", tags=["Rackets"])

@router.get("/", response_model=List[RacketBase])
def list_rackets(
    db: Session = Depends(get_db),
    power_gt: Optional[int] = Query(None, description="Power greater than"),
    power_lt: Optional[int] = Query(None, description="Power less than"),
    power_eq: Optional[int] = Query(None, description="Power equal to"),
    control_gt: Optional[int] = Query(None),
    control_lt: Optional[int] = Query(None),
    control_eq: Optional[int] = Query(None),
    overall_rating_gt: Optional[int] = Query(None),
    overall_rating_lt: Optional[int] = Query(None),
    overall_rating_eq: Optional[int] = Query(None),
):
    return get_rackets(
        db,
        power_gt,
        power_lt,
        power_eq,
        control_gt,
        control_lt,
        control_eq,
        overall_rating_gt,
        overall_rating_lt,
        overall_rating_eq
    )