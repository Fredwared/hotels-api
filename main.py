from fastapi import FastAPI
from fastapi.testclient import TestClient

from routes import (auth)

app = FastAPI()
app.title = 'Hotels API'
app.version = '0.0.1'
app.description = 'Hotel service app'
app.redoc_url = '/docs'

# Routes
app.include_router(auth.router)

# Testing
TestClient(app)
