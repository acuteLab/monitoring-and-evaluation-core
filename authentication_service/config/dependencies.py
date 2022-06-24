from authentication.models import Base
from database import engine


def create_tables():
    return Base.metadata.create_all(engine)
