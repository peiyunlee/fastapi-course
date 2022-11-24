from pydantic import BaseModel, Field

# --------RESPONSE


class EventResponseSchema(BaseModel):
    event_id: int = Field(default=None, description="事件編號")
    num_terminals: int = Field(..., description='端點數')
    class Config():
        orm_mode = True