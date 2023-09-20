from sqlalchemy import Column, String, Integer, DateTime, Float, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from typing import Union

from model.base import Base
from model.consulta import Consulta


class Paciente(Base):
    __tablename__ = 'paciente'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    cpf = Column(String(11), unique=True, index=True, nullable=False)
    nome = Column(String(255), nullable=False)
    sobrenome = Column(String(255), nullable=False)
    data_nascimento = Column(String(8), nullable=True)
    plano_saude = Column(Boolean, default=0, nullable=False)

    # Definição do relacionamento entre o paciente e consulta.
    # Essa relação é implicita, não está salva na tabela 'paciente',
    # mas aqui estou deixando para SQLAlchemy a responsabilidade
    # de reconstruir esse relacionamento.
    consultas = relationship("Consulta")

    def __init__(self, nome:str, sobrenome:str, cpf:str, data_nascimento:str, plano_saude:bool):
        """
        Cria um paciente

        Arguments:
            nome: nome do paciente
            sobrenome: sobrenome do paciente
            cpf: cpf do paciente
            data_nascimento: data de nascimento do paciente
            plano_saude: informa se o paciente possui um plano de saúde ou não
        """
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf
        self.data_nascimento = data_nascimento
        self.plano_saude = plano_saude
    
    # def adiciona_consulta(self, consulta:Consulta):
    #     """Adiciona os valores da classe Consulta ao Paciente
    #     """
    #     self.consultas.append(consulta)