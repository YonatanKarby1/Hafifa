from pydantic import BaseModel

class ProcessResult(BaseModel):
    data: bytes
    header: dict[str, str]
    status: str