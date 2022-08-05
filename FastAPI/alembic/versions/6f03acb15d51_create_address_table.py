"""Create address table

Revision ID: 6f03acb15d51
Revises: 5595d390f0ad
Create Date: 2022-05-23 22:21:41.034072

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = '6f03acb15d51'
down_revision = '5595d390f0ad'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('address',
        sa.Column('id', sa.Integer, nullable=False, primary_key=True),
        sa.Column('address1', sa.String(), nullable=False),
        sa.Column('address2', sa.String(), nullable=False),
        sa.Column('city', sa.String(), nullable=False),
        sa.Column('state', sa.String(), nullable=False),
        sa.Column('country', sa.String(), nullable=False),
        sa.Column('postalcode', sa.String(), nullable=False)
    )


def downgrade():
    op.drop_table('address')
