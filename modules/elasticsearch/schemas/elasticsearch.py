
from typing import Optional, List

from fastapi import Query
from pydantic import BaseModel


class ElasticsearchBasePayload(BaseModel):
    host: str
    token: Optional[str]


class ElasticsearchBulkEndpointPayload(ElasticsearchBasePayload):
    payload: str


class ElasticsearchCreateIndexPayload(ElasticsearchBasePayload):
    index_name: str
    settings: Optional[object]
    mappings: Optional[object]
    aliases: Optional[object]
