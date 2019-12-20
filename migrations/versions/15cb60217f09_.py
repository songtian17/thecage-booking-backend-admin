"""empty message

Revision ID: 15cb60217f09
Revises: cc542df161fc
Create Date: 2019-12-19 02:29:32.210753

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '15cb60217f09'
down_revision = 'cc542df161fc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('Pitch_name_key', 'Pitch', type_='unique')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint('Pitch_name_key', 'Pitch', ['name'])
    # ### end Alembic commands ###