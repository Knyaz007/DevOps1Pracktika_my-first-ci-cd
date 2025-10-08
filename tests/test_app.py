# tests/test_app.py
import sys
import os

# Добавляем корень проекта в sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import DevOps1Pracktika_my_first_ci_cd  # теперь Python видит app.py в корне

def test_hello_world():
    with DevOps1Pracktika_my_first_ci_cd.test_client() as client:
     response = client.get('/')
    assert response.status_code == 200
    assert b'Hello' in response.data