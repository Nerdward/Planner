from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.users import user_router
from routes.events import event_router
from database.connection import Settings

import uvicorn

app = FastAPI()

# register origins
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

settings = Settings()
@app.on_event("startup")
async def start_db():
    await settings.initialize_database()


app.include_router(user_router, prefix="/user")
app.include_router(event_router, prefix="/event")

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)