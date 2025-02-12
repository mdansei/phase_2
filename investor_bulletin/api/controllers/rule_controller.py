"""Alert Rules Controller"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from db.config import get_db
from resources.alert_rules.alert_rule_schema import (
    AlertRuleCreate,
    AlertRuleUpdate,
    AlertRuleResponse,
)
import resources.alert_rules.alert_rule_service as AlertRuleService

router = APIRouter()


@router.post("/", response_model=AlertRuleResponse)
def create_alert_rule(alert_rule: AlertRuleCreate, db: Session = Depends(get_db)):
    """Create a new alert rule"""
    rule = AlertRuleService.create_alert_rule(alert_rule, db)
    return rule


@router.get("/", response_model=list[AlertRuleResponse])
def get_alert_rules(db: Session = Depends(get_db)):
    """Get all alert rules"""
    return AlertRuleService.get_alert_rules(db)


@router.get("/{rule_id}", response_model=AlertRuleResponse)
def get_alert_rule(rule_id: int, db: Session = Depends(get_db)):
    """Get a specific alert rule by ID"""
    rule = AlertRuleService.get_alert_rule(rule_id, db)
    if not rule:
        raise HTTPException(status_code=404, detail="Alert rule not found")
    return rule


@router.patch("/{rule_id}", response_model=AlertRuleResponse)
def update_alert_rule(
    rule_id: int, alert_rule: AlertRuleUpdate, db: Session = Depends(get_db)
):
    """Update an alert rule"""
    updated_rule = AlertRuleService.update_alert_rule(
        rule_id=rule_id, rule=alert_rule, session=db
    )
    if not updated_rule:
        raise HTTPException(status_code=404, detail="Alert rule not found")
    return updated_rule


@router.delete("/{rule_id}")
def delete_alert_rule(rule_id: int, db: Session = Depends(get_db)) -> dict:
    """Delete an alert rule"""
    rule = AlertRuleService.delete_alert_rule(rule_id, db)
    if not rule:
        raise HTTPException(status_code=404, detail="Alert rule not found")
    return {"message": "Alert rule deleted successfully"}
