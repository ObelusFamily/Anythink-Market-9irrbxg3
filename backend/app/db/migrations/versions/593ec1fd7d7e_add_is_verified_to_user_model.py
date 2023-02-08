"""add is_verified to user model

Revision ID: 593ec1fd7d7e
Revises: fdf8821871d7
Create Date: 2023-02-08 15:53:49.735386

"""
from alembic import op
import sqlalchemy as sa


revision = '593ec1fd7d7e'
down_revision = 'fdf8821871d7'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('users', sa.Column("is_verified", sa.Boolean, nullable=False, server_default=sa.text("false"), index=True))


def downgrade() -> None:
    op.drop_column("users", "is_verified")
