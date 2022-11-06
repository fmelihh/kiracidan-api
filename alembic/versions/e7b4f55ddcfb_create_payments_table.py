"""create payments table

Revision ID: e7b4f55ddcfb
Revises: a8b4cf6c8dc9
Create Date: 2022-11-06 15:27:49.506715

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy import Integer, ForeignKey, DateTime, Float
from sqlalchemy.sql import func

# revision identifiers, used by Alembic.
revision = 'e7b4f55ddcfb'
down_revision = 'a8b4cf6c8dc9'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'payments',
        sa.Column('id', Integer, primary_key=True, nullable=False, unique=True, autoincrement=True),
        sa.Column('target_home_id', Integer, ForeignKey("home.id"), nullable=False),
        sa.Column('type', Integer, ForeignKey("payment_types.id"), nullable=False),
        sa.Column('date', DateTime(timezone=True), server_default=func.now(), nullable=False),

        sa.Column('amount', Float, nullable=False),
    )


def downgrade() -> None:
    op.drop_table('payments')
