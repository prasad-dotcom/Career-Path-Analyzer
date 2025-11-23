# 🚀 Career Path Analyzer

A modern full-stack application that provides AI-powered career guidance through skill gap analysis, personalized roadmaps, and latest tech news integration.

![Career Path Analyzer](https://img.shields.io/badge/React-18.2.0-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-Latest-green.svg)
![Python](https://img.shields.io/badge/Python-3.11+-yellow.svg)

## ✨ Features

- 🎯 **Skill Gap Analysis** - Compare your current skills with target role requirements
- 🗺️ **Career Roadmap Generator** - Get personalized 3-phase learning paths
- 📰 **Latest Tech News** - Stay updated with HackerNews integration
- 🎨 **Modern Dark UI** - Beautiful glassmorphism design with smooth animations
- 📱 **Responsive Design** - Works perfectly on desktop and mobile devices

## 🛠️ Tech Stack

### Frontend
- **React 18.2.0** - Modern React with hooks
- **CSS3** - Custom styling with CSS variables and animations
- **Fetch API** - For backend communication

### Backend
- **FastAPI** - High-performance Python web framework
- **Uvicorn** - ASGI web server
- **Requests** - HTTP library for HackerNews API integration
- **Pydantic** - Data validation using Python type annotations

#Demo


https://github.com/user-attachments/assets/9272f268-12f2-465f-98c6-b4eaa7d19e05



## 🚀 Quick Start

### Prerequisites
- Node.js 16+ and npm
- Python 3.11+
- Git

### Backend Setup

1. Navigate to backend directory:
   ```bash
   cd backend
   ```

2. Create and activate virtual environment:
   ```bash
   python -m venv cenv
   # On Windows:
   .\cenv\Scripts\activate
   # On macOS/Linux:
   source cenv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Start the FastAPI server:
   ```bash
   uvicorn main:app --reload
   ```

   Backend will be available at: `http://localhost:8000`

### Frontend Setup

1. Navigate to frontend directory:
   ```bash
   cd frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Start the development server:
   ```bash
   npm start
   ```

   Frontend will be available at: `http://localhost:3000`

## 📡 API Endpoints

### POST /api/skill-gap
Analyzes skill gaps for a target role.

**Request:**
```json
{
  "targetRole": "Backend Developer",
  "currentSkills": ["Java", "Git"]
}
```

**Response:**
```json
{
  "role": "Backend Developer",
  "matchedSkills": ["Java", "Git"],
  "missingSkills": ["Spring Boot", "SQL", "APIs"],
  "recommendations": ["Learn Spring Boot to strengthen your Backend Developer profile"],
  "suggestedLearningOrder": ["Spring Boot", "SQL", "APIs"]
}
```

### POST /api/roadmap
Generates a career roadmap for a target role.

**Request:**
```json
{
  "targetRole": "Backend Developer"
}
```

**Response:**
```json
{
  "role": "Backend Developer",
  "roadmap": [
    "Phase 1 (1–2 months): Java basics, OOP, Git",
    "Phase 2 (2 months): Spring Boot, SQL, APIs",
    "Phase 3 (1–2 months): Deployment, projects, system design basics"
  ]
}
```

### GET /api/news
Fetches latest tech news from HackerNews.

**Response:**
```json
{
  "news": [
    {
      "title": "Latest Tech Story",
      "url": "https://example.com",
      "score": 150,
      "by": "username",
      "type": "story",
      "time": 1640995200
    }
  ]
}
}
```

## 🎨 Design Features

- **Modern Dark Theme** - Professional dark color scheme
- **Gradient Accents** - Beautiful blue/purple gradients
- **Glassmorphism Effects** - Backdrop blur and transparency
- **Smooth Animations** - Hover effects and transitions
- **Responsive Layout** - Mobile-first design approach
- **Accessibility** - Proper contrast and keyboard navigation

## 🏗️ Project Structure

```
Career-Path-Analyzer/
├── backend/                 # FastAPI backend
│   ├── data/               # JSON data files
│   ├── routers/            # API route handlers
│   ├── services/           # Business logic
│   ├── main.py             # FastAPI application
│   └── requirements.txt    # Python dependencies
├── frontend/               # React frontend
│   ├── public/             # Static files
│   ├── src/                # React components
│   │   ├── App.jsx         # Main app component
│   │   ├── InputForm.jsx   # Career input form
│   │   ├── Dashboard.jsx   # Results dashboard
│   │   └── styles.css      # Global styles
│   └── package.json        # Node.js dependencies
└── README.md               # Project documentation
```

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Prasad Reddy** - [GitHub](https://github.com/prasad-dotcom)

## 🙏 Acknowledgments

- HackerNews API for tech news integration
- React community for excellent documentation
- FastAPI for the amazing Python web framework

---

⭐ Star this repository if you find it helpful!
