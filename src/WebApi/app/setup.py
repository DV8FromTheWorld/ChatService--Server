import uvicorn
from fastapi import FastAPI
from .routers import channels, guilds

app = FastAPI()


app.include_router(channels.router)
app.include_router(guilds.router)


def setup():
    uvicorn.run(app, host="0.0.0.0", port=4200)


