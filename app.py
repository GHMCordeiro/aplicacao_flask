from flask import Flask, render_template
from controllers import routes
import os
from models.database import db

app = Flask(__name__, template_folder='views')

routes.init_app(app)

dir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(dir, 'models/livros.sqlite3')

if __name__ == '__main__': 
    # Verifica se o banco já existe, caso contrário, ele criará #
    db.init_app(app=app)
    with app.test_request_context():
        db.create_all()
    # Rodando a aplicação no localhost, porta 5000, modo debug ativado
    app.run(host='localhost', port=5000, debug=True)