"""add_password_column_user_table

Revision ID: ff8f14ba0f38
Revises: 11e01a3ad2b5
Create Date: 2023-01-01 18:57:42.063677

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy import LargeBinary


# revision identifiers, used by Alembic.
revision = 'ff8f14ba0f38'
down_revision = '11e01a3ad2b5'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('user', sa.Column('password', LargeBinary, nullable=False))


def downgrade() -> None:
    op.drop_column('user', 'password')
