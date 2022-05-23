"""create phone number for user col

Revision ID: 5595d390f0ad
Revises: 
Create Date: 2022-05-22 22:58:40.533940

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5595d390f0ad'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('users', sa.Column('phone_number', sa.String(), nullable=True))


def downgrade():
    op.drop_column('users', 'phone_number')

