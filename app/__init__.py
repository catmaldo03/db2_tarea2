from litestar import Litestar

from app.controlers import AuthorController, BookController, ClientController, baController
from app.database import sqlalchemy_config

app = Litestar(
    [AuthorController, BookController, ClientController, baController],
    debug=True,
    plugins=[sqlalchemy_config],
)
