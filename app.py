from sanic import Sanic, response
from sanic.response import stream
from utils import streamer


app = Sanic(__name__)


@app.route('/')
async def index(request):
    return response.json({
        "status": "ok"
    })


@app.route("/stream")
async def stream_data(request):
    return stream(streamer, content_type='text/csv')


@app.route('/html')
async def html(request):
    return response.html('<h2>This is nice!</h2>')
