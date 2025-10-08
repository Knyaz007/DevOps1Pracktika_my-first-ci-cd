# app.py
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    # Потенциальная уязвимость: кривое преобразование данных от пользователя
    try:
        user_id = int(request.args.get('id', 1))
    except ValueError:
        user_id = 1
    return f'<h1>Hello, user #{user_id}!</h1>'

if __name__ == '__main__':
    app.run(debug=True)  # Уязвимость! debug=True нельзя в продакшене



    
# # app.py
# import os
# from flask import Flask, request, escape, abort, make_response

# app = Flask(__name__)

# # Пример базовой конфигурации: в продакшене задавайте через переменные окружения / конфиг-файл
# app.config.from_mapping(
#     DEBUG=False,  # не включаем debug в коде явно
# )

# @app.route('/')
# def hello_world():
#     # Используем request.args.get с type=int — Flask вернёт None, если привести не получится
#     user_id = request.args.get('id', default=None, type=int)

#     # Если параметр отсутствует — берем 1
#     if user_id is None:
#         user_id = 1
#     # Дополнительная валидация: диапазон, чтобы избежать необычных значений
#     if not (1 <= user_id <= 10_000_000):
#         # Можно вернуть 400 Bad Request
#         return make_response('Invalid id parameter', 400)

#     # Всегда экранируем вывод, если формируем HTML вручную
#     safe_user_id = escape(str(user_id))
#     return f'<h1>Hello, user #{safe_user_id}!</h1>'

# # Не включаем debug=True в коде. Для локальной разработки используйте переменные окружения / flask CLI.
# if __name__ == '__main__':
#     # Для локальной отладки можно поднимать flask с FLASK_DEBUG=1 либо через flask run
#     # Но в коде оставляем debug=False (безопаснее).
#     app.run(host='127.0.0.1', port=5000, debug=False)
