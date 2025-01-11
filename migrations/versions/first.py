"""Added email and description columns

Revision ID: abc123xyz456
Revises: None
Create Date: 2025-01-11 13:00:01.698290
"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

revision: str = 'abc123xyz456'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('creators', sa.Column('email', sa.String(), nullable=True))

    op.add_column('storage_places', sa.Column('description', sa.String(), nullable=True))


def downgrade() -> None:
    op.drop_column('creators', 'email')

    op.drop_column('storage_places', 'description')
