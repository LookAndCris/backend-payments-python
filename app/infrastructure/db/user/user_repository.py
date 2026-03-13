from sqlalchemy import select
from uuid import uuid4

from app.domain.user.user import User
from app.infrastructure.db.session import AsyncSessionLocal
from .user_models import UserORM


class UserRepository:

    async def create(self, email: str, password_hash: str) -> User:

        async with AsyncSessionLocal() as db:

            user = UserORM(id=str(uuid4()), email=email, password_hash=password_hash)

            db.add(user)

            await db.commit()

            return User(id=user.id, email=user.email, password_hash=user.password_hash)

    async def get_by_email(self, email: str):

        async with AsyncSessionLocal() as db:

            stmt = select(UserORM).where(UserORM.email == email)

            result = await db.execute(stmt)

            user = result.scalar_one_or_none()

            if not user:
                return None

            return User(id=user.id, email=user.email, password_hash=user.password_hash)
