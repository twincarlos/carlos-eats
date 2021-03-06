"""empty message

Revision ID: a9ac50589310
Revises: bb3f4d3a794e
Create Date: 2022-05-18 15:27:20.925599

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a9ac50589310'
down_revision = 'bb3f4d3a794e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('order_items', sa.Column('quantity', sa.Integer(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('order_items', 'quantity')
    # ### end Alembic commands ###
