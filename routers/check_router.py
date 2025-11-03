from fastapi import APIRouter, Response

from client.cp_client import get_cp
from schemas.check_schema.schema import CreateCheck, DeleteCheck
from schemas.return_schema.check_schema import CheckCreateSchema, DeleteCheckSchema

check_router = APIRouter(
    tags=["ЧЕКИ"],
    prefix="/check"
)

@check_router.post("/create/check")
async def create_check(token: str, param: CreateCheck) -> CheckCreateSchema:
    cp = get_cp(token=token)
    
    res = await cp.create_check(
        amount=param.amount,
        asset=param.asset,
        pin_to_user_id=param.pin_to_user_id,
        pin_to_username=param.pin_to_username
    )
    
    return {
        "status": 200,
        "message": "Успешно",
        "link": res.bot_check_url,
        "check_id": res.check_id,
    }
    
@check_router.delete("/delete/check")
async def delete_check(token: str, param: DeleteCheck) -> DeleteCheckSchema:
    cp = get_cp(token=token)
    
    res = await cp.delete_check(
        check_id = param.check_id
    )
    return {
        "status": 200,
        "message": "Успешно",
        "result": res
    }
    
@check_router.delete("/delete/check/all")
async def delete_chec_all(token: str) -> DeleteCheckSchema:
    cp = get_cp(token=token)
    res = await cp.delete_all_checks()
    return {
        "status": 200,
        "message": "Успешно",
        "result": res
    }