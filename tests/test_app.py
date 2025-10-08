# tests/test_app.py
import pytest

# Вариант 1: если у тебя файл app.py в корне проекта
try:
    from app import app
except Exception:
    # Вариант 2: если твой пакет называется DevOps1Pracktika_my_first_ci_cd
    from DevOps1Pracktika_my_first_ci_cd import app  # fallback

def test_hello_world():
    # Используем тест-клиент самого Flask-приложения
    with app.test_client() as client:
        response = client.get('/')  # GET /
        assert response.status_code == 200
        assert b"Hello, user" in response.data
