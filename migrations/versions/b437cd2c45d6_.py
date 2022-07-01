"""empty message

Revision ID: b437cd2c45d6
Revises: 88984d53dd1f
Create Date: 2022-07-01 22:47:21.696951

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b437cd2c45d6'
down_revision = '88984d53dd1f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('image_file', sa.String(length=20), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'image_file')
    # ### end Alembic commands ###