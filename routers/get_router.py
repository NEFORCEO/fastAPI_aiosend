from aiosend import CryptoPay
from fastapi import APIRouter

from aiosend.client import Network

get_router = APIRouter(
    tags=["ИНФОРМАЦИЯ"],
    prefix='/me'
)

@get_router.get("/")
async def get_me(token: str, network:Network):
    cp = CryptoPay(token=token, network=network)
    result = await cp.get_me()
    return {
        "status": 200,
        "payment": result.payment_processing_bot_username,
        "id_app": result.app_id,
        "name_app": result.name
    }