import React, { useState } from "react";
import InputForm from "./InputForm.jsx";
import Dashboard from "./Dashboard.jsx";

export default function App() {
  const [analysis, setAnalysis] = useState(null);
  const [roadmap, setRoadmap] = useState(null);
  const [news, setNews] = useState(null);
  const [loading, setLoading] = useState(false);

  return (
    <div className="page">
      <header className="header">
        <h1>Career Path Analyzer</h1>
        <p className="sub">Skill-gap analysis • Roadmap • Latest tech news</p>
      </header>

      <main className="container">
        <InputForm
          onStart={async (payload) => {
            setLoading(true);
            setAnalysis(null);
            setRoadmap(null);
            setNews(null);

            try {
              // call skill-gap
              const skillResp = await fetch("/api/skill-gap", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify(payload),
              });
              const skillJson = await skillResp.json();
              setAnalysis(skillJson);

              // call roadmap
              const roadmapResp = await fetch("/api/roadmap", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ targetRole: payload.targetRole }),
              });
              const roadmapJson = await roadmapResp.json();
              setRoadmap(roadmapJson);

              // call news
              const newsResp = await fetch("/api/news");
              const newsJson = await newsResp.json();
              setNews(newsJson?.news || newsJson);
            } catch (err) {
              console.error(err);
              alert("Error communicating with backend. Check console.");
            } finally {
              setLoading(false);
            }
          }}
        />

        <Dashboard
          analysis={analysis}
          roadmap={roadmap}
          news={news}
          loading={loading}
        />
      </main>

      <footer className="footer">
        <small>Assignment — Full Stack Intern • Clean & minimal UI</small>
      </footer>
    </div>
  );
}
