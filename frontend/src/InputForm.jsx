import React, { useState } from "react";

function InputForm({ onStart }) {
  const [targetRole, setTargetRole] = useState("");
  const [skillsText, setSkillsText] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();
    if (!targetRole.trim()) {
      alert("Please enter a target role (e.g., Backend Developer).");
      return;
    }
    const currentSkills = skillsText
      .split(",")
      .map((s) => s.trim())
      .filter(Boolean);
    onStart({ targetRole: targetRole.trim(), currentSkills });
  };

  const handlePreset = (role) => {
    setTargetRole(role);
    setSkillsText("");
  };

  return (
    <form className="card form" onSubmit={handleSubmit}>
      <h2>Career Goal</h2>

      <label>Target Role</label>
      <input
        type="text"
        value={targetRole}
        onChange={(e) => setTargetRole(e.target.value)}
        placeholder='e.g., "Backend Developer"'
      />

      <label>Current Skills (comma separated)</label>
      <input
        type="text"
        value={skillsText}
        onChange={(e) => setSkillsText(e.target.value)}
        placeholder="e.g., Java, SQL, Git"
      />

      <div className="form-actions">
        <button className="btn primary" type="submit">
          Analyze My Career Path
        </button>
        
        <div className="quick">
          <small>Quick roles:</small>
          <div className="quick-buttons">
            <button 
              type="button" 
              onClick={() => handlePreset("Backend Developer")} 
              className="btn mini"
            >
              Backend
            </button>
            <button 
              type="button" 
              onClick={() => handlePreset("Frontend Developer")} 
              className="btn mini"
            >
              Frontend
            </button>
            <button 
              type="button" 
              onClick={() => handlePreset("Data Analyst")} 
              className="btn mini"
            >
              Data Analytics
            </button>
          </div>
        </div>
      </div>
    </form>
  );
}

export default InputForm;
