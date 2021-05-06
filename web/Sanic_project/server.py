import asyncio

from sanic import Sanic
from sanic.response import text, json, stream
from Dbs import get_course
cat_list=[]
app = Sanic("My Hello, world app")

@app.get("/")
async def hello_world(request):
    return text("Hello, world.")

@app.get("/api/course/<currency>")
async def tag_handler(request, currency):
    course_rub = get_course(currency)
    return text("{}".format(course_rub))


@app.route('/hi',)
async def hi_my_name_is(request):
    return text("Hi, my name is {}".format(request))

async def sample_streaming_fn(response):
    await response.write("foo")
    await asyncio.sleep(1)
    await response.write("bar")
    await asyncio.sleep(1)\
    @app.post("/q")
    async def test(request):
        return stream(sample_streaming_fn)


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8080)