from pydantic import BaseModel

class RelationCreate(BaseModel):
    elder_id:int
    family_id:int
    relation:str