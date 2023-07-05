import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from api.db.schemas import *
from api.db.models import *
from conf.database import *
from fastapi_jwt_auth import AuthJWT
from fastapi_jwt_auth.exceptions import AuthJWTException
from api.rest.permissions import router as permissions_router
from api.rest.roles import router as roles_router
from api.rest.users import router as users_router
from api.rest.user_activity_rest import router as user_activity_router
from dotenv import load_dotenv

# Load the .env file
load_dotenv()

Base.metadata.create_all(bind=engine)

app = FastAPI()

# app.include_router(users_router)
# app.include_router(roles_router)
# app.include_router(permissions_router)
app.include_router(user_activity_router)

@AuthJWT.load_config
def get_config():
    return Settings()

@app.exception_handler(AuthJWTException)
def authjwt_exception_handler(request: Request, exc: AuthJWTException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.message}
    )

if __name__ =='__main__':
    uvicorn.run(app, host="0.0.0.0")