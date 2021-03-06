"""addresses, profiles, and user

Revision ID: 2bfe54c360dc
Revises: 4308d0cfc691
Create Date: 2014-09-08 11:06:02.767163

"""

# revision identifiers, used by Alembic.
revision = '2bfe54c360dc'
down_revision = '4308d0cfc691'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('emails', sa.Column('user_id', sa.Integer(), nullable=True))
    op.add_column('profile', sa.Column('claimed', sa.Text(), nullable=True))
    op.add_column('user', sa.Column('is_community', sa.Boolean(), nullable=True))
    op.add_column('user', sa.Column('is_contributor', sa.Boolean(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'is_contributor')
    op.drop_column('user', 'is_community')
    op.drop_column('profile', 'claimed')
    op.drop_column('emails', 'user_id')
    ### end Alembic commands ###
