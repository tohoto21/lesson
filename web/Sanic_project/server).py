from sanic import Sanic
from sanic.response import text, json
from Dbs import get_course
app = Sanic("My Hello, world app")

@app.get("/")
async def hello_world(request):
    return text("Hello, world.")

@app.get("/api/course/<currency>")
async def tag_handler(request, currency):
    course_rub = get_course(currency)
    return text("{}".format(course_rub))

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8080)