from flask import  render_template, request, flash, redirect, url_for
from flask_login import login_user, logout_user,current_user
from sqlalchemy.sql import or_
from app import app ,db , login_manager


from app.models.formulario import CadastroForm, LoginForm, FocoForm
from app.models.tabela import User, Endereco, Foco

@login_manager.user_loader
def load_user(cpf):
    return User.query.filter_by(cpf=cpf).first()

@app.route("/", methods=["GET", "POST"])
@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(cpf=form.cpf.data).first()
        if user.cpf and user.password == form.password.data:
            login_user(user)
            return redirect(url_for("index"))
        else:
            flash("Login Invalido!")
    return render_template("form.html", form=form)



@app.route("/logout", methods=["GET", "POST"])
def logout():
    logout_user()
    return redirect(url_for("login"))

@app.route('/cadastro_user', methods=["GET", "POST"])
def cadastro():
    form = CadastroForm()
    if form.validate_on_submit():
        userRegistered = User.query.filter(or_(User.cpf == form.cpf.data,
                                               User.email == form.email.data)).first()
        if userRegistered is not None:
            flash('Email ou CPF já existe.')
            return render_template("cadastro_user.html", form=form)

        user = User(form.nome.data, form.cpf.data, form.data_nascimento.data, form.email.data, form.password.data)
        db.session.add(user)
        db.session.commit()
        cpf = User.query.filter_by(cpf=form.cpf.data).first()
        endereco = Endereco(form.logradouro.data, form.numero.data,
                            form.complemento.data, form.bairro.data, form.cep.data,
                            form.estado.data, cpf.id)
        db.session.add(endereco)
        db.session.commit()
        flash('Usuario Registrado')
        return redirect(url_for('login'))
    return render_template("cadastro_user.html",
                           form=form)

@app.route("/index", methods=["GET", "POST"])
def index():
    coords = Foco.query.all()
    return render_template("index.html", coords=coords)


@app.route('/foco')
def foco():
  formulario = FocoForm()
  longitude = request.args.get('longitude', type=float)
  latitude = request.args.get('latitude', type=float)
  return render_template("foco.html", longitude=longitude, latitude=latitude, formulario=formulario)


@app.route('/addfoco', methods=['POST', 'GET'])
def addfoco():
    formulario = FocoForm()
    imagem = formulario.foto.data
    img = imagem.read()
    if formulario.validate_on_submit():
        focos = Foco(request.form['latitude'], request.form['longitude'], formulario.data_inicio.data,
                     formulario.data_fim.data, formulario.descricao.data, formulario.foco_existente.data,
                     img, current_user.cpf)
        db.session.add(focos)
        db.session.commit()
        return redirect(url_for('index'))




