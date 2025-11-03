from pydantic import BaseModel

from schemas.asset_schema.schema import Asset


class CreateCheck(BaseModel):
    amount: float
    asset: Asset | str 
    pin_to_user_id: int | None = None
    pin_to_username: str | None = None
    
class DeleteCheck(BaseModel):
    check_id: int