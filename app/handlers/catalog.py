from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, InputMediaPhoto
from aiogram.filters import Command
from sqlalchemy.ext.asyncio import AsyncSession
from app.config import settings
from app.db.crud import get_products_page
from app.keyboards.catalog import catalog_pagination_kb
import requests

router = Router(name="catalog")


# Оформление данных дял карточки товаров
def _build_product_card(product):
    caption_lines = [f"<b>{product.title}</b>"]
    if product.discount_price is not None and product.discount_price < product.price:
        caption_lines.append(
            f"Цена: <s>{product.price:.2f}</s> -> <b>{product.discount_price:.2f}</b>"
        )
    else:
        caption_lines.append(f"Цена: <b>{product.price:.2f}</b>")
    if product.short_description:
        caption_lines.append("")
        caption_lines.append(product.short_description)
    caption = "\n".join(caption_lines)
    return product.image_url, caption


# Проверка картинки на доступ
async def _show_product_card(
    cb: CallbackQuery, product, page: int, total_pages: int, replace: bool = False
) -> bool:
    image_url, caption = _build_product_card(product)

    async def _try(image: str) -> bool:
        try:
            if replace:
                await cb.message.edit_media(
                    media=InputMediaPhoto(
                        media=image, caption=caption, parse_mode="HTML"
                    ),
                    reply_markup=catalog_pagination_kb(page, total_pages),
                )
            else:
                await cb.message.answer_photo(
                    photo=image,
                    caption=caption,
                    parse_mode="HTML",
                    reply_markup=catalog_pagination_kb(page, total_pages),
                )
            return True
        except Exception:
            return False

    if await _try(image_url):
        return True
    if await _try(settings.PLACEHOLDER_IMAGE):
        return True
    return False


# Обработчик перелистывания страниц каталога
@router.callback_query(F.data.startswith("catalog:page:"))
async def catalog_page_cb(cb: CallbackQuery, session: AsyncSession):
    try:
        page = int(cb.data.split(":")[-1])
    except Exception:
        await cb.answer("Некорректная страница", show_alert=True)
        return

    items, total_pages = await get_products_page(session, page)
    if not items:
        await cb.answer("Нет товаров на этой странице.", show_alert=True)
        return

    product = items[0]
    if not await _show_product_card(cb, product, page, total_pages, replace=True):
        await cb.answer("Не удалось обновить карточку.", show_alert=True)
        return

    await cb.answer()


# Обработчик кнопки "Открыть каталог" из приветственного окна
@router.callback_query(F.data == "open_catalog")
async def open_catalog_cb(cb: CallbackQuery, session: AsyncSession):
    await cb.message.delete()
    page = 1

    items, total_pages = await get_products_page(session, page)
    if not items:
        await cb.message.answer("Каталог пуст. Добавьте товары и попробуйте снова.")
        await cb.answer()
        return

    product = items[0]
    if not await _show_product_card(cb, product, page, total_pages, replace=False):
        await cb.message.answer("Не удалось открыть каталог. Попробуйте позже.")

    await cb.answer()
