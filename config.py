from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    vllm_base_url: str = "http://localhost:8000/v1"
    model_name: str = "speakleash/Bielik-4.5B-v3.0-Instruct"
    openai_api_key: str = "EMPTY"

    api_host: str = "0.0.0.0"
    api_port: int = 8080


settings = Settings()
