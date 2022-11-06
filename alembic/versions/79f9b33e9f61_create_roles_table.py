"""create roles table

Revision ID: 79f9b33e9f61
Revises: 
Create Date: 2022-11-05 19:42:34.337579

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy import Integer, String


# revision identifiers, used by Alembic.
revision = '79f9b33e9f61'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'roles',
        sa.Column('id', Integer, primary_key=True, unique=True, nullable=False, autoincrement=True),
        sa.Column('role_name', String(50), nullable=False, unique=True)
    )


def downgrade() -> None:
    op.drop_table('roles')
