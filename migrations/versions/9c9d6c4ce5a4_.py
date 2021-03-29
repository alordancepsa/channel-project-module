"""empty message

Revision ID: 9c9d6c4ce5a4
Revises: 14681c33f598
Create Date: 2021-03-29 10:58:27.615535

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9c9d6c4ce5a4'
down_revision = '14681c33f598'
branch_labels = None
depends_on = None


def upgrade(engine_name):
    globals()["upgrade_%s" % engine_name]()


def downgrade(engine_name):
    globals()["downgrade_%s" % engine_name]()





def upgrade_():
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade_():
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def upgrade_datalake():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('master_flags', sa.Column('flagShort', sa.String(length=120), nullable=True))
    # ### end Alembic commands ###


def downgrade_datalake():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('master_flags', 'flagShort')
    # ### end Alembic commands ###
