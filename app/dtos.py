from litestar.contrib.sqlalchemy.dto import SQLAlchemyDTO, SQLAlchemyDTOConfig

from app.models import Author, Book, Client,Bookloan


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
    config = SQLAlchemyDTOConfig(exclude={"id", "author","book_loans"})

class BookUpdateDTO(SQLAlchemyDTO[Book]):
    config = SQLAlchemyDTOConfig(exclude={"id","author","author_id","book_loans"}, partial=True)


#clientes
class ClientReadDTO(SQLAlchemyDTO[Client]):
    pass

class ClientWriteDTO(SQLAlchemyDTO[Client]):
    config = SQLAlchemyDTOConfig(exclude={"id","book_loans"})

class ClientUpdateDTO(SQLAlchemyDTO[Client]):
    config = SQLAlchemyDTOConfig(exclude={"id","book_loans"}, partial=True)

#Bookloan
class BookloanReadDTO(SQLAlchemyDTO[Bookloan]):
    pass
class BookloanWriteDTO(SQLAlchemyDTO[Bookloan]):
    config = SQLAlchemyDTOConfig(exclude={"id","clients","books"})

class BookloanUpdateDTO(SQLAlchemyDTO[Bookloan]):
    config = SQLAlchemyDTOConfig(exclude={"id","clients","books"}, partial=True)