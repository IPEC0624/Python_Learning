from fastapi import FastAPI

app = FastAPI()

"""
あいさつAPI
"""
# @app.get("/sample")
# def read_root():
#     return {"message": "I am the API"}

"""
パスパラメーター
"""

@app.get