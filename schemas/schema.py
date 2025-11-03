from pydantic import BaseModel


class Invoice(BaseModel):
    amount: float
    asset: str | None
    description: str | None 
    allow_comments: bool | None
    allow_anonymous: bool | None 
    expires_in: int | None 