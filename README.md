# Sistema de Agendamento e Gerenciamento de Consultas (SAGC) - API

O **Sistema de Agendamento e Gerenciamento de Consultas (SAGC)** busca prover aos profissionais de secretariado 
um modo ágil e prático de agendar e administrar consultas virtualmente.

No presente projeto, o SAGC é empregado no contexto de um consultório odontológico, cujos serviços são 
prestados por um único profissional dentista. Cabe ao seu (sua) secretário(a) o uso dessa ferramenta 
para cadastrar os pacientes e marcar suas consultas.

Este projeto foi desenvolvido para o MVP da Sprint 1 da **Pós Gradução de Engenharia de Softwarer da PUC-Rio**. 
<br>
---
<br>
## Execução da aplicação

Para executar esta aplicação, siga os passos enumerados a seguir:


### 1 - Clone o repositório

Clone o repositório através do comando abaixo:

```
[git clone (...)](https://github.com/rafarasant/MVP_PUC_RIO_CONSULTORIO_BACKEND.git)
```


### 2 - Instale as dependências

Para que seja possível executar a aplicação, é preciso instalar primeiramente todas as *libs* (bibliotecas) listadas no arquivo *requirements.txt*. 
Isso deve ser feito no diretório raiz, através do terminal, a partir do seguinte comando.

> Importante: recomença-se fortemente o uso de ambientes virtuais do tipo [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html).

> Atenção: O símbolo *(env)$* presente nos comandos abaixo refere-se tão somente a um exemplo de ambiente virtual ativado. Contudo, não faz por parte dos
> comandos em si.

```
(env)$ pip install -r requirements.txt
```


### 3 - Execute a API

No terminal, execute o comando abaixo:

```
(env)$ flask run --host 0.0.0.0 --port 7000
```

Caso esteja em modo de desenvolvimento, recomenda-se executar o comando acima junto do parâmetro *reload*, o qual reinicia o servidor automaticamente
após qualquer alteração no código fonte.

```
(env)$ flask run --host 0.0.0.0 --port 7000 --reload
```


### 5 - Banco de dados

A pasta *database*, localizada na raiz do projeto, contém o arquivo *mvp.db*. Nela já se encontram criadas as duas tabelas necessárias para a execução
da API (*paciente* e *consulta*). Ainda na pasta *database*, estão os arquivos do tipo *.txt* com os comandos em SQL para a criação das duas tabelas e para 
inserção dos dados referentes a cada uma.


### 4 - Abra a API no navegador

No navegador, abra o link abaixo para visualizar o status da API em execução.

```
localhost:7000
```
