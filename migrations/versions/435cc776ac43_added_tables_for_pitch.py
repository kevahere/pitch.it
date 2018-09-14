"""added tables for pitch

Revision ID: 435cc776ac43
Revises: a633bac5feb3
Create Date: 2018-09-13 16:13:07.796046

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '435cc776ac43'
down_revision = 'a633bac5feb3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pitches', sa.Column('category_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'pitches', 'categories', ['category_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'pitches', type_='foreignkey')
    op.drop_column('pitches', 'category_id')
    # ### end Alembic commands ###
