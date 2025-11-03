from pydantic import BaseModel
from schemas.asset_schema.schema import Asset

    
class Invoice(BaseModel):
    amount: float
    asset: Asset
    description: str | None = None
    allow_comments: bool | None = None 
    allow_anonymous: bool | None = None 
    expires_in: int | None = None
    