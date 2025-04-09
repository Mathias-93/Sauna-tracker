from flask import Flask
from flask_cors import CORS
from models import db

app = Flask(__name__)
CORS(app)

# SQLite database config
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return "Hello Sauna World!"


if __name__ == "__main__":
    app.run(debug=True)
