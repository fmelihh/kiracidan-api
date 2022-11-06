"""insert default roles into role table

Revision ID: f22e322b8bb6
Revises: e7b4f55ddcfb
Create Date: 2022-11-06 15:46:37.830337

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f22e322b8bb6'
down_revision = 'e7b4f55ddcfb'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute("""INSERT INTO roles (role_name) SELECT * FROM unnest(array['TENANT', 'HOMEOWNER']) """)


def downgrade() -> None:
    op.execute("""DELETE FROM roles WHERE role_name IN('TENANT', 'HOMEOWNER')""")
