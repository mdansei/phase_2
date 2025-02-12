""" Alert Rule Service"""

"""_summary_
this file to write any business logic for the Alert Rules
"""
from resources.alert_rules.alert_rule_schema import AlertRuleCreate, AlertRuleUpdate
import resources.alert_rules.alert_rule_dal as AlertRuleDal
from sqlalchemy.orm import Session


def create_alert_rule(rule: AlertRuleCreate, session: Session):
    return AlertRuleDal.create_alert_rule(rule=rule, session=session)


def get_alert_rules(session: Session):
    return AlertRuleDal.get_alert_rules(session=session)


def get_alert_rule(rule_id: int, session: Session):
    return AlertRuleDal.get_alert_rule(rule_id=rule_id, session=session)


def update_alert_rule(rule_id: int, rule: AlertRuleUpdate, session: Session):
    return AlertRuleDal.update_alert_rule(rule_id=rule_id, rule=rule, session=session)


def delete_alert_rule(rule_id: int, session: Session):
    return AlertRuleDal.delete_alert_rule(rule_id=rule_id, session=session)
