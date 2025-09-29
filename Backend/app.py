from flask import Flask
from models import db
from models.member import Member
import os

app = Flask(__name__)

# Correct absolute path for database
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(BASE_DIR, '../database/dms.db')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_path
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
db.init_app(app)

# Basic route
@app.route('/')
def home():
    return "Hello, DMS Project!"

if __name__ == "__main__":
    app.run(debug=True)
