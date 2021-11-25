from app import db

class User(db.Model):
    __tablename__ = "usuarios"
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80), nullable=False)
    cpf = db.Column(db.String, unique=True, nullable=False)
    data_nascimento = db.Column(db.String(10))
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(6), nullable=False)

    @property
    def is_authenticated(self):
        return True
    @property
    def is_active(self):
        return True
    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.cpf)

    def __init__(self, nome, cpf, data_nascimento, email, password):
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento
        self.email = email
        self.password = password


    def __repr__(self):
        return "<User %r>" % (self.cpf)





class Endereco(db.Model):
    __tablename__ = "enderecos"

    id = db.Column(db.Integer, primary_key=True)
    logradouro = db.Column(db.String(100))
    numero = db.Column(db.String(80))
    complemento = (db.String(80))
    bairro = db.Column(db.String(80))
    estado = db.Column(db.String(80))
    cep = db.Column(db.String(8), nullable=False)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'))

    user = db.relationship('User', foreign_keys=usuario_id)

    def __init__(self, logradouro, numero, complemento, bairro, estado, cep, usuario_id):
        self.logradouro = logradouro
        self.numero = numero
        self.complemento = complemento
        self.bairro = bairro
        self.estado = estado
        self.cep = cep
        self.usuario_id = usuario_id


    def __repr__(self):
        return "<Endereco %r>" % self.id


class Foco(db.Model):
    __tablename__ = "focos"

    id = db.Column(db.Integer, primary_key=True)
    latitude = db.Column(db.Text)
    longitude = db.Column(db.Text)
    data_inicio = db.Column(db.String(10), nullable = False)
    data_fim = db.Column(db.String(10))
    descricao = db.Column(db.Text)
    foco_existente = db.Column(db.Boolean)
    foto = db.Column(db.Binary)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'))


    user = db.relationship('User', foreign_keys=usuario_id)

    def __init__(self,latitude,longitude, data_inicio, data_fim, descricao, foco_existente, foto, usuario_id):
        self.latitude = latitude
        self.longitude = longitude
        self.data_inicio = data_inicio
        self.data_fim = data_fim
        self.descricao = descricao
        self.foco_existente = foco_existente
        self.foto = foto
        self.usuario_id = usuario_id

    def __repr__(self):
        return "<Foco %r>" % self.id
