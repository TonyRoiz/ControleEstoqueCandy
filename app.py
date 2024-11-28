from ESTOQUECANDY import app, db
from ESTOQUECANDY.utils import criacao_usuario_default

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        criacao_usuario_default()
    
    app.run(host='localhost', port=5000)