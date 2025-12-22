from fastapi  import FastAPI, status , HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

book = [{
    "id": 1,
    "title": "The Great Gatsby",
    "author": "F. Scott Fitzgerald",
    "year_published": 1925
},{
    "id": 2,
    "title": "To Kill a Mockingbird",
    "author": "Harper Lee",
    "year_published": 1960
}]

class Book(BaseModel):
    id: int
    title: str
    author: str
    year_published: int

class BookUpdateModel(BaseModel):
    title: str | None = None
    author: str | None = None
    year_published: Optional[int] = None

@app.get("/books", response_model=List[Book])
async def get_all_books():
    return book

@app.post("/books", status_code=status.HTTP_201_CREATED)
async def create_book(book_data:Book)-> dict:
    new_book = book_data.model_dump()
    book.append(new_book)
    return new_book

@app.get("/books/{book_id}")
async def get_book(book_id: int)->dict:
    for b in book:
        if b["id"] == book_id:
            return b
    raise HTTPException(status_code=404, detail="Book not found")

@app.patch("/books/{book_id}")
async def update_book(book_id: int, book_data: BookUpdateModel) -> dict:
    for b in book:
        if b["id"] == book_id:
            if book_data.title is not None:
                b["title"] = book_data.title
            if book_data.author is not None:
                b["author"] = book_data.author
            if book_data.year_published !=0 :
                b["year_published"] = book_data.year_published
            return b
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")

@app.delete("/books/{book_id}")
async def delete_book(book_id: int):
    for b in book:
        if b["id"] == book_id:
            book.remove(b)
            return {}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")

