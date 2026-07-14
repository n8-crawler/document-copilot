"""modifying chatmessage model to accept null values for tokens

Revision ID: 2903cea951b6
Revises: 4ac3831324da
Create Date: 2026-07-14 05:29:55.938814

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2903cea951b6'
down_revision: Union[str, Sequence[str], None] = '4ac3831324da'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
