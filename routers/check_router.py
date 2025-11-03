from fastapi import APIRouter, Response
from aiosend import CryptoPay
from aiosend.client import Network

check_router = APIRouter(
    tags=["ЧЕКИ"],
    prefix="/check"
)
