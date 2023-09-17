from pydantic_settings import BaseSettings
from functools import lru_cache
from decouple import config


class Settings(BaseSettings):
    """
        wraps all project settings variables
    """
    ES_HOST: str = config('ES_HOST')
    TOKEN: str = config('TOKEN')
    DATA_INDEX_NAME: str = config('DATA_INDEX_NAME')


@lru_cache()
def get_settings():
    """
        return cached setting class instance
    """
    return Settings()

