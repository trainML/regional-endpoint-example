from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import importlib

app = FastAPI()

origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

predict = importlib.import_module("simple-tensorflow-classifier.predict")


class prediction_request(BaseModel):
    name: str
    contents: str


@app.post("/predict")
def predict_image(
    item: prediction_request,
):
    return predict.predict_base64_image(item.name, item.contents)
