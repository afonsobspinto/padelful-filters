from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from typing import List, Optional
from app.crud import get_rackets
from app.database import get_db
from app.schemas import RacketBase

router = APIRouter()

@router.get("/rackets/", response_model=List[RacketBase])
def list_rackets(
    db: Session = Depends(get_db),
    power_gt: Optional[int] = Query(None), power_lt: Optional[int] = Query(None), power_eq: Optional[int] = Query(None),
    control_gt: Optional[int] = Query(None), control_lt: Optional[int] = Query(None), control_eq: Optional[int] = Query(None),
    rebound_gt: Optional[int] = Query(None), rebound_lt: Optional[int] = Query(None), rebound_eq: Optional[int] = Query(None),
    maneuverability_gt: Optional[int] = Query(None), maneuverability_lt: Optional[int] = Query(None), maneuverability_eq: Optional[int] = Query(None),
    sweet_spot_gt: Optional[int] = Query(None), sweet_spot_lt: Optional[int] = Query(None), sweet_spot_eq: Optional[int] = Query(None),
    overall_rating_gt: Optional[int] = Query(None), overall_rating_lt: Optional[int] = Query(None), overall_rating_eq: Optional[int] = Query(None),
    sort_by: Optional[str] = Query(None, description="Sort by: power, control, rebound, maneuverability, sweet_spot, overall_rating"),
    order: Optional[str] = Query("asc", description="Sort order: 'asc' or 'desc'"),
):
    return get_rackets(
        db,
        power_gt, power_lt, power_eq,
        control_gt, control_lt, control_eq,
        rebound_gt, rebound_lt, rebound_eq,
        maneuverability_gt, maneuverability_lt, maneuverability_eq,
        sweet_spot_gt, sweet_spot_lt, sweet_spot_eq,
        overall_rating_gt, overall_rating_lt, overall_rating_eq,
        sort_by, order
    )
