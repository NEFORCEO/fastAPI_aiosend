from client.cp_client import get_cp
from schemas.invoice_schema.schema import DeleteSchema, Invoice
from fastapi import APIRouter, Response
from aiosend.exceptions import APIError

from schemas.return_schema.invoice_schema import CreateInvoiceSchema, DeleteInvoiceAllSchema, DeleteInvoiceSchema



inv_router = APIRouter(
    tags=["СЧЕТА"],
    prefix="/invoice"
)

@inv_router.post("/create/invoice")
async def create_invoice(token: str, param: Invoice) -> CreateInvoiceSchema:
    cp = get_cp(token=token)
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
async def delete_invoice(token: str, invoice: DeleteSchema) -> DeleteInvoiceSchema:
    cp = get_cp(token=token)
    
    result = await cp.delete_invoice(
        invoice_id=invoice.invoice_id
    )
    return {
            "status": 200,
            "message": "Успешно",
            "result": result
            }
    
@inv_router.delete("/delete/invoice/all")
async def delete_invoice_all(token: str) -> DeleteInvoiceAllSchema:
    cp = get_cp(token=token)
    res = await cp.delete_all_invoices()
    return {
        "status": 200,
        "message": "Успешно",
        "result": res
    }
