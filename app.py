from flask import Flask
from flask import render_template
from avatar.control import *
from flask_caching import Cache

cache = Cache(config={'CACHE_TYPE': 'filesystem', 'CACHE_DIR': '/tmp'})
app = Flask(__name__, static_folder='static/')
cache.init_app(app)

@app.route('/')
def index():
    return render_template('index.html')


@app.errorhandler(404)
def page_not_found(error):
    return render_template('error.html')
    
@app.route('/planetas')
@cache.cached(timeout=120)
def planetas():
    titulo = "Planetas de Star Wars"
    lista_planetas = obtener_planetas()
    return render_template('planetas.html', name="planetas", lista_planetas = lista_planetas, titulo = titulo)

@app.route('/peliculas')
@cache.cached(timeout=120)
def peliculas():
    titulo = "Peliculas de Star Wars"
    lista_peliculas = obtener_peliculas()
    return render_template('peliculas.html', name="peliculas", lista_peliculas = lista_peliculas, titulo = titulo)

@app.route('/personajes')
@cache.cached(timeout=120)
def personajes():
    titulo = "Personajes de Star Wars"
    lista_personajes = obtener_personajes()
    return render_template('personajes.html', name="personajes", lista_personajes = lista_personajes, titulo = titulo)

if __name__ == "__main__":
    app.run(debug=True)