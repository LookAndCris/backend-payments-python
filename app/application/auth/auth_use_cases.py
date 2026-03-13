from app.infrastructure.security.password_hasher import (
    hash_password,
    verify_password,
)

from app.infrastructure.security.jwt_service import create_access_token


class RegisterUser:

    def __init__(self, repository):
        self.repository = repository

    async def execute(self, email: str, password: str):

        password_hash = hash_password(password)

        return await self.repository.create(email, password_hash)


class LoginUser:

    def __init__(self, repository):
        self.repository = repository

    async def execute(self, email: str, password: str):

        user = await self.repository.get_by_email(email)

        if not user:
            raise Exception("Invalid credentials")

        if not verify_password(password, user.password_hash):
            raise Exception("Invalid credentials")

        token = create_access_token({"sub": user.email})

        return token
