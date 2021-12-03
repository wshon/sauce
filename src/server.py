import logging

from sanic import Sanic, response
from sanic.response import text
from tortoise.contrib.sanic import register_tortoise

from models import Users

logging.basicConfig(level=logging.DEBUG)

app = Sanic(__name__)


# @app.get("/")
# async def hello_world(request):
#     return text("Hello, world.")


@app.route("/")
async def list_all(request):
    users = await Users.all()
    return response.json({"users": [str(user) for user in users]})


@app.route("/user")
async def add_user(request):
    user = await Users.create(name="New User")
    return response.json({"user": str(user)})


register_tortoise(
    app, db_url="sqlite://:memory:", modules={"models": ["models"]}, generate_schemas=True
)
