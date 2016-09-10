"""empty message

Revision ID: e17cc549fd65
Revises: 1739031ab894
Create Date: 2016-09-09 22:44:43.069636

"""

# revision identifiers, used by Alembic.
revision = 'e17cc549fd65'
down_revision = '1739031ab894'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('interests', sa.Text(), nullable=True))
    op.add_column('users', sa.Column('num_hackathons', sa.Integer(), nullable=True))
    op.add_column('users', sa.Column('skill_level', sa.Integer(), nullable=True))
    op.drop_column('users', 'first_hackathon')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('first_hackathon', sa.VARCHAR(length=100), autoincrement=False, nullable=True))
    op.drop_column('users', 'skill_level')
    op.drop_column('users', 'num_hackathons')
    op.drop_column('users', 'interests')
    ### end Alembic commands ###
