from datetime import date
from typing import Optional

from sqlalchemy import ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


class Book(Base):
    __tablename__ = "books"

    id: Mapped[int] = mapped_column(primary_key=True)
    isbn: Mapped[str] = mapped_column(index=True)
    title: Mapped[str] = mapped_column(index=True)
    description: Mapped[str]
    year: Mapped[int]
    language: Mapped[str]
    author_id: Mapped[int] = mapped_column(ForeignKey("authors.id"))

    # relationships
    author: "Mapped[Author]" = relationship(back_populates="books")
    categories: "Mapped[list[Category]]" = relationship(
        back_populates="books", secondary="books_categories"
    )

    copies: Mapped[int]
    bas: "Mapped[list[ba]]" = relationship(back_populates="books")


class Author(Base):
    __tablename__ = "authors"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    biography: Mapped[Optional[str]]
    date_of_birth: Mapped[Optional[date]]

    # relationships
    books: "Mapped[list[Book]]" = relationship(back_populates="author")


class Category(Base):
    __tablename__ = "categories"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]

    # relationships
    books: "Mapped[list[Book]]" = relationship(
        back_populates="categories", secondary="books_categories"
    )


class BookCategory(Base):
    __tablename__ = "books_categories"

    book_id: Mapped[int] = mapped_column(ForeignKey("books.id"), primary_key=True)
    category_id: Mapped[int] = mapped_column(ForeignKey("categories.id"), primary_key=True)


class Client(Base):
    __tablename__ = "clients"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    last_name: Mapped[str]

    bas: "Mapped[list[ba]]" = relationship(back_populates="clients")


class ba(Base):
    __tablename__ = "bas"

    id: Mapped[int] = mapped_column(primary_key=True)
    book_id: Mapped[int] = mapped_column(ForeignKey("books.id"))
    client_id: Mapped[int] = mapped_column(ForeignKey("clients.id"))
    days_loans: Mapped[int]
    loan_date: Mapped[date]

    books: "Mapped[Book]" = relationship(back_populates="bas")
    clients: "Mapped[Client]" = relationship(back_populates="bas")
