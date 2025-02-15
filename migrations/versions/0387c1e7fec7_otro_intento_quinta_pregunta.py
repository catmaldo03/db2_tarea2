"""Otro intento quinta pregunta

Revision ID: 0387c1e7fec7
Revises: 46cf552386e2
Create Date: 2023-12-03 11:38:56.799577

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "0387c1e7fec7"
down_revision: Union[str, None] = "46cf552386e2"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "book_loans",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("client_id", sa.Integer(), nullable=False),
        sa.Column("book_id", sa.Integer(), nullable=False),
        sa.Column("days_loans", sa.Integer(), nullable=False),
        sa.Column("date_loan", sa.Date(), nullable=True),
        sa.ForeignKeyConstraint(
            ["book_id"],
            ["books.id"],
        ),
        sa.ForeignKeyConstraint(
            ["client_id"],
            ["clients.id"],
        ),
        sa.PrimaryKeyConstraint("id", "client_id", "book_id"),
    )
    op.drop_table("book_Loans")
    op.add_column("books", sa.Column("copies", sa.Integer(), nullable=False))
    op.drop_column("books", "available_amount")
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "books", sa.Column("available_amount", sa.INTEGER(), autoincrement=False, nullable=False)
    )
    op.drop_column("books", "copies")
    op.create_table(
        "book_Loans",
        sa.Column("id", sa.INTEGER(), autoincrement=False, nullable=False),
        sa.Column("client_id", sa.INTEGER(), autoincrement=False, nullable=False),
        sa.Column("book_id", sa.INTEGER(), autoincrement=False, nullable=False),
        sa.Column("loan_date", sa.DATE(), autoincrement=False, nullable=True),
        sa.Column("days_loan", sa.INTEGER(), autoincrement=False, nullable=False),
        sa.ForeignKeyConstraint(["book_id"], ["books.id"], name="book_Loans_book_id_fkey"),
        sa.ForeignKeyConstraint(["client_id"], ["clients.id"], name="book_Loans_client_id_fkey"),
        sa.PrimaryKeyConstraint("id", "client_id", "book_id", name="book_Loans_pkey"),
    )
    op.drop_table("book_loans")
    # ### end Alembic commands ###
