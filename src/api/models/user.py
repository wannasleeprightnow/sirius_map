import bcrypt
from sqlalchemy import LargeBinary, String
from sqlalchemy.orm import Mapped, mapped_column

from db.database import Base


class UserModel(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(50), unique=True)
    password: Mapped[str] = mapped_column(String(25))
    name: Mapped[str] = mapped_column(String(25))
    phone_number: Mapped[str] = mapped_column(unique=True)
    user_type: Mapped[str] = mapped_column(String(), default="user")
    user_image: Mapped[bytes | None] = mapped_column(LargeBinary)

    @staticmethod
    def hash_password(unhashed_password: str):
        salt = bcrypt.gensalt()
        return bcrypt.hashpw(unhashed_password.encode("utf-8"), salt)

    @staticmethod
    def check_password(first_password, second_password):
        return bcrypt.checkpw(
            first_password.encode("utf-8"),
            second_password,
            )

    def __repr__(self):
        return f"{self.id=} {self.username=} {self.password=} \
            {self.name=} {self.phone_number=} {self.user_type=} \
            self.user_image"
