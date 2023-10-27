To-Do List
Um site simples para gerenciar tarefas, permitindo aos usuários adicionar, excluir e marcar como concluídas as tarefas.

Instalação
Instale a máquina virtual venv:
python
python -m venv venv


2. Ative o ambiente virtual venv:

.\venv\Scripts\activate


3. Instale as dependências:

pip install fastapi
pip install uvicorn

Entre na pasta correta:
cd "MVC"

4. Rode o servidor:

uvicorn controller:app --reload

## Acessando o site

Acesse o site no navegador usando o seguinte endereço:

http://127.0.0.1:8000/


## Licença

Este projeto é licenciado sob a licença MIT.

## Contribuições

Contribuições são bem-vindas. Para contribuir, siga estas etapas:

1. Fork o projeto no GitHub.
2. Crie uma nova branch para sua alteração.
3. Faça suas alterações e teste-as.
4. Envie um pull request para a branch principal.

## Contato

Para mais informações, entre em contato com o autor do projeto pelo e-mail guilhermevs54@gmail.com
