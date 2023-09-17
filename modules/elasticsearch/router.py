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
def bulk(payload: ElasticsearchBulkEndpointPayload):
    return bulk_update(payload)


@router.put("/create-index")
def create(payload: ElasticsearchCreateIndexPayload):
    response = create_index(payload)
    status = response.get('status')if response.get('status') else 201
    return JSONResponse(status_code=status, content=response)

