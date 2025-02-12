""" Alert Rule Schema """

"""_summary_
This file to abstract any validation logic for the Alert Rules
"""
from pydantic import BaseModel, Field, ConfigDict, model_validator
from db.enums import StockSymbol


class AlertRuleBase(BaseModel):
    name: str = Field(..., description="Name of the alert rule")
    threshold_price: float = Field(
        ..., gt=0, description="Price threshold that triggers the alert"
    )
    symbol: StockSymbol = Field(..., description="Stock symbol to monitor")


class AlertRuleCreate(AlertRuleBase):
    pass


class AlertRuleUpdate(BaseModel):
    name: str | None = Field(None, description="Name of the alert rule")
    threshold_price: float | None = Field(
        None, gt=0, description="Price threshold that triggers the alert"
    )
    symbol: StockSymbol | None = Field(None, description="Stock symbol to monitor")

    @model_validator(mode="before")
    def check_at_least_one_key(cls, values):
        required_fields = cls.__annotations__.keys()
        if not any(values.get(field) is not None for field in required_fields):
            raise ValueError(
                f'At least one of {", ".join(required_fields)} must be provided'
            )
        return values


class AlertRuleResponse(AlertRuleBase):
    id: int

    model_config = ConfigDict(
        from_attributes=True,
        json_encoders={int: str},  # Ensure large integers are serialized as strings
    )
