from model import Session
from model.paciente import Paciente
from model.consulta import Consulta
from typing import Optional, List

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