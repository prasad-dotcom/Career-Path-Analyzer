from fastapi import APIRouter
from services.skill_gap_service import analyze_skill_gap
from pydantic import BaseModel
from typing import List

router = APIRouter()

class SkillGapRequest(BaseModel):
    targetRole: str
    currentSkills:List[str]

@router.post("/skill-gap")
def skill_gap(data: SkillGapRequest):
    return analyze_skill_gap(data.targetRole, data.currentSkills)
