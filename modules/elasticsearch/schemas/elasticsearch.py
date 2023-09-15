
from typing import Optional, List

from fastapi import Query
from pydantic import BaseModel


class ElasticsearchBulkEndpointPayload(BaseModel):
    project: str
    action: str
    payload: List[dict]

