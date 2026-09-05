# Just like Templates are Dynamic Content holding place in Jinja2 in the same way to Hold differnt URL links we use Path Parameter
# Path parameters are dynamic variables embedded directly inside a web URL. 
# They act as placeholders that allow a single route to handle many different requests by extracting specific values directly from the web address.
# Like instead for doing (posts/1),(posts/2).... we can use (posts/{post_id})

from fastapi import FastAPI, Request, HTTPException, status
from fastapi.exceptions import RequestValidationError
# This used for Validation of Path Parameters

from fastapi.responses import JSONResponse 
# Manually return JSON Response from our Exceptions

from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.exceptions import HTTPException as StarletteHTTPException
# We are using starlette because FastAPI is built on StarLette and the Exception is raised by Starlette rather than FastAPI

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templetes")

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


@app.get("/",name="home")
@app.get("/posts",name="posts")
def home(request : Request):
    return templates.TemplateResponse(
        request,
        "home.html",
        {"posts":posts,"title":"Home"},
        )


# Here we are creating a Path Parameters for Displaying Indivisual post to User End
# This done using syntax "api/posts/{...}" for Dynamic route Allocation for required post
# And the Type Casting inside the Function of the Route help in Function Argument {post_id : int}
# And FastAPI automatically validates the variable to check if it fits

@app.get("/posts/{post_id}")
def post_page(request : Request, post_id : int):
    for post in posts:
        if post.get("id")==post_id:
            title = post["title"][:50]
            return templates.TemplateResponse(
                request,
                "post.html",
                {"post" : post,"title":title})
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Post not Found")

# The use of returning error is not a good Practise 
# Because even we are not having a post with the provided id we stil are getting 200 msg instead of 404
# So we use HTTPSExeception using 404 status code and for this we use HTTPSExeception 

# Data Validation is also a major use in FastAPI which help in Miss handling of the Dynamic Routes
# Like if we put any string like "hello" in hte route in the Brower we will an Error like :
# {
#   "detail": [
#     {
#       "type": "int_parsing",
#       "loc": [
#         "path",
#         "post_id"
#       ],
#       "msg": "Input should be a valid integer, unable to parse string as an integer",
#       "input": "hello"
#     }
#   ]
# }
# Which is telling that the Input should be valid Int not an String

@app.get("/api/posts")
def get_posts():
    return posts

# The Below two Error Handlers Handles the Errors for both API enduser and even Frontend User

# This handles Error like now we only have 2 Posts but if we try to Access 99th posts this error will occur
@app.exception_handler(StarletteHTTPException)
def general_http_exception_handler(request : Request, exception : StarletteHTTPException):
    message = (
        exception.detail
        if exception.detail
        else "An Error Occurred. Please check your request an try again."
    )
    if request.url.path.startswith("/api"):
        return JSONResponse(
            status_code=exception.status_code,
            content={"detail" : message}
        )
    return templates.TemplateResponse(
        request,
        "error.html",
        {
            "status_code" : exception.status_code,
            "title" : exception.status_code,
            "message" : message,
        },
        status_code=exception.status_code
    )

# 1. 
# @app.exception_handler(StarletteHTTPException) => this helps in catching the Starlette Error

# 2.
# def general_http_exception_handler(request : Request, exception : StarletteHTTPException) => this helps in request catching because the the Jinja2 for frontend
# And exception is the Instance of the current Starlette Error

# 3. 
# message = (
#         exception.detail => get the detail of the Exception
#         if exception.detail => if it exists it is the msg we print
#         else "An Error Occurred. Please check your request an try again." => if there is no detail this HardCoded msg
#     )
# This helps in building msg to show that what went wrong

# 4.
# if request.url.path.startswith("/api"):
#         return JSONResponse(
#             status_code=exception.status_code,
#             content={"detail" : message}
#         )
# When the user need the api ends we return the JSON part

# 5.
# return templates.TemplateResponse(
#         request,
#         "error.html",
#         {
#             "status_code" : exception.status_code,
#             "title" : exception.status_code,
#             "message" : message,
#         },
#         status_code=exception.status_code
#     )
# This is for the Frontend User who will just the the Jinja2 Template


# But this Error occurs when in path parameters which need int for next post page we put other data type this is call Validation
@app.exception_handler(RequestValidationError)
def validation_exception_handler(request: Request, exception: RequestValidationError):
    if request.url.path.startswith("/api"):
        return JSONResponse(
            status_code=status.HTTP_422_UNPROCESSABLE_CONTENT,
            content={"detail": exception.errors()},
        )
    return templates.TemplateResponse(
        request,
        "error.html",
        {
            "status_code": status.HTTP_422_UNPROCESSABLE_CONTENT,
            "title": status.HTTP_422_UNPROCESSABLE_CONTENT,
            "message": "Invalid request. Please check your input and try again.",
        },
        status_code=status.HTTP_422_UNPROCESSABLE_CONTENT,
    )
# In this error there is no need for creating msg as Validation error itself is just for Error 422 and can be HardCoded
