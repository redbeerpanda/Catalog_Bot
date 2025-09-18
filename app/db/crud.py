from typing import Sequence, Tuple
from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.models import Product


async def get_products_page(
    session: AsyncSession, page: int
) -> Tuple[Sequence[Product], int]:
    """
    Возвращает список товаров для указанной страницы и общее количество страниц.

    Аргументы:
        session (AsyncSession): Асинхронная сессия.
        page (int): Номер страницы (начиная с 1).

    Возвращает:
        Tuple[Sequence[Product], int]: Кортеж, содержащий список товаров на странице и общее число страниц.
    """
    page = max(1, page)
    total_stmt = select(func.count(Product.id))
    total = (await session.execute(total_stmt)).scalar_one()
    total_pages = max(1, total)

    offset = (page - 1)
    stmt = select(Product).order_by(Product.id.asc()).offset(offset).limit(1)
    result = await session.execute(stmt)
    items: Sequence[Product] = result.scalars().all()
    return items, total_pages
