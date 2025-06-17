Desculpe, mas a especificação está contraditória. Você está pedindo uma API em Node.js, mas o contexto inicial é de um desenvolvedor Python especializado em FastAPI. 

Por favor, esclareça se você precisa de uma API em Node.js ou Python (FastAPI). 

Se você precisa de uma API Python usando FastAPI, o código poderia ser algo como isto:


from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str = None
    price: float
    quantity: int

store_items = []

@app.post("/items/")
async def create_item(item: Item):
    store_items.append(item.dict())
    return item

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    if item_id > len(store_items):
        raise HTTPException(status_code=404, detail="Item not found")
    return store_items[item_id-1]


Este código define uma API com dois endpoints (`/items/` e `/items/{item_id}`), aceita a criação de novos itens e retorna um item existente baseado em seu id. 

Por favor, note que este é um exemplo simples e não é uma implementação completa com persistência de dados e autenticação.