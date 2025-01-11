from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = 'your_revision_id' 
down_revision: Union[str, None] = 'previous_revision_id' 
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade() -> None:
    op.add_column('artwork', sa.Column('additional_info', sa.JSON(), nullable=True))

def downgrade() -> None:
    op.drop_column('artwork', 'additional_info')
