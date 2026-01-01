from fastapi import FastAPI
from src.books.routes import book_router
from contextlib import asynccontextmanager
from src.db.main import init_db

version = "v1"

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup actions
    print("Starting up...")
    await init_db()
    yield
    # Shutdown actions
    print("Shutting down...")

app = FastAPI(
  title="Bookly",
  version=version,
  description="A RESTful API for a book review.",
  lifespan=lifespan
)

app.include_router(book_router, prefix=f"/api/{version}/books")