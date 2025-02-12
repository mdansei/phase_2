"""Seed alerts table

Revision ID: dd7d187ce8d1
Revises: add_created_at_column
Create Date: 2025-02-10 08:16:30.750770

"""

from typing import Sequence, Union

from alembic import op
from sqlalchemy.sql import text

# revision identifiers, used by Alembic.
revision: str = "dd7d187ce8d1"
down_revision: Union[str, None] = "add_created_at_column"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute(
        text(
            "INSERT INTO alert_rules (id, name, threshold_price, symbol) VALUES (1, 'Sample Rule', 150, 'AAPL')"
        )
    )

    op.execute(
        text(
            """
            INSERT INTO alerts (rule_id, triggered_price, reason) VALUES
            (1, 155.0, 'Price of AAPL exceeded threshold of $150'),
            (1, 160.0, 'Price of AAPL exceeded threshold of $150'),
            (1, 150.5, 'Price of AAPL exceeded threshold of $150'),
            (1, 145.0, 'Price of AAPL fell below threshold of $150'),
            (1, 140.0, 'Price of AAPL fell below threshold of $150'),
            (1, 149.0, 'Price of AAPL fell below threshold of $150')
        """
        )
    )


def downgrade() -> None:
    pass
