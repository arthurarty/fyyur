"""empty message

Revision ID: 77ca986210cc
Revises: 6440d312d0df
Create Date: 2020-01-22 14:11:56.999177

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '77ca986210cc'
down_revision = '6440d312d0df'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('genres_artists',
    sa.Column('artist_id', sa.Integer(), nullable=False),
    sa.Column('genre_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['artist_id'], ['Artist.id'], ),
    sa.ForeignKeyConstraint(['genre_id'], ['Genre.id'], ),
    sa.PrimaryKeyConstraint('artist_id', 'genre_id')
    )
    op.drop_column('Artist', 'genres')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Artist', sa.Column('genres', sa.VARCHAR(length=120), autoincrement=False, nullable=True))
    op.drop_table('genres_artists')
    # ### end Alembic commands ###
