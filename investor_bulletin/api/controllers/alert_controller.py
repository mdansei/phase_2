"""Alert Controller"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from db.config import get_db
from resources.alerts.alert_schema import AlertResponse
import resources.alerts.alert_service as AlertService

router = APIRouter()


@router.get("/", response_model=list[AlertResponse])
def get_alerts(db: Session = Depends(get_db)):
    """Get all alerts"""
    return AlertService.get_alerts(db)
