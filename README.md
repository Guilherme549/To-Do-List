To-Do-List Web App
O To-Do-List Web App é uma aplicação que permite aos usuários gerenciar suas tarefas de forma prática. Com ele, você pode adicionar novas tarefas, marcá-las como concluídas e removê-las da lista.

Como Iniciar
Siga os passos abaixo para configurar e executar o projeto localmente:

Clone este repositório em sua máquina:

bash
Copy code
git clone https://github.com/seu-usuario/to-do-list.git
Navegue até o diretório do projeto:

bash
Copy code
cd to-do-list
Crie uma máquina virtual Python (venv) para isolar o ambiente de desenvolvimento:

bash
Copy code
python -m venv venv
Ative a máquina virtual (Windows):

bash
Copy code
.\venv\Scripts\activate
Ou ative a máquina virtual (macOS e Linux):

bash
Copy code
source venv/bin/activate
Instale as dependências do projeto:

bash
Copy code
pip install -r requirements.txt
Com as dependências instaladas, você pode iniciar o servidor com o comando:

bash
Copy code
uvicorn controller:app --reload
O servidor estará disponível em http://127.0.0.1:8000/.

Acesse o site em seu navegador favorito com o seguinte endereço:

http://127.0.0.1:8000/

Agora você pode começar a gerenciar suas tarefas de forma eficiente com o To-Do-List Web App. Desfrute!

Tecnologias Utilizadas
FastAPI: Framework web assíncrono de alto desempenho.
SQLite3: Sistema de gerenciamento de banco de dados leve e eficiente.
