from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from config import get_settings
from .schemas.elasticsearch import ElasticsearchBulkEndpointPayload, ElasticsearchCreateIndexPayload
from .service import bulk_update, create_index


router = APIRouter(
    tags=["base-route"],
    prefix="/elasticsearch"
)


@router.post("/bulk")
async def bulk(payload: ElasticsearchBulkEndpointPayload):
    return await bulk_update(payload)


@router.put("/create-index")
def create(payload: ElasticsearchCreateIndexPayload):
    response = create_index(payload)
    return JSONResponse(status_code=response.get('status'), content=response)

