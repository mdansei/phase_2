""" Alert Schema """

"""_summary_
This file to abstract any validation logic for the Alerts
"""
from pydantic import BaseModel, ConfigDict


class AlertResponse(BaseModel):
    id: int
    triggered_price: float
    reason: str

    model_config = ConfigDict(from_attributes=True, json_encoders={int: str})

class AlertCreate(BaseModel):
    rule_id: int
    triggered_price: float
    reason: str
