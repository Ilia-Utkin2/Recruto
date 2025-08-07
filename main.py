from fastapi import FastAPI, Query
from fastapi.responses import PlainTextResponse

app = FastAPI()

@app.get("/", response_class=PlainTextResponse)
async def hello(
    name: str = Query(default="Recruto", title="Имя"),
    message: str = Query(default="Давай дружить", title="Сообщение")
):
    return f"Hello {name}! {message}!"