"""empty message

Revision ID: af836bb0d2ac
Revises: 43d9a0ac54ec
Create Date: 2016-10-27 21:10:33.764903

"""

# revision identifiers, used by Alembic.
revision = 'af836bb0d2ac'
down_revision = '43d9a0ac54ec'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('mlh_id', sa.Integer(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'mlh_id')
    ### end Alembic commands ###