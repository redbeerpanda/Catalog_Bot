# Telegram Каталог товаров

Этот проект — простой Telegram-бот-каталог на aiogram v3 + SQLite.
Пользователь может листать товары с фото, описанием и ценой прямо в чате.

---

1. **Клонируйте репозиторий и перейдите в папку проекта:**

2. **Создайте и активируйте виртуальное окружение:**
   ```bash
   python -m venv .venv
   # Windows:
   .venv\Scripts\activate
   # Linux/Mac:
   source .venv/bin/activate
   ```

3. **Установите зависимости:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Настройте переменные окружения:**
   ```bash
   Откройте .env и укажите свой BOT_TOKEN
   ```

5. **Заполните базу тестовыми товарами:**
   ```bash
   python -m scripts.seed_db
   ```

6. **Запустите бота:**
   ```bash
   python -m app.main
   ```
---
