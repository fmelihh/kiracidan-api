"""create users table

Revision ID: d0e28d45d8e4
Revises: 79f9b33e9f61
Create Date: 2022-11-05 20:04:09.178865

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy import Column, Integer, String, ForeignKey


# revision identifiers, used by Alembic.
revision = 'd0e28d45d8e4'
down_revision = '79f9b33e9f61'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'user',
        sa.Column('id', Integer, primary_key=True, unique=True, nullable=False, autoincrement=True),
        sa.Column('name', String(100), nullable=False),
        sa.Column('family_name', String(100), nullable=False),
        sa.Column('email', String(50), nullable=False),
        sa.Column('phone_number', String(15), nullable=False),
        sa.Column('role_id', Integer, ForeignKey("roles.id"), unique=True),
    )


def downgrade() -> None:
    op.drop_table('user_service')