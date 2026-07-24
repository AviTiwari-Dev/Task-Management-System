""" """

from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).resolve().parent.parent.parent


class Settings(BaseSettings):
    """ """

    ENVIRONMENT: str
    APP_VERSION: str
    API_VERSION: int

    model_config = SettingsConfigDict(
        env_file=BASE_DIR / ".env",
        extra="ignore",
    )


auth_api_configuration_variables = Settings()
