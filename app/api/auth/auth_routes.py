from fastapi import APIRouter

from app.infrastructure.db.user.user_repository import UserRepository
from app.application.auth.auth_use_cases import RegisterUser, LoginUser

from .auth_schemas import RegisterRequest, LoginRequest, TokenResponse


router = APIRouter(prefix="/auth", tags=["auth"])

repository = UserRepository()


@router.post("/register")
async def register(request: RegisterRequest):

    use_case = RegisterUser(repository)

    user = await use_case.execute(request.email, request.password)

    return user


@router.post("/login", response_model=TokenResponse)
async def login(request: LoginRequest):

    use_case = LoginUser(repository)

    token = await use_case.execute(request.email, request.password)

    return TokenResponse(access_token=token)
