import asyncio
from app.db.session import SessionLocal, engine, Base
from app.db.models import Product

SAMPLE_PRODUCTS = [
    {
        "title": "Фигурка Геральта из Ривии (The Witcher 3)",
        "image_url": "https://cdn1.ozone.ru/s3/multimedia-5/6348531089.jpg",
        "price": 49.99,
        "discount_price": 39.99,
        "short_description": "Высота: 24 см. Официальная фигурка Геральта из Ривии от Dark Horse. Детализированная покраска, подставка в комплекте.",
    },
    {
        "title": "Фигурка Йеннифер из Венгерберга (The Witcher 3)",
        "image_url": "https://wantshop.ru/media/tmp/ee9ab12663a116103d9b853c877d63a2.jpeg",
        "price": 44.99,
        "discount_price": 36.99,
        "short_description": "Высота: 20 см. Оригинальная фигурка Йеннифер от Dark Horse. Отличная детализация, устойчивая подставка.",
    },
    {
        "title": "Фигурка Цири (The Witcher 3)",
        "image_url": "https://kemerovo.sidex.ru/images_offers/3888/3888709/figyrka_dark_horse_the_witcher_3_wild_hunt__ciri_1.jpg",
        "price": 44.99,
        "discount_price": 34.99,
        "short_description": "Высота: 20 см. Фигурка Цири с мечом, официальная коллекция. Качественная покраска, подставка.",
    },
    {
        "title": "Фигурка Трисс Меригольд (The Witcher 3)",
        "image_url": "https://avatars.mds.yandex.net/get-marketpic/5591688/picb91610b82e4a0c0ddf2a4dc3f5557d37/orig",
        "price": 44.99,
        "discount_price": 35.99,
        "short_description": "Высота: 20 см. Фигурка Трисс из официальной серии. Яркая детализация, устойчивая подставка.",
    },
    {
        "title": "Фигурка Эредина (The Witcher 3)",
        "image_url": "https://avatars.mds.yandex.net/get-marketpic/6052030/pica2af664abbe68540d39aaa1221b312cf/orig",
        "price": 54.99,
        "discount_price": 44.99,
        "short_description": "Высота: 24 см. Фигурка Эредина, Короля Дикой Охоты. Детализированная броня, подставка.",
    },
    {
        "title": "Фигурка Весемира (The Witcher 3)",
        "image_url": "https://m.media-amazon.com/images/I/61aVGTNiISL.jpg",
        "price": 49.99,
        "discount_price": 39.99,
        "short_description": "Высота: 23 см. Официальная фигурка Весемира. Отличная детализация, подставка в комплекте.",
    },
]


async def run():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    async with SessionLocal() as session:
        # Очистка и сидинг
        await session.execute(Product.__table__.delete())
        session.add_all([Product(**p) for p in SAMPLE_PRODUCTS])
        await session.commit()
    print("Seed complete.")


if __name__ == "__main__":
    asyncio.run(run())
