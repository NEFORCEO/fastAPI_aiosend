from typing import Any
from pydantic import BaseModel



class CheckCreateSchema(BaseModel):
     status: int
     message: str
     link: str  
     check_id: int
     
class DeleteCheckSchema(BaseModel):
     status: int
     message: str 
     result: Any
    
    
    

    