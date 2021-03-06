"""empty message

Revision ID: 611bfe501573
Revises: 
Create Date: 2020-05-13 00:47:33.926383

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '611bfe501573'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('usuarios',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(length=80), nullable=False),
    sa.Column('cpf', sa.Integer(), nullable=False),
    sa.Column('data_nascimento', sa.String(length=10), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('password', sa.String(length=6), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('cpf'),
    sa.UniqueConstraint('email')
    )
    op.create_table('enderecos',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('logradouro', sa.String(length=100), nullable=True),
    sa.Column('numero', sa.String(length=80), nullable=True),
    sa.Column('bairro', sa.String(length=80), nullable=True),
    sa.Column('estado', sa.String(length=80), nullable=True),
    sa.Column('cep', sa.String(length=8), nullable=False),
    sa.Column('usuario_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['usuario_id'], ['usuarios.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('focos',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('latitude', sa.Text(), nullable=True),
    sa.Column('longitude', sa.Text(), nullable=True),
    sa.Column('data_inicio', sa.String(length=10), nullable=False),
    sa.Column('data_fim', sa.String(length=10), nullable=True),
    sa.Column('descricao', sa.Text(), nullable=True),
    sa.Column('foco_existente', sa.Boolean(), nullable=True),
    sa.Column('foto', sa.Binary(), nullable=True),
    sa.Column('usuario_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['usuario_id'], ['usuarios.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('focos')
    op.drop_table('enderecos')
    op.drop_table('usuarios')
    # ### end Alembic commands ###
