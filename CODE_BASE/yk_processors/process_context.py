from pydantic import BaseModel

class ProcessContext(BaseModel):
    data: bytes
    headers: dict[str, str]
    id: str