"""empty message

Revision ID: 5b686024b828
Revises: 
Create Date: 2024-04-29 16:38:37.246367

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5b686024b828'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('categories',
    sa.Column('cid', sa.Integer(), nullable=False),
    sa.Column('category_name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('cid')
    )
    op.create_table('users',
    sa.Column('uid', sa.Integer(), nullable=False),
    sa.Column('password', sa.String(length=60), nullable=False),
    sa.Column('username', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('uid'),
    sa.UniqueConstraint('username')
    )
    op.create_table('quotes',
    sa.Column('qid', sa.Integer(), nullable=False),
    sa.Column('movie_id', sa.Integer(), nullable=False),
    sa.Column('character_id', sa.Integer(), nullable=False),
    sa.Column('movie_type', sa.Enum('TV Show', 'Movie'), nullable=False),
    sa.Column('category_id', sa.Integer(), nullable=True),
    sa.Column('quote', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['category_id'], ['categories.cid'], ),
    sa.PrimaryKeyConstraint('qid')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('quotes')
    op.drop_table('users')
    op.drop_table('categories')
    # ### end Alembic commands ###
