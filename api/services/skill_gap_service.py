import json


def analyze_skill_gap(target_role:str, current_skills:list):
    with open("data/skills.json") as f:
        skill_data = json.load(f)
        
    if target_role not in skill_data:
        return {"error": "Role is not found"}
    
    required_skills = skill_data[target_role]
    
    matched = [s for s  in current_skills if s in required_skills]
    missing = [s for s in required_skills if s not in current_skills]
    
    recommendations = [
        
        f"Learn {skill} to strengthen your {target_role} profile"
        for skill in missing
    ]
    
    return {
        "role": target_role,
        "matchedSkills":matched,
        "missingSKills":missing,
        "recommendations":recommendations,
        "suggestedLearningOrder": missing
    }