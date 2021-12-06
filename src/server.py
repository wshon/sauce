import logging

from sanic import Sanic, response
from sanic_jinja2 import SanicJinja2
from sanic_jwt import Initialize
from sanic_session import Session, InMemorySessionInterface
from tortoise.contrib.sanic import register_tortoise

from auth import authenticate
from models import Users
from utility import autodiscover

logging.basicConfig(level=logging.DEBUG)

app = Sanic(__name__)

session = Session(app, interface=InMemorySessionInterface())
jinja = SanicJinja2(app, session=session)
Initialize(app, authenticate=authenticate)

register_tortoise(
    app, db_url="sqlite://:memory:", modules={"models": ["models"]}, generate_schemas=True
)

autodiscover(app, 'views', recursive=True)


@app.route("/")
@jinja.template('index.html')
async def list_all(request):
    users = await Users.all()
    return {'greetings': 'Hello, sanic!'}


@app.route("/user")
async def add_user(request):
    user = await Users.create(name="New User")
    return response.json({"user": str(user)})
