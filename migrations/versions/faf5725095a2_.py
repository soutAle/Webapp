"""empty message

Revision ID: faf5725095a2
Revises: d78048860ab5
Create Date: 2024-10-08 01:39:55.335831

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'faf5725095a2'
down_revision = 'd78048860ab5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('offers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=100), nullable=False),
    sa.Column('description', sa.String(length=200), nullable=False),
    sa.Column('location', sa.String(length=100), nullable=False),
    sa.Column('salary', sa.Float(), nullable=False),
    sa.Column('contract_type', sa.String(length=50), nullable=False),
    sa.Column('company_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['company_id'], ['companies.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('projects',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=100), nullable=False),
    sa.Column('description', sa.String(length=200), nullable=False),
    sa.Column('technologies', sa.String(length=140), nullable=False),
    sa.Column('category', sa.String(length=200), nullable=False),
    sa.Column('developer_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['developer_id'], ['developers.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('companies', schema=None) as batch_op:
        batch_op.add_column(sa.Column('website', sa.String(length=120), nullable=True))
        batch_op.add_column(sa.Column('logo', sa.String(length=200), nullable=True))
        batch_op.alter_column('name',
               existing_type=sa.VARCHAR(length=100),
               type_=sa.String(length=50),
               existing_nullable=False)
        batch_op.alter_column('location',
               existing_type=sa.VARCHAR(length=100),
               type_=sa.String(length=50),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('companies', schema=None) as batch_op:
        batch_op.alter_column('location',
               existing_type=sa.String(length=50),
               type_=sa.VARCHAR(length=100),
               existing_nullable=False)
        batch_op.alter_column('name',
               existing_type=sa.String(length=50),
               type_=sa.VARCHAR(length=100),
               existing_nullable=False)
        batch_op.drop_column('logo')
        batch_op.drop_column('website')

    op.drop_table('projects')
    op.drop_table('offers')
    # ### end Alembic commands ###
