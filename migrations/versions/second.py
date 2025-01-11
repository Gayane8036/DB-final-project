"""Added index on price column in Artwork

Revision ID: def456ghi789
Revises: abc123xyz456
Create Date: 2025-01-11 13:37:01.698290
"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

revision: str = 'def456ghi789'
down_revision: str = 'abc123xyz456'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_index('ix_artwork_price', 'artworks', ['price'])


def downgrade() -> None:
    op.drop_index('ix_artwork_price', table_name='artworks')
