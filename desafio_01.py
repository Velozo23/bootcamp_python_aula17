from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.exc import SQLAlchemyError


Base = declarative_base()

class Fornecedor(Base):
    __tablename__ = 'fornecedores'
    id = Column(Integer, primary_key=True)
    nome = Column(String(50), nullable=False)
    telefone = Column(String(20))
    email = Column(String(50))
    endereco = Column(String(100))

class Produto(Base):
    __tablename__ = 'produtos'
    id = Column(Integer, primary_key=True)
    nome = Column(String(50), nullable=False)
    descricao = Column(String(200))
    preco = Column(Integer)
    fornecedor_id = Column(Integer, ForeignKey('fornecedores.id'))
    # Estabelece a relacao entre Produto e Fornecedor
    fornecedor = relationship("Fornecedor")
 

engine = create_engine('sqlite:///desafio.db', echo=True)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# Inserindo fornecedores 
try:
    with Session() as session: # Usando a sessao corretamente com o gerenciador de contexto
        fornecedores:list = [
            Fornecedor(nome='Fornecedor A', telefone='12345678', email='contato@ab.com', endereco='Endereco A'),
            Fornecedor(nome='Fornecedor B', telefone='55645871', email='contato@abc.com', endereco='Endereco B'),
            Fornecedor(nome='Fornecedor C', telefone='65872150', email='contato@abd.com', endereco='Endereco C'),
            Fornecedor(nome='Fornecedor D', telefone='78425186', email='contato@aba.com', endereco='Endereco D'),
            Fornecedor(nome='Fornecedor E', telefone='33548813', email='contato@abe.com', endereco='Endereco E')
        ]
        session.add_all(fornecedores)
        session.commit()
except SQLAlchemyError as e: # Capiturando excessoes do SQLAlchemy
    print(f"Erro ao inserir fornecedores: {e}")


# Inserindo produtos 
try:
    with Session() as session: # Usando a sessao corretamente com o gerenciador de contexto
        produtos = [
            Produto(nome='Produto 1', descricao='Descricao produto 1', preco=100, fornecedor_id='1'),
            Produto(nome='Produto 2', descricao='Descricao produto 2', preco=300, fornecedor_id='2'),
            Produto(nome='Produto 3', descricao='Descricao produto 3', preco=400, fornecedor_id='3'),
            Produto(nome='Produto 4', descricao='Descricao produto 4', preco=800, fornecedor_id='4'),
            Produto(nome='Produto 5', descricao='Descricao produto 5', preco=1000, fornecedor_id='5')
        ]
        session.add_all(produtos)
        session.commit()
except SQLAlchemyError as e: # Capiturando excessoes do SQLAlchemy
    print(f"Erro ao inserir produto: {e}")




