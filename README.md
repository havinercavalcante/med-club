# MedClub API

## Descrição

Este projeto é uma API RESTful desenvolvida com Django Rest Framework para gerenciar usuários, pedidos e itens.

## Instalação

1. Clone o repositório:
   ```bash
   git clone git@github.com:havinercavalcante/medclub.git

2. Navegue até o diretório do projeto:
   ```bash
   cd medclub

3. Crie um ambiente virtual:
   ```bash
   python3 -m venv venv

4. Ative o ambiente virtual:
   ```bash
   source venv/bin/activate  # No Windows: venv\Scripts\activate

5. Instale as dependências:
   ```bash
   pip install -r requirements.txt

6. Execute as migrações do banco de dados:
   ```bash
   python manage.py migrate

7. Inicie o servidor de desenvolvimento:
   ```bash
   python manage.py runserver

## Rotas da API
Usuários
- Login: http://127.0.0.1:8000/api/v1/login
- Registro: http://127.0.0.1:8000/api/v1/register
- Perfil do usuário: http://127.0.0.1:8000/api/v1/user
  
Pedidos
- Gestão de pedidos: http://127.0.0.1:8000/api/v1/pedidos
  
Itens
- Gestão de itens: http://127.0.0.1:8000/api/v1/itens
  
## Documentação da API
A documentação da API é gerada utilizando o Swagger. Para acessar a documentação, execute o servidor de desenvolvimento e acesse:
   ```bash
   http://127.0.0.1:8000/swagger/
