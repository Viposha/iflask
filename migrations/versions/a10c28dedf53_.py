"""empty message

Revision ID: a10c28dedf53
Revises: aeabbd3fdf06
Create Date: 2022-06-15 16:11:18.364578

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a10c28dedf53'
down_revision = 'aeabbd3fdf06'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('post', 'date_posted')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('date_posted', sa.DATETIME(), nullable=False))
    # ### end Alembic commands ###