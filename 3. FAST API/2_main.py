# Templates is like Invitation Card where we have some Prior Content and some Blanks to fill
# And per our need we Dynamically add the new Needed content into those Blanks to fill
# This prevents us from writing those f-string for each and every part and and act as a General Box for every related Package

from fastapi import FastAPI,Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
# We will be using Jinja2 for Templetee Design

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

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

@app.get("/",name="home")
@app.get("/posts",name="posts")
def home(request : Request):
    return templates.TemplateResponse(
        request,
        "home.html",
        {"posts":posts,"title":"Home"},
        )

# TemplateResponse(...) is a Function which helps in searching the provided file in the HardDrive
# templates => Declares that we are using Jinja2 which scan from Top to Bottom to look for Python Variables {...} and replace them with Dynamic Values
# Then again TemplateResponse(...) wraps your HTML reponse in form of HTTPS and Attaches "Content-Type: text/html" to tell WebPage to treat it as VisualPage
# And request in "templates.TemplateResponse(request,"home.html")" is the store house from where we retrive the user Data to Display
# "return templates.TemplateResponse(...)" turns on the Jinja2 HTML rendering engine. You are instructing FastAPI not to return raw JSON text, but to build and return a complete visual webpage.

# Arguments inside "templates.TemplateResponse(...)" :
# 1. "request" object just because Jinja2 need it to study the Layout of the User Page through whcih the User is Viewing the Website
# 2. "home.html" tells Jinja2 where to look for the Template Design and to Dynamically change {{ ... }}
# 3. "{"posted":posts}" this is very Critical Syntax :
#       "posted" means we are tells Jinja2 to look for the Variable "posted in the html Template format file
#       "posts" is the the Dynamic Content we are passing to Jinja2 to Write the {{...}} part
# 4. "{"title":"Home"}" is a Syntax to tell Jinja2 that "Home" should be the Title of our WebPage

# So we could tell that in the Syntax of {"..." : "***"} the "..." will be the value Jinja2 will be looking in the HTML file and "***" will be the Content it will be Dynamically inserting 

# {% ... %} is a way to tell Jinja2 to Peform the Python like Operation like here it is Running for loop 


# Sometimes we need some Visuals which are Common in all the WebPage Visuals
# And Editing one can cause a need to edit the other Places too so we use Inheritance in Jinja2 in form of "block" which can be Overriddin by Child Templates

@app.get("/api/posts")
def get_posts():
    return posts