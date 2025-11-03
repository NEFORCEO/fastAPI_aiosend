from typing import Any
from pydantic import BaseModel

class CreateInvoiceSchema(BaseModel):
    status: int
    link: str 
    invoice_id: int
    
class DeleteInvoiceSchema(BaseModel):
    status: int
    message: str 
    result: bool
    
class DeleteInvoiceAllSchema(BaseModel):
    status: int
    message: str 
    result: Any
    

