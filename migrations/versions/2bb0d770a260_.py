"""empty message

Revision ID: 2bb0d770a260
Revises: 787bef3465bd
Create Date: 2020-08-26 12:47:03.519900

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2bb0d770a260'
down_revision = '787bef3465bd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user') as bop:
        bop.alter_column('aboutme', new_column_name='about_me')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('aboutme', sa.VARCHAR(length=140), nullable=True))
    op.drop_column('user', 'about_me')
    # ### end Alembic commands ###
