from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column

from .session import Base


class PaymentORM(Base):
    __tablename__ = "payments"

    id: Mapped[str] = mapped_column(String, primary_key=True)
    amount: Mapped[int] = mapped_column(Integer, nullable=False)
    currency: Mapped[str] = mapped_column(String(10), nullable=False)
    description: Mapped[str] = mapped_column(String(255), nullable=False)
    status: Mapped[str] = mapped_column(String(20), nullable=False)
    idempotency_key: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
        unique=True,  # idempotencia real
    )