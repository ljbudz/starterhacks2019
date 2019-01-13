from flask import Flask
import backend

app = Flask(
    __name__,
)

app.register_blueprint(backend.form_api)
app.run(host="localhost", port = 8000)
