""" Alert DAL"""

"""_summary_
this file is to right any ORM logic for the Alert model
"""
from sqlalchemy import desc
from db.models.models import Alert, AlertRule


def get_alerts(session):
    """Get all alerts ordered by creation time."""
    return session.query(Alert).order_by(desc(Alert.created_at)).all()

def get_rules_with_last_alert_price(session, symbol: str) -> list[tuple[AlertRule, float | None]]:
    """
    Get all rules for a symbol along with their most recent alert's triggered price.
    Returns a list of tuples (rule, triggered_price) where triggered_price may be None.
    """
    # Subquery to get the most recent alert for each rule using timestamp
    last_alerts = (
        session.query(
            Alert.rule_id,
            Alert.triggered_price,
            Alert.created_at
        )
        .order_by(Alert.rule_id, desc(Alert.created_at))
        .distinct(Alert.rule_id)
        .subquery()
    )

    # Get rules and join with their last alert (if any)
    return (
        session.query(
            AlertRule,
            last_alerts.c.triggered_price
        )
        .outerjoin(last_alerts, AlertRule.id == last_alerts.c.rule_id)
        .filter(AlertRule.symbol == symbol)
        .all()
    )

def create_alert(session, rule_id: int, triggered_price: float, reason: str):
    new_alert = Alert(
        rule_id=rule_id,
        triggered_price=triggered_price,
        reason=reason
    )
    session.add(new_alert)
    session.commit()
    return new_alert
