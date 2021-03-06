"""empty message

Revision ID: cd4731ccd587
Revises: 6546e510ecea
Create Date: 2020-01-27 12:46:18.889267

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cd4731ccd587'
down_revision = '6546e510ecea'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'Artist', ['phone'])
    op.create_unique_constraint(None, 'Artist', ['name'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'Artist', type_='unique')
    op.drop_constraint(None, 'Artist', type_='unique')
    # ### end Alembic commands ###
