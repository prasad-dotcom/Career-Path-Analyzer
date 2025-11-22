from fastapi import FastAPI
from routers.skill_gap import router as skill_gap_router
from routers.roadmap import router as roadmap_router
from routers.news import router as news_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    
    title= "Carrer Guidance Backend API",
    version="1.0.0"
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers =["*"],
)


app.include_router(skill_gap_router, prefix ="/api")
app.include_router(roadmap_router, prefix="/api")
app.include_router(news_router, prefix="/api")


@app.get("/")

def root():
    return {"message" : "Carrer Guidance API is running"}

