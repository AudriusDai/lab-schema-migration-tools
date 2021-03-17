"""create account table

Revision ID: 50714ca6c847
Revises: 
Create Date: 2021-03-17 10:15:31.400424

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '50714ca6c847'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'account',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), nullable=False),
        sa.Column('description', sa.Unicode(200)),
    )


def downgrade():
    op.drop_table('account')
