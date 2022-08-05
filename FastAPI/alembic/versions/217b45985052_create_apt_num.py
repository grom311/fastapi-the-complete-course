"""Create apt_num

Revision ID: 217b45985052
Revises: 73b30ca6d491
Create Date: 2022-05-23 23:30:24.678145

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = '217b45985052'
down_revision = '73b30ca6d491'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('address', sa.Column('apt_num', sa.Integer(), nullable=True))


def downgrade():
    op.drop_column('address', 'apt_num')
