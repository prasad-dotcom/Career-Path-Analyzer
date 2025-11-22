from fastapi import APIRouter
from services.roadmap_service import generate_roadmap
from pydantic import BaseModel

router = APIRouter()

class RoadmapRequest(BaseModel):
    targetRole: str

@router.post("/roadmap")
def roadmap(data: RoadmapRequest):
    return generate_roadmap(data.targetRole)
