from app import app

if __name__ != "__main__":
    gunicorn_app = app
else:
    app.run(debug=True)