"""create home status table

Revision ID: fb62a05535ae
Revises: 75595f9a009d
Create Date: 2022-11-06 15:19:04.413775

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy import Integer, String


# revision identifiers, used by Alembic.
revision = 'fb62a05535ae'
down_revision = '75595f9a009d'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'home_status',
        sa.Column('id', Integer, primary_key=True, nullable=False, unique=True, autoincrement=True),
        sa.Column('status_name', String(), unique=True)
    )


def downgrade() -> None:
    op.drop_table('home_status')
