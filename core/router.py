from fastapi import FastAPI
from fa_learn_app.routers import products

def set_riuters(app :FastAPI):
    app.include_router(product.router,prefix = "", tags=['products'])