"""Add created_at timestamp to alerts

Revision ID: add_created_at_column
Revises: 9a365fd87641
Create Date: 2024-02-11 11:00:00.000000

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import func


# revision identifiers, used by Alembic.
revision: str = 'add_created_at_column'
down_revision: Union[str, None] = '9a365fd87641'  # Point to initial migration
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Add created_at column with current timestamp as default
    op.add_column('alerts', sa.Column('created_at', sa.DateTime(timezone=True), nullable=False,
                    server_default=sa.text('CURRENT_TIMESTAMP')))


def downgrade() -> None:
    op.drop_column('alerts', 'created_at') 