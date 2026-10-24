from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from snippets import posts

templates = Jinja2Templates(directory='./templates')

app = FastAPI()

app.mount("/static", StaticFiles(directory="./static"), name="static")

@app.get("/", include_in_schema=False, name="home")
@app.get("/posts", include_in_schema=False, name="posts")
def home(request: Request):
    return templates.TemplateResponse(request, "home.html", {"posts": posts, "title": "home"})


@app.get("/api/posts")
def get_posts():
    return posts