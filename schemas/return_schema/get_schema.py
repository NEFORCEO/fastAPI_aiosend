from typing import Any
from aiosend.types import Balance, Currency
from pydantic import BaseModel

class GetAppSchema(BaseModel):
    status: int
    payment: str 
    id_app: int
    name_app: str

class FoundSchema(BaseModel):
    status: int
    message: str

class GetBalanceSchema(FoundSchema):
    result: Any
    
class GetCurrenciesSchema(FoundSchema):
    result: list[Currency]
    

class GetExchange_ratesSchema(FoundSchema):
    result: Any
