from pydantic import BaseModel

class CreateInvoie(BaseModel):
    status: int
    link: str 
    invoice_id: int
    
class DeleteInvoice(BaseModel):
    status: int
    message: str 
    result: bool
