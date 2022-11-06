"""insert default payment types into the payment types table

Revision ID: f9231b8d71bd
Revises: f22e322b8bb6
Create Date: 2022-11-06 15:58:18.763905

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f9231b8d71bd'
down_revision = 'f22e322b8bb6'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute("""
    INSERT INTO payment_types (payment_type) 
    SELECT * FROM unnest(array['RENT', 'DEPOSIT'])
    """)


def downgrade() -> None:
    op.execute("""DELETE FROM payment_types WHERE payment_type IN('RENT', 'DEPOSIT')""")
