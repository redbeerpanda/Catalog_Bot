from sqlalchemy import String, Integer, Float, Text
from sqlalchemy.orm import Mapped, mapped_column
from app.db.session import Base

class Product(Base):
   
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)      # ID товара
    title: Mapped[str] = mapped_column(String(200), nullable=False)                     # Названеи товара
    image_url: Mapped[str] = mapped_column(String(500), nullable=False)                 # URL изображения товара
    price: Mapped[float] = mapped_column(Float, nullable=False)                         # Базовая цена
    discount_price: Mapped[float | None] = mapped_column(Float, nullable=True)          # Цена со скидкой (опционально)
    short_description: Mapped[str] = mapped_column(Text, nullable=False, default="")    # Краткое описание товара
