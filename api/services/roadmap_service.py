def generate_roadmap(role:str):
    roadmap_data ={
        
        "Backend Developer":[
            "Phase 1 (1–2 months): Java basics, OOP, Git",
            "Phase 2 (2 months): Spring Boot, SQL, APIs",
            "Phase 3 (1–2 months): Deployment, projects, system design basics"
        ],
        
        "Frontend Developer":[
            "Phase 1 (1–2 months): HTML, CSS, JavaScript",
            "Phase 2 (2 months): React, Git, UI Design",
            "Phase 3 (1–2 months): Advanced React, API Integration, Projects"
            
            
        ],
        
        "Data Analyst":[
          
            "Phase 1 (1–2 months): Excel, SQL basics",
            "Phase 2 (2 months): Python, Pandas, Dashboards",
            "Phase 3 (1–2 months): Statistics, Visualizations, Case Studies"  
        ]
    }
    
    
    if role not in roadmap_data:
        return {"error" : "Roadmap not available for this role"}
    return{
        "role": role,
        "roadmap":roadmap_data[role]
    }