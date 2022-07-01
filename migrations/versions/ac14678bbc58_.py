"""empty message

Revision ID: ac14678bbc58
Revises: 93ae06dd560a
Create Date: 2022-06-15 16:43:11.946881

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ac14678bbc58'
down_revision = '93ae06dd560a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('post', 'picture')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('picture', sa.VARCHAR(length=100), nullable=True))
    # ### end Alembic commands ###