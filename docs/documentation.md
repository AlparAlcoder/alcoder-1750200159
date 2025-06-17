# Documentação da API de itens

Essa API é um exemplo simples de uma API construída com o FastAPI do Python. Ela permite a criação e recuperação de itens em uma loja fictícia. 

## Endpoints

### POST /items/

Cria um novo item na loja.

#### Parâmetros

- `item` (corpo da requisição): Um objeto JSON que representa o item a ser criado. Deve ter a seguinte estrutura:

    - `name` (string): O nome do item (obrigatório).
    - `description` (string): A descrição do item (opcional).
    - `price` (float): O preço do item (obrigatório).
    - `quantity` (int): A quantidade do item em estoque (obrigatório).

#### Exemplo de Uso

```bash
curl -X POST "http://localhost:8000/items/" -H  "accept: application/json" -H  "Content-Type: application/json" -d "{\"name\":\"item1\",\"price\":10.5,\"quantity\":5}"
```

### GET /items/{item_id}

Retorna um item existente baseado em seu id.

#### Parâmetros

- `item_id` (path): O ID do item a ser recuperado.

#### Exemplo de Uso

```bash
curl -X GET "http://localhost:8000/items/1" -H  "accept: application/json"
```

## Notas Importantes

- Essa API não possui persistência de dados. Portanto, os itens serão perdidos quando o servidor for desligado.
- Não há validação de IDs duplicados para os itens. Cada POST em /items/ simplesmente adiciona o item à lista.
- Não há nenhuma forma de autenticação implementada.

## Dependências Necessárias

- Python 3.6 ou superior
- FastAPI
- Pydantic
- Uvicorn (para servir a aplicação)