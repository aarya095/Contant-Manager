from sqlalchemy import ForeignKey
from typing import List

from sqlalchemy.schema import CreateTable
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

from app.database.database import engine

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "users"

    user_id : Mapped[int] = mapped_column(primary_key=True)
    user_name : Mapped[str] = mapped_column(unique=True)
    contacts : Mapped["Contact"] = relationship(back_populates = "users")

class Contact(Base):
    __tablename__ = "contacts"

    contact_id : Mapped[int] = mapped_column(primary_key=True)
    user_id : Mapped[int] = mapped_column(ForeignKey("users.user_id"))
    contact_name : Mapped[str] = mapped_column(unique=True)
    contact_number : Mapped[int] = mapped_column(unique=True)

    users : Mapped["User"] = relationship(back_populates="contacts")

if __name__ == '__main__':
    Base.metadata.create_all(engine)