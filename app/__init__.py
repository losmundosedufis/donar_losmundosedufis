from flask import Flask
import os

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "clave_de_desarrollo")

from app import routes