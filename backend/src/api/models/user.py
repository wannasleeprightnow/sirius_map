from sqlalchemy import LargeBinary, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class UserModel(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(50), unique=True)
    password: Mapped[str] = mapped_column(String(25))
    name: Mapped[str] = mapped_column(String(25))
    phone_number: Mapped[str] = mapped_column(unique=True)
    user_type: Mapped[str]
    user_image: Mapped[bytes | None] = mapped_column(LargeBinary)

    def __repr__(self):
        return f"{self.id=} {self.username=} {self.password=} \
            {self.name=} {self.phone_number=} {self.user_type=} \
            self.user_image"
