import uvicorn
from fastapi import FastAPI
from .routers import self, users, guilds, channels, messages

app = FastAPI()


app.include_router(self.router)
app.include_router(users.router)
app.include_router(guilds.router)
app.include_router(channels.router)
app.include_router(messages.router)


def setup():
    uvicorn.run(app, host="0.0.0.0", port=4200)


