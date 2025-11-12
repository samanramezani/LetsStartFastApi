
from fastapi import Body, FastAPI 
app = FastAPI() 


BOOKS = [
    {'title': "title one" , 'author' : 'author one' , 'category' : 'science' } ,
     {'title': "title tow" , 'author' : 'author two' , 'category' : 'science'} ,
      {'title': "title three" , 'author' : 'author three' , 'category' : 'history'} ,
       {'title': "title four" , 'author' : 'author four' , 'category' : 'math'} ,
        {'title': "title five" , 'author' : 'author five' , 'category' : 'math'} , 
         {'title': "title six" , 'author' : 'author six' , 'category' : 'math'} , 
]

#############  get method ################

@app.get("/hi") 
async def say_hi():
     return { 'salam' : 'mohsen'}




@app.get("/book") 
async def show_book():
     return BOOKS

################## path param ######################################

# @app.get("/books/{dynamic_param}") 
# async def read_all_books(dynamic_param):
#         return {'dynamic_param' : dynamic_param}


@app.get("/book/{book_title}") 
async def read_book(book_title: str):
        for book in BOOKS: 
            if book.get('title').casefold() == book_title.casefold():
                return book
#################################################################

##### query parameter ########################
# bade ? query param miyad
#for example : 127.0.0.1:8000/books/?category=math

# @app.get('/books/') 
# async def read_category_by_query(category: str):
#             books_to_return = [] 
#             for book in BOOKS: 
#                 if book.get('category').casefold() == category.casefold():
#                     books_to_return.append(book)
#             return books_to_return


###### using path param with query at same time #######



@app.get('/books/{book_author}/') 
async def read_category_by_query(book_author: str, category: str):
    books_to_return = [] 
    for book in BOOKS: 
        if book.get('author').casefold() == book_author.casefold() and \
            book.get('category').casefold() == category.casefold():
             books_to_return.append(book)
    return books_to_return

###################### post method #####################################



########################## put method ####################################

@app.put('/books/update_book') 
async def update_book(updated_book=Body()):
    for i in range(len(BOOKS)): 
        if BOOKS[i].get('title').casefold() == updated_book.get('title').casefold():
            BOOKS[i] = updated_book
