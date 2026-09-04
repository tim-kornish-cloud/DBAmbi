from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
# from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

# initialize fast api app
app = FastAPI()

# mount static folder for css to pull values into html
# 1. directory/location sub-path of static files to add to app, will include all folders starting with static
# 2. name of specific directory to look for static files
# 3. name that can be referenced by fastapi to pull values/files with
app.mount("/static", StaticFiles(directory = "static"), name = "static")

templates = Jinja2Templates(directory = "templates")

posts: list[dict] = [
  {
    "id" : 1,
    "author" : "Corey Schafer",
    "title" : "FastAPI is Awesome",
    "content" : "This framework is really easy to use and super fast.",
    "date_posted" : "April 20, 2025",
  },
  {
    "id" : 2,
    "author" : "Jane Doe",
    "title" : "Python is Great for Web Development",
    "content" : "Python is a great language for web development,  and FastAPI makes if even better.",
    "date_posted" : "April 21, 2025",
  }
]

# @app.get("/")
# def home():
#     return {"Message" : "Hello world payload"}

# include_in_schema -> add route to docs page when true, exclude when false
# @app.get("/", response_class = HTMLResponse, include_in_schema = True)
# @app.get("/posts", response_class = HTMLResponse, include_in_schema = False)
# def home():
#     return f"<h1>{posts[0]['title']}</h1>"

@app.get("/", include_in_schema = True)
@app.get("/posts", include_in_schema = False)
def home(request: Request):
    return templates.TemplateResponse(request, "home.html", {"posts" : posts, "title" : "Home"})

@app.get("/api/posts")
def get_posts():
    return posts
