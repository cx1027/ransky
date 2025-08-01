"""add score_analysis_result to job

Revision ID: afe3bf5d379b
Revises: 540c8231d9d9
Create Date: 2025-06-23 20:06:12.732704

"""
from alembic import op
import sqlalchemy as sa
import sqlmodel.sql.sqltypes


# revision identifiers, used by Alembic.
revision = 'afe3bf5d379b'
down_revision = '540c8231d9d9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('job', sa.Column('score_analysis_result', sqlmodel.sql.sqltypes.AutoString(length=10000), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('job', 'score_analysis_result')
    # ### end Alembic commands ###
