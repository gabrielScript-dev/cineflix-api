# CineFlix API

Uma API RESTful para gerenciamento de filmes, críticas e informações cinematográficas. Construída com Django REST Framework e autenticação JWT.

## Principais Funcionalidades

### 🎬 Filmes
- Listar todos os filmes com informações detalhadas
- Criar novos filmes associados a gêneros e atores
- Atualizar dados de filmes existentes
- Remover filmes do catálogo
- Visualizar classificação média de cada filme baseada em avaliações

### ⭐ Avaliações
- Adicionar avaliações (comentários e notas) para filmes
- Listar todas as avaliações do sistema
- Editar avaliações existentes
- Deletar avaliações
- Calcular automaticamente a média de estrelas de cada filme

### 🎭 Atores
- Gerenciar lista de atores
- Associar atores a filmes
- Listar atores e seus filmografias

### 🎪 Gêneros
- Criar e gerenciar categorias de filmes
- Classificar filmes por gênero
- Listar gêneros disponíveis

### 🔐 Autenticação
- Autenticação baseada em JWT (JSON Web Tokens)
- Endpoints protegidos que exigem token válido
- Obtenção de token com credenciais
- Refresh de tokens expirados
- Verificação de validade de tokens

## Stack Tecnológico

- **Linguagem:** Python
- **Framework:** Django 6.0.6 + Django REST Framework
- **Autenticação:** Simple JWT
- **Banco de Dados:** SQLite (padrão para desenvolvimento)
- **API Version:** v1

## Estrutura do Projeto

```
cineflix-api/
├── app/              # Configurações principais do Django
├── authentication/   # Autenticação JWT
├── movies/          # Gerenciamento de filmes
├── reviews/         # Sistema de avaliações
├── actors/          # Gerenciamento de atores
├── genres/          # Gerenciamento de gêneros
└── manage.py        # Utilitário CLI do Django
```

## Como Usar

### Instalação

```bash
# Clonar o repositório
git clone https://github.com/gabrielScript-dev/cineflix-api.git
cd cineflix-api

# Criar ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate  # Windows

# Instalar dependências
pip install django djangorestframework djangorestframework-simplejwt
```

### Executar o Servidor

```bash
# Executar migrações
python manage.py migrate

# Criar superusuário (opcional, para acessar admin)
python manage.py createsuperuser

# Iniciar o servidor
python manage.py runserver
```

O servidor estará disponível em `http://localhost:8000`

## Endpoints da API

Todos os endpoints requerem autenticação JWT (exceto `/api/v1/auth/token/`).

### Autenticação
- `POST /api/v1/auth/token/` - Obter token JWT
- `POST /api/v1/auth/token/refresh/` - Renovar token
- `POST /api/v1/auth/token/verify/` - Verificar token

### Filmes
- `GET /api/v1/movies/` - Listar filmes
- `POST /api/v1/movies/` - Criar filme
- `GET /api/v1/movies/{id}` - Detalhe do filme
- `PUT /api/v1/movies/{id}` - Atualizar filme
- `DELETE /api/v1/movies/{id}` - Deletar filme

### Avaliações
- `GET /api/v1/reviews/` - Listar avaliações
- `POST /api/v1/reviews/` - Criar avaliação
- `GET /api/v1/reviews/{id}` - Detalhe da avaliação
- `PUT /api/v1/reviews/{id}` - Atualizar avaliação
- `DELETE /api/v1/reviews/{id}` - Deletar avaliação

### Gêneros
- `GET /api/v1/genres/` - Listar gêneros
- `POST /api/v1/genres/` - Criar gênero
- `GET /api/v1/genres/{id}` - Detalhe do gênero
- `PUT /api/v1/genres/{id}` - Atualizar gênero
- `DELETE /api/v1/genres/{id}` - Deletar gênero

### Atores
- `GET /api/v1/actors/` - Listar atores
- `POST /api/v1/actors/` - Criar ator
- `GET /api/v1/actors/{id}` - Detalhe do ator
- `PUT /api/v1/actors/{id}` - Atualizar ator
- `DELETE /api/v1/actors/{id}` - Deletar ator
