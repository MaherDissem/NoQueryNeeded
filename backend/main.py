import uvicorn
from fastapi import FastAPI
from routers import query_db
from config import host, port
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Allow requests from this origin
    allow_credentials=True,  # Allow cookies and credentials
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

app.include_router(query_db.router)

@app.get("/")
async def read_root():
    return {"message": "Welcome to the SQL generation API!"}


if __name__ == "__main__":
    uvicorn.run(app, host=host, port=port)
