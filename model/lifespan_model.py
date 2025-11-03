from contextlib import asynccontextmanager

from fastapi import FastAPI


@asynccontextmanager
async def start_app(app: FastAPI):
    print("Приложение запущено")
    yield
    print("Приложение завершило свою работу")