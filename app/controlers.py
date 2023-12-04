from litestar import Controller, get, patch, post
from litestar.di import Provide
from litestar.dto import DTOData
from litestar.exceptions import HTTPException, NotFoundException

from app.dtos import (
    AuthorReadDTO,
    AuthorReadFullDTO,
    AuthorUpdateDTO,
    AuthorWriteDTO,
    BookReadDTO,
    BookReadFullDTO,
    BookUpdateDTO,
    BookWriteDTO,
    ClientReadDTO,
    ClientReadFullDTO,
    ClientUpdateDTO,
    ClientWriteDTO,
    baReadDTO,
    baReadFullDTO,
    baUpdateDTO,
    baWriteDTO,
)
from app.models import Author, Book, Client, ba
from app.repositories import (
    AuthorRepository,
    BookRepository,
    ClientRepository,
    baRepository,
    provide_authors_repo,
    provide_bas_repo,
    provide_books_repo,
    provide_clients_repo,
)


class AuthorController(Controller):
    path = "/authors"
    tags = ["authors"]
    return_dto = AuthorReadDTO
    dependencies = {"authors_repo": Provide(provide_authors_repo)}

    @get()
    async def list_authors(self, authors_repo: AuthorRepository) -> list[Author]:
        return authors_repo.list()

    @post(dto=AuthorWriteDTO)
    async def create_author(self, data: Author, authors_repo: AuthorRepository) -> Author:
        return authors_repo.add(data)

    @get("/{author_id:int}", return_dto=AuthorReadFullDTO)
    async def get_author(self, author_id: int, authors_repo: AuthorRepository) -> Author:
        return authors_repo.get(author_id)

    @patch("/{author_id:int}", dto=AuthorUpdateDTO)
    async def update_author(
        self, author_id: int, data: DTOData[Author], authors_repo: AuthorRepository
    ) -> Author:
        author = authors_repo.get(author_id)
        author = data.update_instance(author)
        return authors_repo.update(author)


class BookController(Controller):
    path = "/books"
    tags = ["books"]
    return_dto = BookReadDTO
    dependencies = {"books_repo": Provide(provide_books_repo)}

    @get()
    async def list_books(self, books_repo: BookRepository) -> list[Book]:
        return books_repo.list()

    @post(dto=BookWriteDTO)
    async def create_book(self, data: Book, books_repo: BookRepository) -> Book:
        return books_repo.add(data)

    @get("/{book_id:int}", return_dto=BookReadFullDTO)
    async def get_book(self, book_id: int, books_repo: BookRepository) -> Book:
        try:
            return books_repo.get(book_id)
        except:
            raise NotFoundException("El libro no existe")

    @patch("/{book_id:int}", dto=BookUpdateDTO)
    async def update_book(
        self, book_id: int, data: DTOData[Book], books_repo: BookRepository
    ) -> Book:
        book = books_repo.get(book_id)
        book = data.update_instance(book)
        return books_repo.update(book)


class ClientController(Controller):
    path = "/clients"
    tags = ["clients"]
    return_dto = ClientReadDTO
    dependencies = {"clients_repo": Provide(provide_clients_repo)}

    @get()  # lista de clientes
    async def list_clients(self, clients_repo: ClientRepository) -> list[Client]:
        return clients_repo.list()

    @post(dto=ClientWriteDTO)  # agregar cliente
    async def create_client(self, data: Client, clients_repo: ClientRepository) -> Client:
        return clients_repo.add(data)

    @get("/{client_id:int}", return_dto=ClientReadFullDTO)  # obtener clientes por id
    async def get_client(self, client_id: int, clients_repo: ClientRepository) -> Client:
        try:
            return clients_repo.get(client_id)
        except:
            raise NotFoundException("El cliente no existe")

    @patch("/{client_id:int}", dto=ClientUpdateDTO)  # Actualizar cliente
    async def update_client(
        self, client_id: int, data: DTOData[Client], clients_repo: ClientRepository
    ) -> Client:
        client = clients_repo.get(client_id)
        client = data.update_instance(client)
        return clients_repo.update(client)


class baController(Controller):
    path = "/bas"
    tags = ["bas"]
    return_dto = baReadDTO
    dependencies = {
        "bas_repo": Provide(provide_bas_repo),
        "books_repo": Provide(provide_books_repo),
        "clients_repo": Provide(provide_clients_repo),
    }

    @get()  # lista de pedidos
    async def list_bas(self, bas_repo: baRepository) -> list[ba]:
        return bas_repo.list()

    @post(dto=baWriteDTO)  # agregar deuda
    async def create_bas(self, data: ba, bas_repo: baRepository, books_repo: BookRepository) -> ba:
        book = books_repo.get(data.book_id)
        if book.copies == 0:
            raise HTTPException(
                detail="No hay copias disponibles",
                status_code=400,
            )
        bas_repo.add(data)
        book.copies -= 1
        books_repo.update(book)
        return data

    @get("/{bas_id:int}", return_dto=baReadFullDTO)  # obtener deuda por id
    async def get_bas(self, bas_id: int, bas_repo: baRepository) -> ba:
        try:
            return bas_repo.get(bas_id)
        except:
            raise NotFoundException("El prestamo no existe")

    @patch("/{bas_id:int}", dto=baUpdateDTO)  # Actualizar cliente
    async def update_bas(self, bas_id: int, data: DTOData[ba], bas_repo: baRepository) -> ba:
        loan = bas_repo.get(bas_id)
        loan = data.update_instance(loan)
        return bas_repo.update(loan)
