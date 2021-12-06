from sanic import Blueprint

bp = Blueprint("info", url_prefix="/info")


@bp.route("/base")
async def bp_root(request):
    return json({"my": "blueprint"})
