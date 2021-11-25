from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField, SelectField, BooleanField, FileField, TextAreaField
from wtforms.validators import DataRequired


class CadastroForm(FlaskForm):
    nome = StringField('nome')
    cpf = StringField('cpf', validators=[DataRequired('Não pode ser vazio')])
    data_nascimento = StringField('data_nascimento')
    cep = StringField('cep')
    logradouro = StringField('logradouro')
    numero = StringField('numero')
    complemento = StringField('complemento')
    bairro = StringField('bairro')
    estado = SelectField('estado', [DataRequired()],
                        choices=[('Acre', 'AC'),
                                 ('Alagoas', 'AL'),
                                 ('Amapá', 'AP'),
                                 ('Amazonas', 'AM'),
                                 ('Bahia', 'BA'),
                                 ('Ceará', 'CE'),
                                 ('Distrito Federal', 'DF'),
                                 ('Espírito Santo', 'ES'),
                                 ('Goiás', 'GO'),
                                 ('Maranhão', 'MA'),
                                 ('Mato Grosso', 'MT'),
                                 ('Mato Grosso do Sul', 'MS'),
                                 ('Minas Gerais', 'MG'),
                                 ('Pará', 'PA'),
                                 ('Paraíba', 'PB'),
                                 ('Paraná', 'PR'),
                                 ('Pernambuco', 'PE'),
                                 ('Piauí', 'PI'),
                                 ('Rio de Janeiro', 'RJ'),
                                 ('Rio Grande do Norte', 'RN'),
                                 ('Rio Grande do Sul', 'RS'),
                                 ('Rondônia', 'RO'),
                                 ('Roraima', 'RR'),
                                 ('Santa Catarina', 'SC'),
                                 ('São Paulo', 'SP'),
                                 ('Sergipe', 'SE'),
                                 ('Tocantins', 'TO')])
    email = StringField('email', validators=[DataRequired('E-mail não pode ficar vazio')])
    password = PasswordField('password')

class LoginForm(FlaskForm):
    cpf = IntegerField('cpf', validators=[DataRequired('Não pode ser vazio')])
    password = PasswordField('password', validators=[DataRequired('Não pode ser vazio')])

class FocoForm(FlaskForm):
    latitude = StringField('latitude')
    longitude = StringField('longitude')
    data_inicio = StringField('data_inicio')
    data_fim = StringField('data_fim')
    descricao = TextAreaField('descricao')
    foco_existente = BooleanField('foco_existente')
    foto = FileField('foto')

