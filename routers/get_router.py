from schemas.schema import Invoice
from aiosend import CryptoPay, TESTNET
from fastapi import APIRouter

get_router = APIRouter(
    tags=["ИНФОРМАЦИЯ"],
    prefix='/me'
)

@get_router.get("/")
async def get_me(token: str):
    cp = CryptoPay(token=token, network=TESTNET)
    result = await cp.get_me()
    return {
        "status": 200,
        "payment": result.payment_processing_bot_username,
        "id_app": result.app_id,
        "name_app": result.name
    }