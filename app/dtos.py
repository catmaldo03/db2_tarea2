from litestar.contrib.sqlalchemy.dto import SQLAlchemyDTO, SQLAlchemyDTOConfig

from app.models import Author, Book, Client, ba


class AuthorReadDTO(SQLAlchemyDTO[Author]):
    config = SQLAlchemyDTOConfig(exclude={"books"})


class AuthorReadFullDTO(SQLAlchemyDTO[Author]):
    pass


class AuthorWriteDTO(SQLAlchemyDTO[Author]):
    config = SQLAlchemyDTOConfig(exclude={"id", "books"})


class AuthorUpdateDTO(SQLAlchemyDTO[Author]):
    config = SQLAlchemyDTOConfig(exclude={"id", "books"}, partial=True)


class BookReadDTO(SQLAlchemyDTO[Book]):
    pass


class BookWriteDTO(SQLAlchemyDTO[Book]):
    config = SQLAlchemyDTOConfig(exclude={"id", "author", "bas"})


class BookUpdateDTO(SQLAlchemyDTO[Book]):
    config = SQLAlchemyDTOConfig(exclude={"id", "author", "author_id", "bas"}, partial=True)


class BookReadFullDTO(SQLAlchemyDTO[Book]):
    pass


# clientes
class ClientReadDTO(SQLAlchemyDTO[Client]):
    pass


class ClientWriteDTO(SQLAlchemyDTO[Client]):
    config = SQLAlchemyDTOConfig(exclude={"id", "bas"})


class ClientUpdateDTO(SQLAlchemyDTO[Client]):
    config = SQLAlchemyDTOConfig(exclude={"id", "bas"}, partial=True)


class ClientReadFullDTO(SQLAlchemyDTO[Client]):
    pass


# Prestamo de libros
class baReadDTO(SQLAlchemyDTO[ba]):
    pass


class baWriteDTO(SQLAlchemyDTO[ba]):
    config = SQLAlchemyDTOConfig(exclude={"id", "clients", "books"})


class baUpdateDTO(SQLAlchemyDTO[ba]):
    config = SQLAlchemyDTOConfig(exclude={"id", "clients", "books"}, partial=True)


class baReadFullDTO(SQLAlchemyDTO[ba]):
    pass
