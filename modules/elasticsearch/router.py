from fastapi import APIRouter, status
from config import get_settings
from .schemas.elasticsearch import ElasticsearchBulkEndpointPayload
from .service import bulk_update


router = APIRouter(
    tags=["base-route"],
    prefix="/elasticsearch"
)


@router.post("/bulk")
async def bulk(payload: ElasticsearchBulkEndpointPayload):
    return await bulk_update(payload)


@router.post("/create-index")
async def create_index(payload: ElasticsearchBulkEndpointPayload):
    return await create_index(payload)

