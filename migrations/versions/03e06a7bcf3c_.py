"""empty message

Revision ID: 03e06a7bcf3c
Revises: ac14678bbc58
Create Date: 2022-06-15 16:43:25.706965

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '03e06a7bcf3c'
down_revision = 'ac14678bbc58'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('picture', sa.String(length=20), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('post', 'picture')
    # ### end Alembic commands ###
