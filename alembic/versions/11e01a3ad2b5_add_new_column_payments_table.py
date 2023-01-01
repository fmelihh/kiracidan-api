"""add new column payments table

Revision ID: 11e01a3ad2b5
Revises: 7a15424d9c7c
Create Date: 2022-11-06 18:00:07.646131

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy import Integer, ForeignKey

# revision identifiers, used by Alembic.
revision = '11e01a3ad2b5'
down_revision = '7a15424d9c7c'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('payments', sa.Column('user_id', Integer, ForeignKey("user_service.id"), nullable=False))


def downgrade() -> None:
    op.drop_column('payments', 'user_id')
