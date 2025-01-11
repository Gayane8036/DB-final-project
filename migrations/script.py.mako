"""Add new columns and indexes to tables

Revision ID: ${up_revision}
Revises: ${down_revision | comma,n}
Create Date: ${create_date}
"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = ${repr(up_revision)}
down_revision: Union[str, None] = ${repr(down_revision)}
branch_labels: Union[str, Sequence[str], None] = ${repr(branch_labels)}
depends_on: Union[str, Sequence[str], None] = ${repr(depends_on)}

def upgrade() -> None:
    op.add_column('creator', sa.Column('date_of_birth', sa.Date(), nullable=True))
    op.add_column('artwork', sa.Column('rating', sa.Float(), nullable=True))
    op.create_index('ix_artwork_rating', 'artwork', ['rating'])

def downgrade() -> None:
    op.drop_index('ix_artwork_rating', table_name='artwork')
    
    op.drop_column('artwork', 'rating')
    op.drop_column('creator', 'date_of_birth')
