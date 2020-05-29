"""create work_queue tables

Revision ID: 98c5a08793e3
Revises:
Create Date: 2020-05-18 16:32:32.297089

"""
import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = "98c5a08793e3"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "job",
        sa.Column("id", sa.Integer, primary_key=True),
    )

def downgrade():
    op.drop_table("job")
