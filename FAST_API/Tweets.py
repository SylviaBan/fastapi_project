from pydantic import BaseModel

# 2. Class which contains a tweet
class Tweet(BaseModel):
    review: str
    