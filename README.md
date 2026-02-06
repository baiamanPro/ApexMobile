# ApexMobile — Django проект

Учебный Django-проект с каталогом товаров и страницами просмотра продукции.

## 📁 Структура проекта

```

woork228/
│
├── Technik/                 # Конфигурация Django проекта
│   ├── **init**.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── main/                    # Основное приложение
│   ├── migrations/
│   ├── **init**.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── templates/               # HTML шаблоны
│   ├── main.html
│   ├── products.html
│   └── product_detail.html
│
├── static/                  # Статические файлы
│   ├── style.css
│   └── main.js
│
├── media/                   # Медиа-файлы
│   └── products/
│
├── db.sqlite3               # База данных SQLite
├── manage.py                # Управление Django проектом
└── .venv/                   # Виртуальное окружение

````

## 🚀 Возможности

- Вывод списка товаров  
- Страница детального просмотра товара  
- Использование шаблонов Django  
- Подключены CSS и JavaScript  
- Поддержка изображений через `media/`

## ⚙️ Установка и запуск

1. Клонируй репозиторий:
```bash
git clone https://github.com/username/technik.git
cd technik
````

2. Установи зависимости:

```bash
pip install django
```

3. Примени миграции:

```bash
python manage.py migrate
```

4. Запусти сервер:

```bash
python manage.py runserver
```

5. Открой в браузере:

```
http://127.0.0.1:8000/
```

## 🛠 Используемые технологии

* Python
* Django
* HTML / CSS
* JavaScript
* SQLite

## 📌 Примечания

* Изображения товаров хранятся в `media/products/`
* Шаблоны лежат в папке `templates/`
* Основная логика реализована в приложении `main`

## 👤 Автор

**baiamanPro**
Учебный проект по Django

```
