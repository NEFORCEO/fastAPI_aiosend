from pydantic import BaseModel

from schemas.asset_schema.schema import Asset


class Check(BaseModel):
    amount: float
    asset: Asset 
    pin_to_user_id: int | None = None
    pin_to_username: str | None = None