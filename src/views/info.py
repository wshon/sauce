from sanic import Blueprint
from sanic.response import json
from sanic_jwt import protected

bp = Blueprint("info", url_prefix="/info")


@bp.route("/base")
@protected(redirect_on_fail=True, redirect_url='/auth/login?from=/info/base')
async def bp_root(request):
    return json({"my": "blueprint"})
