""" Alert Service"""
"""_summary_
this file to write any business logic for the alerts
"""
import resources.alerts.alert_dal as AlertDal
from resources.alerts.alert_schema import AlertCreate

def get_alerts(session):
    return AlertDal.get_alerts(session)

def create_alert(alert: AlertCreate, session):
    return AlertDal.create_alert(**alert.model_dump(exclude_unset=True), session=session)

def should_create_alert(current_price: float, threshold: float, last_price: float | None) -> tuple[bool, bool]:
    """
    Determine if we should create an alert by comparing positions relative to threshold.
    Returns (should_create, is_above) where:
    - should_create: True if we should create an alert
    - is_above: True if current price is above threshold
    """
    currently_above = current_price > threshold
    
    if last_price is None:
        return True, currently_above  # First alert for this rule
        
    was_above = last_price > threshold
    return currently_above != was_above, currently_above

def process_market_data(market_data: dict, session) -> list[AlertCreate]:
    """
    Process market data and create alerts for any threshold crossovers.
    """
    symbol = market_data['symbol']
    current_price = float(market_data['price'])
    created_alerts = []
    
    
    rules_with_last_alert_prices = AlertDal.get_rules_with_last_alert_price(session, symbol)
    
    for rule, last_alert_price in rules_with_last_alert_prices:
        threshold = rule.threshold_price
        should_alert, is_above = should_create_alert(current_price, threshold, last_alert_price)
        
        if should_alert:
            reason = f"Price of {symbol} crossed {'above' if is_above else 'below'} threshold of ${threshold}"
            alert = AlertCreate(
                rule_id=rule.id,
                triggered_price=current_price,
                reason=reason
            )
            created_alert = create_alert(alert, session)
            print(f"Created alert reason: {reason}")
            
            created_alerts.append(created_alert)
    
    return created_alerts
