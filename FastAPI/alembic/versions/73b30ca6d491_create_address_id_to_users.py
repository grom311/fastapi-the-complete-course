"""create address_id to users

Revision ID: 73b30ca6d491
Revises: 6f03acb15d51
Create Date: 2022-05-23 22:29:57.399413

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '73b30ca6d491'
down_revision = '6f03acb15d51'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('users', sa.Column('address_id', sa.Integer(), nullable=True))
    op.create_foreign_key('address_users_fk', source_table='users', referent_table='address', local_cols=['address_id'], remote_cols=["id"], ondelete="CASCADE")

def downgrade():
    op.drop_constraint('address_users_fk', table_name="users")
    op.drop_column('users', 'address_id')
