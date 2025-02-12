""" Alert Rule  DAL"""

"""_summary_
this file is to right any ORM logic for the Alert Rule model
"""
from resources.alert_rules.alert_rule_schema import AlertRuleCreate, AlertRuleUpdate
from db.models.models import AlertRule
from sqlalchemy.orm import Session


def create_alert_rule(rule: AlertRuleCreate, session: Session) -> AlertRule:
    new_rule = AlertRule(**rule.model_dump(exclude_unset=True))
    session.add(new_rule)
    session.commit()
    session.refresh(new_rule)
    return new_rule


def update_alert_rule(
    rule_id: int, rule: AlertRuleUpdate, session: Session
) -> AlertRule:
    updated_rule_query = session.query(AlertRule).filter(AlertRule.id == rule_id)
    updated_rule = updated_rule_query.first()
    updated_rule_query.update(rule.model_dump(exclude_unset=True))
    session.commit()
    session.refresh(updated_rule)
    return updated_rule


def get_alert_rules(session: Session) -> list[AlertRule]:
    return session.query(AlertRule).all()


def get_alert_rule(rule_id: int, session: Session) -> AlertRule:
    return session.query(AlertRule).filter(AlertRule.id == rule_id).first()


def delete_alert_rule(rule_id: int, session: Session) -> AlertRule | None:
    rule = session.query(AlertRule).filter_by(id=rule_id).first()
    if rule:
        session.delete(rule)
        session.commit()
        return rule
    return None
