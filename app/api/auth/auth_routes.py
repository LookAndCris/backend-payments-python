from fastapi import APIRouter, HTTPException

from app.api.auth.auth_schemas import LoginRequest, TokenResponse
from app.infrastructure.security.jwt_service import create_access_token
from app.infrastructure.security.password_hasher import verify_password

router = APIRouter(prefix="/auth", tags=["auth"])


# usuario mock temporal
FAKE_USER = {
    "email": "admin@example.com",
    "password_hash": "$2b$12$RdIqwUvzZxCHMbHsE4mBJe01iDcxHUa3wF2HmoDA63cojxUdXhG0q",
}


@router.post("/login", response_model=TokenResponse)
async def login(request: LoginRequest):

    if request.email != FAKE_USER["email"]:
        raise HTTPException(status_code=401)

    if not verify_password(request.password, FAKE_USER["password_hash"]):
        raise HTTPException(status_code=401)

    token = create_access_token({"sub": request.email})

    return TokenResponse(access_token=token)
