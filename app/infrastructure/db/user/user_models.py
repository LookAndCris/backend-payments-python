from sqlalchemy import Column, String
from app.infrastructure.db.session import Base


class UserORM(Base):

    __tablename__ = "users"

    id = Column(String, primary_key=True)
    email = Column(String, unique=True, nullable=False)
    password_hash = Column(String, nullable=False)
