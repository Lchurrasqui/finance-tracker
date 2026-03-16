from sqlalchemy import func
from app.core.database import Base
from sqlalchemy.orm import mapped_column, Mapped, relationship
from datetime import datetime

class User(Base):
    __tablename__ = "users"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(nullable=False, unique=True, index=True)
    password_hash: Mapped[str] = mapped_column(nullable=False)
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())

    accounts = relationship("Account", back_populates="user", cascade="all, delete-orphan")