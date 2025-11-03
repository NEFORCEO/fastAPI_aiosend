from schemas.schema import Invoice
from aiosend import CryptoPay, TESTNET
from fastapi import APIRouter
from aiosend.exceptions import APIError

inv_router = APIRouter(
    tags=["СЧЕТА"],
    prefix="/api"
)

@inv_router.post("/create/invoice")
async def create_invoice(token: str, param: Invoice):
    cp = CryptoPay(token=token, network=TESTNET)
    invoice = await cp.create_invoice(
        amount=param.amount,
        asset=param.asset,
        description=param.description,
        allow_comments=param.allow_comments,
        allow_anonymous=param.allow_anonymous
    )
    return {
        "status": 200,
        "link": invoice.bot_invoice_url,
        "invoice_id": invoice.invoice_id
    }
    
@inv_router.delete("/delete/invoice/")
async def delete_invoice(token: str, invoice_id: int):
    cp = CryptoPay(token=token, network=TESTNET)
    
    result = await cp.delete_invoice(
        invoice_id=invoice_id
    )
    if result.invoice_id:
        return {
            "status": 200,
            "message": "Успешно",
            "result": result
            }
