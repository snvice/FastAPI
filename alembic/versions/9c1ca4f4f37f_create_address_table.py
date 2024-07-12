"""create address table

Revision ID: 9c1ca4f4f37f
Revises: f8cf5c76d530
Create Date: 2024-07-09 02:56:30.782213

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9c1ca4f4f37f'
down_revision: Union[str, None] = 'f8cf5c76d530'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('address',
        sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
        sa.Column('address1', sa.String(), nullable=False),
        sa.Column('address2', sa.String(), nullable=True),
        sa.Column('city', sa.String(), nullable=False),
        sa.Column('state', sa.String(), nullable=False),
        sa.Column('country', sa.String(), nullable=False),
        sa.Column('postalcode', sa.String(), nullable=False)
    )

def downgrade() -> None:
    op.drop_table('address')
