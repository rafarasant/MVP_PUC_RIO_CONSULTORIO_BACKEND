from flask_openapi3 import OpenAPI, Info, Tag, Response
from flask import redirect, request
from urllib.parse import unquote

from sqlalchemy.exc import IntegrityError

from model import Session
from model.paciente import Paciente
from model.consulta import Consulta

from logger import logger

from helper.api_helper import apresenta_consultas

from schemas.consulta import ConsultaSchema, ListagemConsultaViewSchema, ConsultaDelSchema, AgendaConsultaSchema, AgendaPacienteSchema, ConsultaPacienteSchema, PacienteSchema

from schemas.error import ErrorAgendaConsultaSchema, ErrorConsultaDelSchema, ErrorListagemSchema

from flask_cors import CORS

from flask.views import View

from pydantic import BaseModel


info = Info(title="Minha API", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

#definição de tags 
home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
paciente_tag = Tag(name="Paciente", description="Cadastramento, visualização e remoção de pacientes à base")
consulta_tag = Tag(name="Consulta", description="Marcação de uma consulta para os pacientes cadastrados na base")


@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi')


# Função lista de consultas agendadas

@app.get('/consultas', tags=[consulta_tag],
         responses={"200": ListagemConsultaViewSchema, "404": ErrorListagemSchema})
def get_consulta():
    """Retorna uma representação dos pacientes cadastrados e das consultas agendadas. 
       Na View, essa representação ocorre numa mesma tabela.
    """
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    consultas_pacientes = session.query(Consulta, Paciente).join(Paciente, Consulta.paciente_id == Paciente.id).all()

    if not consultas_pacientes:
        # se não houver consultas cadastradas
        return {"consultas_pacientes": []}, 200
    else:
        logger.debug(f"%d consultadas agendadas" % len(consultas_pacientes))
        # retorna a representação das consultas cadastradas
        # return apresenta_consultas_marcadas(consultas_pacientes), 200
        # print(consultas_pacientes)
        return apresenta_consultas(consultas_pacientes), 200
        
    
@app.delete('/desmarcar_consulta', tags=[consulta_tag],
            responses={"200": ConsultaDelSchema, "404": ErrorConsultaDelSchema})
def del_consulta(query: ConsultaDelSchema):
    """Deleta uma consulta a partir da data e horario da consulta

    Retorna uma mensagem de confirmação da remoção.
    """

    data = request.args['data']
    horario = request.args['horario']

    session = Session()

    consultas_desmarcadas = session.query(Consulta).filter((Consulta.data == data),
                                                         (Consulta.horario == horario)).delete()
    
    session.commit()

    return {"mesage": "Consulta desmarcada com sucesso!"}, 200


#  adiciona dados de paciente e consuta no banco de dados 

@app.post('/agendar_consulta', tags=[consulta_tag],
          responses={"200": ListagemConsultaViewSchema, "404": ErrorAgendaConsultaSchema})
def add_consulta(form: ConsultaSchema and PacienteSchema):
    """Adiciona uma nova consulta à base de dados

    Retorna uma representação da consulta e do paciente associado.
    """

    plano_saude_boolean = False

    if (request.form['plano_saude'] == "Sim"):
        plano_saude_boolean = True

     # criando conexão com a base
    session = Session()

    consulta = session.query(Consulta).filter(Consulta.data == request.form['data_consulta'],
                            Consulta.horario == request.form['horario_consulta']).first()
    
    if consulta == None:

        paciente = session.query(Paciente).filter(Paciente.cpf == request.form['cpf']).first()
        
        if paciente == None:

            # criando objeto da classe Paciente
            paciente = Paciente(
                nome = request.form['nome'],
                sobrenome = request.form['sobrenome'],
                cpf = request.form['cpf'],
                data_nascimento = request.form['data_nascimento'],
                plano_saude = plano_saude_boolean
            )

            session.add(paciente)
            session.flush()
            session.refresh(paciente)

        consulta = Consulta(
            data = request.form['data_consulta'],
            horario = request.form['horario_consulta'],
            paciente_id = paciente.id
        )

        session.add(consulta)
        session.commit()

        return {'mesage': "Consulta agendada com sucesso"}
    
    else:

        return {'mesage': "Horário indisponível"}
