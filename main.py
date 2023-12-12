from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def f_index():
    return {"Хлыстова Екатерина Александровна"}

@app.get('/tools')
async def f_indexT():
    return "Опыт работы с Java"

@app.get('/users')
async def f_indexU():
    return "+79345346944"