from pydantic import BaseModel


class ErrorConsultaDelSchema(BaseModel):
    """ Define como uma mensagem de eero será representada
    """
    message: str = "Não há nenhuma consulta agendada para este horário"

class ErrorAgendaConsultaSchema(BaseModel):
    """ Define como uma mensagem de erro será representada
    """
    message: str = "Data e horário não disponíveis para o agendamento."

class ErrorListagemSchema(BaseModel):
    """ Define como uma mensagem de erro será representada
    """
    message: str = "Não foi possível retornar a listagem de consultas."