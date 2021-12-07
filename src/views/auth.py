from sanic import Blueprint

from server import jinja

auth = Blueprint("auth", url_prefix="/auth")


@auth.get("/login")
@jinja.template('auth_login.jinja2')
async def pg_login(request):
    return {'greetings': 'Hello, sanic!'}
