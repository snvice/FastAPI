"""create address_id to users

Revision ID: b7ac8fac715b
Revises: 9c1ca4f4f37f
Create Date: 2024-07-09 03:12:59.011014

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b7ac8fac715b'
down_revision: Union[str, None] = '9c1ca4f4f37f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('users', sa.Column('address_id', sa.Integer(), nullable=True))
    op.create_foreign_key('address_users_fk', source_table="users", referent_table="address",
                          local_cols=['address_id'], remote_cols=["id"], ondelete="CASCADE")

def downgrade() -> None:
    op.drop_constraint('address_users_fk', table_name="users")
    op.drop_column('users', 'address_id')
