
from fastapi import APIRouter

from client.cp_client import get_cp
from schemas.return_schema.get_schema import GetAppSchema, GetBalanceSchema, GetCurrenciesSchema, GetExchange_ratesSchema



get_router = APIRouter(
    tags=["ИНФОРМАЦИЯ"],
    prefix='/get'
)

@get_router.get("/app")
async def get_me(token: str) -> GetAppSchema:
    cp = get_cp(token=token)
    result = await cp.get_me()
    return {
        "status": 200,
        "payment": result.payment_processing_bot_username,
        "id_app": result.app_id,
        "name_app": result.name
    }
    
@get_router.get("/balance")
async def get_balance(token: str) -> GetBalanceSchema:
    cp = get_cp(token=token)
    
    get_balance = await cp.get_balance()
    return {
        "status": 200,
        "message": "Успешно",
        "result": get_balance
    }

@get_router.get('/currencies')
async def get_currencies(token: str) -> GetCurrenciesSchema:
    cp = get_cp(token=token)
    
    res = await cp.get_currencies()
    return {
        "status": 200,
        "message": "Успешно",
        "result": res
    }
    
@get_router.get("/exchange_rates")
async def exchange_rates(token: str) -> GetExchange_ratesSchema:
    cp = get_cp(token=token)
    
    res = await cp.get_exchange_rates()
    return {
        "status": 200,
        "message": "Успешно",
        "result": res
    }