from pydantic import BaseModel, ConfigDict, Field
# Basse Model is the Parent Class from where we import ydantic Lib
# Field is for Minimum and Maximum Constraints
# ConfigDict is like the security for the incoming data from the user end

class PostBase(BaseModel):
    title : str = Field(min_length=1, max_length=100)
    content : str = Field(min_length=1)
    author : str = Field(min_length=1, max_length=50)

# Pydantic at runtime validates this DataTypes


class PostCreate(PostBase):
    pass

class PostResponse(PostBase):
    model_config = ConfigDict(from_attributes=True)
    # model_config is a way to set up some parameter around the Data we are going to access to prevnt error and ConfigDict is class from Lib Pydantic which help us write those Rules 
    # This allows object to get data from objects with Attributes
    # Earlier when we are using dict we Access the Data by {post['title']} but when we are using Schema we use them by dot operator {post.title}
    
    
    
    # These are the things which are not provided from the user
    id : int
    date_posted :  str