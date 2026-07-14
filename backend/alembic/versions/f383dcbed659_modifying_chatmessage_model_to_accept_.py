"""modifying chatmessage model to accept null values for tokens

Revision ID: f383dcbed659
Revises: 2903cea951b6
Create Date: 2026-07-14 05:35:58.336099

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f383dcbed659'
down_revision: Union[str, Sequence[str], None] = '2903cea951b6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
