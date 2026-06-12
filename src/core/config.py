from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "Ticket Managment"
    DEBUG: bool = True
    DATABASE_URL: str = "sqlite:///./database.db"

settings = Settings()