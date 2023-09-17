from fastapi import APIRouter, status
from config import get_settings
from .schemas.elasticsearch import ElasticsearchBulkEndpointPayload, ElasticsearchCreateIndexPayload
from .service import bulk_update, create_index
from .utils.helpers import format_elasticsearch_response


router = APIRouter(
    tags=["elasticsearch"],
    prefix="/elasticsearch"
)


@router.post("/bulk")
def bulk(payload: ElasticsearchBulkEndpointPayload):
    response = bulk_update(payload)
    return format_elasticsearch_response(response)


@router.put("/create-index")
def create(payload: ElasticsearchCreateIndexPayload):
    response = create_index(payload)
    return format_elasticsearch_response(response)
