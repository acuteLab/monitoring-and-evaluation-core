import uvicorn
from fastapi import Depends, FastAPI, Header, HTTPException
from authentication import user_api, authenticate
from dependencies import create_tables
from fastapi.middleware.cors import CORSMiddleware

create_tables()

app = FastAPI(title="Authentication Service", docs_url="/docs", redoc_url=None)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)


async def get_token_header(token: str = Header(...)):
    if  token != "fake-super-secret-token":
        raise HTTPException(status_code=400, detail="X-Token header invalid")


app.include_router(authenticate.router, tags=["Authentications"])
app.include_router(
    user_api.router,
    tags=["User"],
)
