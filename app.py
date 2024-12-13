from flask import Flask
from models import db
from routes import blueprints 


app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/health_center'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

for blueprint in blueprints:
    app.register_blueprint(blueprint)

if __name__ == '__main__':
    app.run(debug=True)
