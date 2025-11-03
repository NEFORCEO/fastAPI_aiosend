from schemas.invoice_schema.schema import DeleteSchema, Invoice
from aiosend import TESTNET, CryptoPay
from fastapi import APIRouter, Response
from aiosend.exceptions import APIError

from schemas.return_schema.invoice_schema import CreateInvoie, DeleteInvoice



inv_router = APIRouter(
    tags=["СЧЕТА"],
    prefix="/invoice"
)

@inv_router.post("/create/invoice")
async def create_invoice(token: str, param: Invoice) -> CreateInvoie:
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
async def delete_invoice(token: str, invoice: DeleteSchema) -> DeleteInvoice:
    cp = CryptoPay(token=token, network=TESTNET)
    
    result = await cp.delete_invoice(
        invoice_id=invoice.invoice_id
    )
    return {
            "status": 200,
            "message": "Успешно",
            "result": result
            }
