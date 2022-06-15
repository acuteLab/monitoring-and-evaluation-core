from starlette.config import Config
from starlette.datastructures import URL, Secret
from config.database import DATABASE_URL


config = Config(".env")

TESTING = config("TESTING", cast=bool, default=False)

DATABASE_URL = config(
    "DATABASE_URL",
    cast=str,
)

SECRET_KEY = config(
    "SECRET_KEY",
    cast=str,
)

ALGORITHM = config(
    "ALGORITHM",
    cast=str,
)

FRONTEND_BASE_URL = config("FRONTEND_BASE_URL", cast=str)
LOGIN_URL_PATH = config("LOGIN_URL_PATH", cast=str)

EMAIL_TOKEN_EXPIRE_MINUTES = config("EMAIL_TOKEN_EXPIRE_MINUTES", cast=int)
ACCESS_TOKEN_EXPIRE_MINUTES = config(
    "ACCESS_TOKEN_EXPIRE_MINUTES", cast=int
)
RESET_PASSWORD_TOKEN_TIME = config("RESET_PASSWORD_TOKEN_TIME", cast=int)

SMTP_HOST = config("SMTP_HOST", cast=str)
SMTP_PORT = config("SMTP_PORT", cast=str)
SMTP_USERNAME = config(
    "SMTP_USERNAME", cast=str
)
SMTP_PASSWORD = config("SMTP_PASSWORD", cast=str)

