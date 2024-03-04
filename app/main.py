from transformers import pipeline
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

generator = pipeline("text-generation", model="gpt2")
app = FastAPI()


class Body(BaseModel):
    text: str


@app.get("/")
def root():
    return HTMLResponse(
        "<h1>A self documenting API to interact with gpt-2 and generate text</h1>"
    )

@app.post('/predict')
def predict(body: Body):
    results = generator(body.text, max_length=35, num_return_sequences=1)
    return results[0]

