import uvicorn
from fastapi import FastAPI
from routers import query_db
from config import host, port


app = FastAPI()
app.include_router(query_db.router)

@app.get("/")
async def read_root():
    return {"message": "Welcome to the SQL generation API!"}


if __name__ == "__main__":
    uvicorn.run(app, host=host, port=port)
