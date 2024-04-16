from flask import render_template, request, redirect, url_for
from models.database import db, Livros

leitores = []
livros = []

def init_app(app):
    @app.route('/')
    def home():
        return render_template('index.html')
    
    @app.route('/livros', methods=['GET', 'POST'])
    def books():
        
        if request.method == 'POST':
            if request.form.get('leitor'):
                leitores.append(request.form.get('leitor'))
                
            if request.form.get('livro'):
                livros.append(request.form.get('livro'))
            
        return render_template('livros.html', leitores=leitores, livros=livros)
    
    @app.route('/cadLivros', methods=['GET', 'POST'])
    def cadBook():
        livros = Livros.query.all()
        
        if request.method == 'POST':
            newlivro = Livros(request.form['titulo'], request.form['ano'], request.form['autor'])
            db.session.add(newlivro)
            db.session.commit()
            
            return redirect(url_for('cadBook'))
        
        return render_template('cadLivros.html', livros=livros)
    
    @app.route('/cadLivros/delete/<int:id>', methods=['GET', 'POST'])
    def deleteBook(id):
        livro = Livros.query.get(id)
        db.session.delete(livro)
        db.session.commit()
        
        return redirect(url_for('cadBook'))
    
    @app.route('/editBook/<int:id>', methods=['GET', 'POST'])
    def editBook(id):
        l = Livros.query.get(id)

        if request.method == 'POST':
            l.titulo = request.form['titulo']
            l.ano = request.form['ano']
            l.autor = request.form['autor']
            db.session.commit()
            return redirect(url_for('cadBook'))

        return render_template('editlivro.html', l=l)