# To run the .py file twe must use the Syntax
# fastapi dev main.py
# dev mode help us to save the changes Dynamically

from fastapi import FastAPI
# fastapi is a Lib which we are using to learn the Backend in the Python
# FastAPI is a class of the Lib fastapi

from fastapi.responses import HTMLResponse
# This class is used to view the Content in form of HTML

app = FastAPI()
# Here we have created an Object "app" of the class FasstAPI

# Route is like a Traffic Police which direct all the incoming Requests form the Web to the Backend Server
# And help them to get there needed location for doing the requried operations
# It has two parts : 
# 1. URL : which tell which path to Access
# 2. HTTPS : what operation to perform wheenhe arrives at that Location
# FastAPI uses Decorators for Routes

# This is the Syntax for making a Route
# @app.get("/") this is a path Operation Decorator
# .get means we need to retrive Data from the Server
# "/" means we need to find it in the URL path in Root URL or the HomePage

@app.get("/",response_class=HTMLResponse)

@app.get("/posts",response_class=HTMLResponse)
# If we want various diffent routes to show sam Function we Stack them bottom to each Other

# response_class=HTMLResponse help us to view the content is form of HTML
def home():
    # return{"message":"Hello World!"}
    return f"<h1>Hello World</h1>" 

# Ex we are using
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

@app.get("/api/posts",response_class=HTMLResponse)

# response_class=HTMLResponse help us to view the content is form of HTML
def get_posts():
    # return posts => this will give us output in form of JSON
    return f"<h1>{posts[0]['title']}</h1>"