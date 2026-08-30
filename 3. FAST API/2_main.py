# Templates is like Invitation Card where we have some Prior Content and some Blanks to fill
# And per our need we Dynamically add the new Needed content into those Blanks to fill
# This prevents us from writing those f-string for each and every part and and act as a General Box for every related Package

from fastapi import FastAPI,Request
from fastapi.templating import Jinja2Templates
# We will be using Jinja2 for Templetee Design

app = FastAPI()

templates = Jinja2Templates(directory="templetes")
# This tells FastAPI where to look for the HTML templates in the Folder

posts: list[dict] = [
    {
        "id": 1,
        "author": "Hesenberg 25",
        "title": "FastAPI is Awesome",
        "content": "This framework is really easy to use and super fast.",
        "date_posted": "April 20, 2025",
    },
    {
        "id": 2,
        "author": "Jane Doe",
        "title": "Python is Great for Web Development",
        "content": "Python is a great language for web development, and FastAPI makes it even better.",
        "date_posted": "April 21, 2025",
    },
]

# request : Request => in this Syntax "request" is a Object of class "Request"
# Where the main need of the Class "Request" is just because we need to store the user info like the Website using, Cookies, IP Address, etc

@app.get("/")
@app.get("/posts")
def home(request : Request):
    return templates.TemplateResponse(request,"home.html")

# TemplateResponse(...) is a Function which helps in searching the provided file in the HardDrive
# templates => Declares that we are using Jinja2 which scan from Top to Bottom to look for Python Variables {...} and replace them with Dynamic Values
# Then again TemplateResponse(...) wraps your HTML reponse in form of HTTPS and Attaches "Content-Type: text/html" to tell WebPage to treat it as VisualPage
# And request in "templates.TemplateResponse(request,"home.html")" is the store house from where we retrive the user Data to Display
@app.get("/api/posts")
def get_posts():
    return posts