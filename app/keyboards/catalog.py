from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def catalog_pagination_kb(current: int, total: int, show_next: bool = True) -> InlineKeyboardMarkup:
    prev_page = max(1, current - 1)
    next_page = min(total, current + 1)

    buttons = []
    if current > 1:
        buttons.append(
            InlineKeyboardButton(
                text="Назад", callback_data=f"catalog:page:{prev_page}"
            )
        )
    buttons.append(
        InlineKeyboardButton(text=f"Стр. {current}/{total}", callback_data="noop")
    )
    if show_next and current < total:
        buttons.append(
            InlineKeyboardButton(
                text="Дальше", callback_data=f"catalog:page:{next_page}"
            )
        )

    return InlineKeyboardMarkup(inline_keyboard=[buttons])


def welcome_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Открыть каталог", callback_data="open_catalog")]
        ]
    )