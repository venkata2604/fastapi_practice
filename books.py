from fastapi import Body, FastAPI
import json

app = FastAPI()

BOOKS = [
    {'title': 'Title One', 'author': 'Author One', 'category': 'science'},
    {'title': 'Title Two', 'author': 'Author Two', 'category': 'science'},
    {'title': 'Title Three', 'author': 'Author Three', 'category': 'history'},
    {'title': 'Title Four', 'author': 'Author Four', 'category': 'math'},
    {'title': 'Title Five', 'author': 'Author Five', 'category': 'math'},
    {'title': 'Title Six', 'author': 'Author Two', 'category': 'math'}
]
# file_path = r"D:\a_my_tutorials\fastapi\fastapi_practice\books_json.json"
# with open(file_path, 'r') as file:
#     BOOKS = json.load(file)
"""
GET
"""
print("BOOKS", BOOKS)


@app.get("/books")
async def read_all_books():
    return BOOKS


# Dynamic Path Parameters
@app.get("/books/{book_title}")
async def read_books(book_title: str):
    for book in BOOKS:
        if book.get("title").casefold() == book_title.casefold():
            return book


# Query Parameters + Path Parameters
@app.get("/books/category")
async def read_category_by_query(category: str):
    """
    Read Category by Query Send Query Parameters through the URL
    """
    books_to_return = []
    for book in BOOKS:
        if book.get('category').casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return


@app.get("/books/authcat/{book_author}")
async def read_author_category_by_query(book_author: str, category: str):
    books_to_return = []
    for book in BOOKS:
        print("Book", book)
        if book.get('author').casefold() == book_author.casefold() and book.get('category').casefold() == category.casefold():
            books_to_return.append(book)

    return books_to_return


"""
POST 
"""


@app.post("/books/create_book")
async def create_book(new_book=Body()):
    BOOKS.append(new_book)

"""
PUT
"""


@app.put("/book/update_book")
async def update_book(updated_book=Body()):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == updated_book.get("title").casefold():
            BOOKS[i] = updated_book


"""
DELETE
"""


@app.delete("/books/delete_book/{book_title}")
async def delete_book(book_title: str):
    for i in range(len(BOOKS)):
        if BOOKS[i].get("title").casefold() == book_title.casefold():
            BOOKS.pop(i)

            break


"""
Assignment
"""


@app.get("/books/{author}")
async def get_all_books1(author: str):
    books_to_return = []
    for i in range(len(BOOKS)):
        if BOOKS[i].get("title").casefold() == author.get("title").casefold():
            books_to_return.append(BOOKS[i])
    return books_to_return
