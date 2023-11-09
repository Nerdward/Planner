import asyncio
import httpx
import pytest

from main import app
from database.connection import TestSettings
from models.events import Event
from models.users import User

@pytest.fixture(scope="session")
def event_loop():
    loop = asyncio.get_event_loop()
    yield loop
    loop.close()

async def init_db():
    test_settings = TestSettings()

    await test_settings.initialize_database()

@pytest.fixture(scope="session")
async def default_client():
    """
    Returns an instance of our application run asynchronously through httpx
    """
    # Initialize database
    await init_db()
    async with httpx.AsyncClient(app=app, base_url="http://app") as client:
        yield client
        # Clean up resources
        await Event.find_all().delete()
        await User.find_all().delete()