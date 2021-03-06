"""empty message

Revision ID: 787bef3465bd
Revises: 5c8d166eaf6d
Create Date: 2020-08-26 11:43:51.374170

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '787bef3465bd'
down_revision = '5c8d166eaf6d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('aboutme', sa.String(length=140), nullable=True))
    op.add_column('user', sa.Column('last_seen', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'last_seen')
    op.drop_column('user', 'aboutme')
    # ### end Alembic commands ###
