from pydantic import BaseModel

class MedicinePlanCreate(BaseModel):
    user_id: int
    medicine_name: str
    time: str