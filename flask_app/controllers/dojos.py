from flask_app import app, render_template, redirect, request
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja


@app.route('/dojos')
def dojos():
    dojos = Dojo.get_all()
    print(dojos)
    return render_template('dojos.html', dojos = dojos)

@app.route('/add', methods=['post'])
def add():
    Dojo.save(request.form)
    return redirect('/dojos')

@app.route('/ninjas')
def new():
    dojos = Dojo.get_all()
    ninjas = Ninja.get_all_ninjas()
    return render_template('ninjas.html', dojos = dojos, ninjas = ninjas)

@app.route('/create', methods=['post'])
def create():
    Ninja.save(request.form)
    return redirect('/ninjas')

@app.route('/dojos/<int:id>')
def show(id):
    dojos = Dojo.join_with_ninjas(id)
    return render_template('show.html', dojos = dojos)

