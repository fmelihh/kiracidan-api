"""create comments table

Revision ID: 75595f9a009d
Revises: d0e28d45d8e4
Create Date: 2022-11-05 20:09:37.108052

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy import Column, Integer, String, ForeignKey


# revision identifiers, used by Alembic.
revision = '75595f9a009d'
down_revision = 'd0e28d45d8e4'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'comments',
        sa.Column('id', Integer, primary_key=True, unique=True, nullable=False, autoincrement=True),
        sa.Column('user_who_commented_id', Integer, ForeignKey("user_service.id")),
        sa.Column('commented_user_id', Integer, ForeignKey("user_service.id")),
        sa.Column('rating', Integer, nullable=False),
        sa.Column('user_comment', String(1000), nullable=True),
    )


def downgrade() -> None:
    op.drop_table('comments')
