import logging

from sanic import Sanic, response
from sanic_jinja2 import SanicJinja2
from sanic_jwt import Initialize, protected
from sanic_session import Session, InMemorySessionInterface
from tortoise.contrib.sanic import register_tortoise

from models import Users
from utility import autodiscover, authenticate

logging.basicConfig(level=logging.DEBUG)

app = Sanic(__name__)
app.config.SECRET = "asd"
app.static('/static', './static')

session = Session(app, interface=InMemorySessionInterface())
jinja = SanicJinja2(app, session=session)
Initialize(
    app,
    authenticate=authenticate,
    cookie_set=True,
    cookie_strict=False,
    login_redirect_url='/auth/login',
    path_to_authenticate='/login',
)

register_tortoise(
    app, db_url="sqlite://:memory:", modules={"models": ["models"]}, generate_schemas=True
)

autodiscover(app, 'views', recursive=True)


@app.get("/")
@protected(redirect_on_fail=True)
@jinja.template('index.jinja2')
async def list_all(request):
    users = await Users.all()
    return {'greetings': 'Hello, sanic!'}


@app.get("/user")
async def add_user(request):
    user = await Users.create(name="New User")
    return response.json({"user": str(user)})
