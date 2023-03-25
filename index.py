from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    title = "Mascotas Loli"
    return render_template('index.html', title=title)

@app.route('/about')
def about():
    title = "Sobre Nosotros"
    return render_template('about.html', title=title) #render_template se usa para "enlazar" con una vista, en este caso al ir a /about


if __name__ == '__main__':
    app.run(debug=True)#podemos poner debug=True debido que al estar en un entorno de pruebas queremos que se actualice constantemente