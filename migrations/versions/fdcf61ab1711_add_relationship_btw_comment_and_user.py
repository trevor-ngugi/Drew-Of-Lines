"""add  relationship btw comment and user

Revision ID: fdcf61ab1711
Revises: 7fa77002d3cb
Create Date: 2020-01-20 09:19:06.902255

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fdcf61ab1711'
down_revision = '7fa77002d3cb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('blogs', sa.Column('posted', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('blogs', 'posted')
    # ### end Alembic commands ###
