from pydantic import BaseModel

class Register(BaseModel):

    username:str

    password:str

    role:str


class Login(BaseModel):

    username:str

    password:str


class Relation(BaseModel):

    elder_id:int

    family_id:int

    relation:str