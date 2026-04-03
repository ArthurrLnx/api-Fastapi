# 📝 Task Manager API

Uma API REST simples e rápida para gerenciamento de tarefas, construída inteiramente com **Python** e **FastAPI**. 

Este projeto foi criado como um exemplo prático de como construir uma API moderna e tipada usando Pydantic, com dados armazenados em memória para facilitar a execução e os testes locais sem necessidade de configurar um banco de dados.

## 🚀 Tecnologias Utilizadas

* **Python 3.7+**
* **FastAPI:** Framework web moderno e de alta performance.
* **Pydantic:** Validação de dados e tipagem estática.
* **Uvicorn:** Servidor ASGI para rodar a aplicação.

## ✨ Funcionalidades

A API permite realizar as seguintes operações (CRUD):
* `POST /tasks`: Cria uma nova tarefa.
* `GET /tasks`: Lista todas as tarefas cadastradas.
* `GET /tasks/{task_id}`: Retorna os detalhes de uma tarefa específica pelo ID.
* `DELETE /tasks/{task_id}`: Remove uma tarefa específica.

## 🛠️ Como rodar o projeto localmente

Siga os passos abaixo para executar a API na sua máquina.

### 1. Clone este repositório
```bash
git clone [https://github.com/ArthurrLnx/api-Fastapi.git](https://github.com/ArthurrLnx/api-Fastapi.git)
cd api-Fastapi
