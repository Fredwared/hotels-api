from fastapi import FastAPI

from routes import (auth)

app = FastAPI()
app.title = 'Hotels API'
app.version = '0.0.1'
app.description = 'Hotel service app'
app.redoc_url = '/docs'

app.include_router(auth.router)
