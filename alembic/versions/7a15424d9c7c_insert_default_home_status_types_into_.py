"""insert default home status types into the home status table

Revision ID: 7a15424d9c7c
Revises: f9231b8d71bd
Create Date: 2022-11-06 16:05:17.438139

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7a15424d9c7c'
down_revision = 'f9231b8d71bd'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute("INSERT INTO home_status (status_name) SELECT * FROM unnest(array['ON_SALE', 'PENDING', 'RENT']) ")


def downgrade() -> None:
    op.execute("""DELETE FROM home_status WHERE status_name IN('ON_SALE', 'PENDING', 'RENT')""")
