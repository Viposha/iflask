"""empty message

Revision ID: a308527be4f9
Revises: 90bd0b4b3f65
Create Date: 2022-06-15 16:32:22.166737

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a308527be4f9'
down_revision = '90bd0b4b3f65'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('post', 'date_posted')
    op.drop_column('post', 'picture')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('picture', sa.VARCHAR(length=100), nullable=False))
    op.add_column('post', sa.Column('date_posted', sa.DATETIME(), nullable=False))
    # ### end Alembic commands ###
