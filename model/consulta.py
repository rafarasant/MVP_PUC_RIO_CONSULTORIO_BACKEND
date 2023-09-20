from sqlalchemy import Column, String, Integer, DateTime, Float, ForeignKey
from datetime import datetime

from  model import Base


class Consulta(Base):
    __tablename__ = 'consulta'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    data = Column( String(8), nullable=False)
    horario = Column(String(4), nullable=False)

    """
    Marca uma consulta

    Arguments:
        data: data da consulta
        horario: horario da consulta
        
    """
    # Definição do relacionamento entre o comentário e um produto.
    # Aqui está sendo definido a coluna 'produto' que vai guardar
    # a referencia ao produto, a chave estrangeira que relaciona
    # um produto ao comentário.

    paciente_id = Column(Integer, ForeignKey("paciente.id"), nullable=False)

    """
    paciente_id: id do paciente da consulta
    
    """

    def __init__(self, data:str, horario:str, paciente_id:int):
        self.data = data
        self.horario = horario
        self.paciente_id = paciente_id
    