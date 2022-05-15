from fastapi import FastAPI
from fastapi.testclient import TestClient

from routes import (default, auth)

app = FastAPI(prefix='/v1')
app.title = 'Hotels API'
app.version = '0.0.1'
app.description = 'Hotel service app'
app.redoc_url = '/docs'

# Routes
common_prefix = "/api/v1.0"
app.include_router(default.router, tags=["Default routes"], include_in_schema=False)
app.include_router(auth.router, prefix=f"{common_prefix}/auth", tags=["Auth"])

# Testing
TestClient(app)
