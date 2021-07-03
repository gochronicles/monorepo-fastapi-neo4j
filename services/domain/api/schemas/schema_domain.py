from pydantic import BaseModel


class Domain(BaseModel):
    name: str
    status: bool = False
    classified: bool = False


class DomainUpdate(BaseModel):
    domain_id: str
    name: str
    status: bool = False
    classified: bool = False
