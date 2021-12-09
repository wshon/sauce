import platform

from sanic import Blueprint
from sanic.response import json
from sanic_jwt import protected

bp = Blueprint("info", url_prefix="/info")


def get_cpu():
    from utils.cpuinfo import cpu

    if platform.system() == "Windows":
        return cpu.info[0].get('ProcessorNameString', '').strip()
    elif platform.system() == "Linux":
        return cpu.info[0].get('model name', '')
    return ''


@bp.route("/base")
@protected()
async def bp_root(request):
    return json({
        'machine': platform.machine(),
        'node': platform.node(),
        'processor': get_cpu() or platform.processor(),
        'system': platform.system(),
        'release': platform.release(),
        'version': platform.version(),
    })
