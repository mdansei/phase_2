from api.controllers.market_controller import router as MarketRouter
from api.controllers.rule_controller import router as RuleRouter
from api.controllers.alert_controller import router as AlertRouter


def init_routes(app):
    app.include_router(MarketRouter, prefix="/market-prices", tags=["Market"])
    app.include_router(RuleRouter, prefix="/rules", tags=["Rules"])
    app.include_router(AlertRouter, prefix="/alerts", tags=["Alerts"])
    return app
