"""create home table

Revision ID: a8b4cf6c8dc9
Revises: d20d0230ca8d
Create Date: 2022-11-06 15:23:36.156044

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy import Integer, String, ForeignKey


# revision identifiers, used by Alembic.
revision = 'a8b4cf6c8dc9'
down_revision = 'd20d0230ca8d'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'home',
        sa.Column('id', Integer, primary_key=True, unique=True, autoincrement=True),
        sa.Column('title', String(500), nullable=False),
        sa.Column('comment', String(), nullable=True),
        sa.Column('address', String(), nullable=False),
        sa.Column('status_id', Integer, ForeignKey("home_status.id"), nullable=False),
        sa.Column('owner_id', Integer, ForeignKey("user.id"), nullable=False),
        sa.Column('tenant_id', Integer, ForeignKey("user.id"), unique=True, nullable=True),
        sa.Column('payment_amount', Integer, nullable=False),
        sa.Column('deposit', Integer, nullable=True),
        sa.Column('payment_period', Integer, nullable=True),
    )


def downgrade() -> None:
    op.drop_table('home')
