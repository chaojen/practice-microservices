# -*- coding: utf-8 -*-
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return "hello, Python"