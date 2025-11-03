from typing import Any
from aiosend.types import Balance, Currency
from pydantic import BaseModel

class GetApp(BaseModel):
    status: int
    payment: str 
    id_app: int
    name_app: str

class Found(BaseModel):
    status: int
    message: str

class GetBalance(Found):
    result: Any
    
class GetCurrencies(Found):
    result: list[Currency]
    

class GetExchange_rates(Found):
    result: Any
