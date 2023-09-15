from pydantic_settings import BaseSettings
from functools import lru_cache
from decouple import config


class Settings(BaseSettings):
    """
        wraps all project settings variables
    """
    TENDER_ES_HOST: str = config('TENDER_ES_HOST')
    TENDER_TOKEN: str = config('TENDER_TOKEN')
    TENDER_DATA_INDEX_NAME: str = config('TENDER_DATA_INDEX_NAME')


@lru_cache()
def get_settings():
    """
        return cached setting class instance
    """
    return Settings()

