from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy import text
import ssl
from src.config import config

# Create SSL context for Neon
ssl_context = ssl.create_default_context()

# Async engine with asyncpg
engine = create_async_engine(
    config.DATABASE_URL,          # must be postgresql+asyncpg://...
    echo=True,
    connect_args={"ssl": ssl_context}
)

# Initialize DB
async def init_db():
    async with engine.begin() as conn:
        statement = text("SELECT 'hello';")
        result = await conn.execute(statement)
        print(result.all())