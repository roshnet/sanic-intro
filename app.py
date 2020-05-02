from sanic import Sanic, response

app = Sanic(__name__)


@app.route('/')
async def index(request):
    return response.json({
        "status": "ok"
    })


@app.route('/html')
async def html(request):
    return response.html('<h2>This is nice!</h2>')
