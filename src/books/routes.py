from fastapi import APIRouter, status, HTTPException
from typing import List, Optional
from src.books.book_data import book
from src.books.schemas  import Book, BookUpdateModel  
book_router = APIRouter()




@book_router.get("/", response_model=List[Book])
async def get_all_books():
    return book

@book_router.post("/", status_code=status.HTTP_201_CREATED)
async def create_book(book_data:Book)-> dict:
    new_book = book_data.model_dump()
    book.append(new_book)
    return new_book

@book_router.get("/{book_id}")
async def get_book(book_id: int)->dict:
    for b in book:
        if b["id"] == book_id:
            return b
    raise HTTPException(status_code=404, detail="Book not found")

@book_router.patch("/{book_id}")
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

@book_router.delete("/{book_id}")
async def delete_book(book_id: int):
    for b in book:
        if b["id"] == book_id:
            book.remove(b)
            return {}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
