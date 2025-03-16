from flask import Flask  # Импортируем Flask

app = Flask(__name__)  # Создаём приложение

@app.route("/")  # Обрабатываем главный маршрут
def home():
    return "Hello, world!"

if __name__ == "__main__":  # Запускаем приложение
    app.run(debug=True)
