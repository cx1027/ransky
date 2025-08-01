"""add candidate analysis table

Revision ID: 61def211e877
Revises: a33da1c23e70
Create Date: 2025-06-22 13:56:09.661071

"""
from alembic import op
import sqlalchemy as sa
import sqlmodel.sql.sqltypes


# revision identifiers, used by Alembic.
revision = '61def211e877'
down_revision = 'a33da1c23e70'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('candidateanalysis',
    sa.Column('id', sa.Uuid(), nullable=False),
    sa.Column('file_name', sqlmodel.sql.sqltypes.AutoString(length=255), nullable=False),
    sa.Column('analysis_result', sqlmodel.sql.sqltypes.AutoString(length=10000), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_candidateanalysis_file_name'), 'candidateanalysis', ['file_name'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_candidateanalysis_file_name'), table_name='candidateanalysis')
    op.drop_table('candidateanalysis')
    # ### end Alembic commands ###
