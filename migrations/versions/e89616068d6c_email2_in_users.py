"""email2_in_users

Revision ID: e89616068d6c
Revises: 8d09f0b94fcc
Create Date: 2021-03-26 21:49:09.230946

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e89616068d6c'
down_revision = '8d09f0b94fcc'
branch_labels = None
depends_on = None


def upgrade(engine_name):
    globals()["upgrade_%s" % engine_name]()


def downgrade(engine_name):
    globals()["downgrade_%s" % engine_name]()





def upgrade_():
    # ### commands auto generated by Alembic - please adjust! ###
    # ### end Alembic commands ###
    pass

def downgrade_():
    # ### commands auto generated by Alembic - please adjust! ###
    # ### end Alembic commands ###
    pass

def upgrade_datalake():
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade_datalake():
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
