import React from "react";

function SkillBox({ analysis }) {
  if (!analysis) {
    return (
      <div className="card">
        <h3>Skill Gap Results</h3>
        <p>Enter your target role and current skills to see your skill gap analysis.</p>
      </div>
    );
  }

  if (analysis.error) {
    return <div className="card error">Error: {analysis.error}</div>;
  }

  return (
    <div className="card">
      <h3>Skill Gap Results</h3>
      <p><strong>Role:</strong> {analysis.role}</p>

      <div className="grid two">
        <div>
          <h4>✅ Matched Skills</h4>
          <ul>
            {(analysis.matchedSkills || []).map((s) => (
              <li key={s}>{s}</li>
            ))}
          </ul>
        </div>
        <div>
          <h4>📚 Skills to Learn</h4>
          <ul>
            {(analysis.missingSkills || []).map((s) => (
              <li key={s}>{s}</li>
            ))}
          </ul>
        </div>
      </div>

      <h4>💡 Recommendations</h4>
      <ol>
        {(analysis.recommendations || []).map((r, i) => (
          <li key={i}>{r}</li>
        ))}
      </ol>

      <h4>🎯 Suggested Learning Order</h4>
      <ol>
        {(analysis.suggestedLearningOrder || []).map((s, i) => (
          <li key={i}>{s}</li>
        ))}
      </ol>
    </div>
  );
}

function RoadmapBox({ roadmap }) {
  if (!roadmap) {
    return (
      <div className="card">
        <h3>Career Roadmap</h3>
        <p>Your personalized career roadmap will appear here after analysis.</p>
      </div>
    );
  }

  if (roadmap.error) {
    return <div className="card error">Error: {roadmap.error}</div>;
  }

  return (
    <div className="card">
      <h3>🗺️ Career Roadmap</h3>
      <p><strong>Role:</strong> {roadmap.role}</p>
      <ol>
        {(roadmap.roadmap || []).map((phase, idx) => (
          <li key={idx}>{phase}</li>
        ))}
      </ol>
    </div>
  );
}

function NewsBox({ news }) {
  if (!news || (Array.isArray(news) && news.length === 0)) {
    return (
      <div className="card">
        <h3>📰 Latest Tech News</h3>
        <p>Loading latest tech stories...</p>
      </div>
    );
  }

  if (news.error) {
    return <div className="card error">Error loading news: {news.error}</div>;
  }

  const newsItems = Array.isArray(news) ? news : news.news || [];

  return (
    <div className="card news">
      <h3>📰 Latest Tech News (HackerNews)</h3>
      {newsItems.map((item, i) => {
        if (!item || !item.title) return null;
        
        return (
          <div className="news-item" key={i}>
            <a 
              href={item.url || "#"} 
              target="_blank" 
              rel="noreferrer"
            >
              {item.title}
            </a>
            <div className="meta">
              <span>by {item.by || "Unknown"}</span>
              <span>score: {item.score || 0}</span>
              <span>{item.type || "story"}</span>
            </div>
          </div>
        );
      })}
    </div>
  );
}

function Dashboard({ analysis, roadmap, news, loading }) {
  return (
    <section className="dashboard">
      <div className="left">
        <SkillBox analysis={analysis} />
      </div>

      <div className="right">
        <RoadmapBox roadmap={roadmap} />
      </div>

      <div className="bottom">
        {loading ? (
          <div className="card">
            <h3>🔄 Loading Results...</h3>
            <p>Analyzing your career path and fetching latest tech news...</p>
          </div>
        ) : (
          <NewsBox news={news} />
        )}
      </div>
    </section>
  );
}

export default Dashboard;
