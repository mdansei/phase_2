"""Seed alert rules table

Revision ID: seed_alert_rules
Revises: dd7d187ce8d1
Create Date: 2024-02-12 15:30:00.000000

"""
from typing import Sequence, Union
from alembic import op
from sqlalchemy.sql import text

# revision identifiers, used by Alembic.
revision: str = 'seed_alert_rules'
down_revision: Union[str, None] = 'dd7d187ce8d1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade() -> None:
    # Insert alert rules for each stock with meaningful thresholds
    op.execute(
        text(
            """
            INSERT INTO alert_rules (name, threshold_price, symbol) VALUES
            ('AAPL High Alert', 180.00, 'AAPL'),
            ('AAPL Low Alert', 170.00, 'AAPL'),
            ('MSFT High Alert', 340.00, 'MSFT'),
            ('MSFT Low Alert', 320.00, 'MSFT'),
            ('GOOG High Alert', 140.00, 'GOOG'),
            ('GOOG Low Alert', 130.00, 'GOOG'),
            ('AMZN High Alert', 150.00, 'AMZN'),
            ('AMZN Low Alert', 140.00, 'AMZN'),
            ('META High Alert', 280.00, 'META'),
            ('META Low Alert', 260.00, 'META')
            """
        )
    )

def downgrade() -> None:
    # Remove all seeded alert rules
    op.execute(text("DELETE FROM alert_rules")) 