from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello():
    return {'message': 'Hello world'}

@app.get("/about")
def diplab():
    return {'message': 'Digital Image Processing Lab is located inside Islamia College Peshawar.'}