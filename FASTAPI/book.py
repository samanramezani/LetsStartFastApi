
from fastapi import FastAPI 
app = FastAPI() 


BOOKS = [
    {'title': "title one" , 'author' : 'author one' , 'category' : 'science'} ,
     {'title': "title tow" , 'author' : 'author two' , 'category' : 'science'} ,
      {'title': "title three" , 'author' : 'author three' , 'category' : 'history'} ,
       {'title': "title four" , 'author' : 'author four' , 'category' : 'math'} ,
        {'title': "title five" , 'author' : 'author five' , 'category' : 'math'} , 
         {'title': "title six" , 'author' : 'author six' , 'category' : 'math'} , 
]



@app.get("/hi") 
async def say_hi():
     return { 'salam' : 'mohsen'}

# @app.get("/books/{dynamic_param}") 
# async def read_all_books(dynamic_param):
#         return {'dynamic_param' : dynamic_param}


@app.get("/book/{book_title}") 
async def read_book(book_title: str):
        for book in BOOKS: 
            if book.get('title').casefold() == book_title.casefold():
                return book
