from pydantic import BaseModel
from typing import Optional, List
from model.paciente import Paciente
from model.consulta import Consulta

from model import Session
from flask import redirect, request

from schemas.error import ErrorAgendaConsultaSchema, ErrorConsultaDelSchema


from flask_cors import CORS

from flask.views import View

from logger import logger

from sqlalchemy.exc import IntegrityError

class ConsultaSchema(BaseModel):
    """ Define como uma nova consulta a ser inserida é representada
    """
    id: int = 1
    data: str = "2023/12/09"
    horario: str= "10:00"
    paciente_id: int = 1

class PacienteSchema(BaseModel):
    """ Define como um novo paciente a ser inserido é representado 
    """
    id:int = 1
    nome: str = "Phillip"
    sobrenome: str = "Sherman"
    cpf: str = "74954962072"
    data_nascimento: str = "1989-04-15"
    plano_saude: bool = True

class ConsultaPacienteSchema(BaseModel):
    id: int = 1
    nome: str = "Phillip"
    sobrenome: str = "Sherman"
    cpf: str = "74954962072"
    data_nascimento: str = "1989-04-15"
    consulta: List[ConsultaSchema]
    plano_saude: bool = True

class ListagemConsultaViewSchema(BaseModel):
    """ Define como uma consulta agendada deve ser retornada e apresentada no front-end: 
        Constam dados do paciente e da respectiva consulta na tabela.
    """
    nome: str = "Phillip"
    sobrenome: str = "Sherman"
    cpf: str = "74954962072"
    data_nascimento: str = "1989-04-15"
    consulta: List[ConsultaSchema]
    plano_saude: bool = True
    
    
def apresenta_consultas(consultas_pacientes):
    """Faz a busca por todos as consultas agendadas

    Retorna uma representação da listagem de consultas.
    """

    result = []
    for consulta, paciente in consultas_pacientes:
        result.append({
            "nome": paciente.nome,
            "sobrenome": paciente.sobrenome,
            "cpf": paciente.cpf,
            "data_nascimento": paciente.data_nascimento,
            "data_consulta": consulta.data,
            "horario_consulta": consulta.horario,
            "plano_saude": paciente.plano_saude,
        })

    return {"consultas_pacientes": result}


class AgendaConsultaSchema(BaseModel):
    """ Define como deve ser a estrutura do dado inserido na tabela do banco de dados.
    """
    mesage: str = "Consulta agendada com sucesso", 200
    # id:int = 1
    # data: str = "2023-09-18"
    # horario: str = "10:00"
    # paciente_id: int = 1
    

class AgendaPacienteSchema(BaseModel):
    """ Define como deve ser a estrutura do dado inserido na tabela do banco de dados.
    """
    id:int = 1
    nome: str = "Phillip"
    sobrenome: str = "Sherman"
    cpf: str = "74954962072"
    data_nascimento: str = "1989-04-15"
    plano_saude: bool = True


def del_consulta(Consulta):
    """Deleta uma consulta a partir do cpf do paciente, bem como da data e horario da consulta

    Retorna uma mensagem de confirmação da remoção.
    """

    data = request.args['data']
    horario = request.args['horario']

    session = Session()

    consultas_desmarcadas = session.query(Consulta).filter((Consulta.data == data),
                                                         (Consulta.horario == horario)).delete()
    
    session.commit()

    return {"mesage": "consulta desmarcada"}, 200


class ConsultaDelSchema(BaseModel):
    """ Define como deve ser a estrutura do dado retornado após uma requisição de remoção.
    """
    mesage: str = "Consulta desmarcada com sucesso!"
    horario: str = "10:00"
    data: str = "2023-09-18"

