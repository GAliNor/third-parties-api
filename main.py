from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from modules.elasticsearch import router as es_router


CORS_CONFIG = {
    "allow_origins": ["*"],
    "allow_methods": ["*"],
    "allow_headers": ["*"],
    "allow_credentials": True,
}


app = FastAPI()
app.add_middleware(CORSMiddleware, **CORS_CONFIG)


@app.get("/")
def read_root():
    """
    Root endpoint
    """
    return {"Status": "Running"}


app.include_router(es_router.router, prefix='/api')

app.mount("/api", app)
