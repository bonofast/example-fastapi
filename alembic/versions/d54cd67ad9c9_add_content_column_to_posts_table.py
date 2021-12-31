"""add content column to posts table

Revision ID: d54cd67ad9c9
Revises: f702fe7ca4bb
Create Date: 2021-12-30 22:06:39.690493

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd54cd67ad9c9'
down_revision = 'f702fe7ca4bb'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
