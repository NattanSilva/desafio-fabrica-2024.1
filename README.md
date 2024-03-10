# Desafio Fabrica de Software - Template 1

### 1 - Crie seu ambiente virtual:

```shell
python -m venv venv
```

### 2 - Ative seu ambiente virtal:

```shell
# linux:
source venv/bin/activate

# windows (powershell):
.\venv\Scripts\activate

# windows (git bash):
source venv/Scripts/activate
```

### 3 - Instale as dependências do projeto:

```shell
pip install -r requirements.txt
```

### 4 - Gere as migrações:

```shell
python manage.py makemigrations
```

### 5 - Execute as migrações:

```shell
python manage.py migrate
```

### 6 - Inicie o servidor:

```shell
python manage.py runserver
```

## Passos adicionais:

### Criar um super usuário:

```shell
python manage.py createsuperuser
```

### Acessar a página de admin:

Para acessar a página de admin basta acessa o link abaixo e preencher os campos com suas informações passadas durante a cração do super user.

```shell
http://localhost:8000/admin/
```

### Testando sua API

Para testar todas as funcionalidades de sua API basta baixar o <a href="https://insomnia.rest/download" target="_blank">Insomnia</a> na sua máquina local, depois realizar o <a href="https://docs.insomnia.rest/insomnia/import-export-data" target="_blank">import</a> dentro do seu Insomnia do arquivo <code>insomnia-data.json</code>, iniciar sua API e testá-la manualmente.
