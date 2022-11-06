"""create payment types table

Revision ID: d20d0230ca8d
Revises: fb62a05535ae
Create Date: 2022-11-06 15:21:17.214153

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy import Integer, String


# revision identifiers, used by Alembic.
revision = 'd20d0230ca8d'
down_revision = 'fb62a05535ae'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'payment_types',
        sa.Column('id', Integer, primary_key=True, unique=True, nullable=False, autoincrement=True),
        sa.Column('payment_type', String(50), nullable=False, unique=True),
    )


def downgrade() -> None:
    op.drop_table('payment_types')
