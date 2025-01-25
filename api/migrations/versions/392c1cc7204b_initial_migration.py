"""Initial migration

Revision ID: 392c1cc7204b
Revises: e55ae9d38f10
Create Date: 2025-01-25 19:02:44.035644

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '392c1cc7204b'
down_revision = 'e55ae9d38f10'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('password',
               existing_type=mysql.VARCHAR(length=120),
               type_=sa.String(length=128),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('password',
               existing_type=sa.String(length=128),
               type_=mysql.VARCHAR(length=120),
               existing_nullable=False)

    # ### end Alembic commands ###
