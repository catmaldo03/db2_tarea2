from litestar import Litestar

from app.controlers import AuthorController, BookController,ClientController,BookloanController
from app.database import sqlalchemy_config

app = Litestar([AuthorController, BookController,ClientController,BookloanController], debug=True, plugins=[sqlalchemy_config])
