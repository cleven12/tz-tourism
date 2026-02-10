# 🗺️ TZ Tourism

> Open-source tourism platform for Tanzania with GPS-accurate attraction data, real-time weather, and seasonal planning guides.

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Django](https://img.shields.io/badge/Django-4.2+-green.svg)](https://www.djangoproject.com/)
[![Next.js](https://img.shields.io/badge/Next.js-14+-black.svg)](https://nextjs.org/)
[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

**Live Demo:** [Coming Soon] | **API Docs:** [COMING SOON](docs/API.md)

---

## 🎯 The Problem

Tourists visiting Tanzania face:
- [X] **Scattered information** about attractions
- [X] **Generic weather data** (city-level, not location-specific)
- [X] **Unclear difficulty ratings** for activities
- [X] **No seasonal planning guidance** (rain vs dry seasons)
- [X] **Commercially biased** or misleading information

**Result:** Poor planning, wrong timing, unrealistic expectations, safety risks.

---

## ✨ The Solution

**TZ Tourism** provides:
- **GPS-accurate location data** for every attraction
- **Real-time weather** at specific attractions (not cities)
- **Historical weather patterns** for seasonal planning
- **Honest difficulty ratings** (altitude, terrain, physical challenge)
- **Nearest access points** (airports, towns)
- **Open-source & free** — no commercial bias
- **Well-documented REST API** for developers

---

## 🏗️ Architecture

**Monorepo Structure:**
```
tz-tourism/
├──app  
|   ├── backend/      # Django REST API
|   └── frontend/     # Next.js web app
├── docs/             # Documentation
└── legal/            # Terms, Privacy, Moderation
```

### **Backend (Django)**
- REST API with DRF
- MySQL database
- Weather integration (Open-Meteo)
- User authentication
- Content moderation system

### **Frontend (Next.js)**
- Server-side rendering (SEO)
- Interactive maps (Leaflet)
- Responsive design
- Real-time weather display
- Progressive Web App (PWA)

---

## 🚀 Quick Start

### **Prerequisites**
- Python 3.10+
- Node.js 18+
- PostgreSQL (or SQLite for dev)

### **1. Clone Repository**
```bash
git clone https://github.com/yourusername/tz-tourism.git
cd tz-tourism
```

### **2. Backend Setup**
```bash
cd backend

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Create superuser (optional)
python manage.py createsuperuser

# Start server
python manage.py runserver
```

Backend runs at: `http://localhost:8000`

### **3. Frontend Setup**
```bash
cd frontend

# Install dependencies
npm install

# Create environment file
cp .env.example .env.local

# Add your API URL to .env.local:
# NEXT_PUBLIC_API_URL=http://localhost:8000/api/v1

# Start development server
npm run dev
```

Frontend runs at: `http://localhost:3000`

---

## 📚 API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/v1/attractions/` | GET | List all attractions |
| `/api/v1/attractions/:id/` | GET | Attraction details |
| `/api/v1/attractions/:id/weather/` | GET | Current weather |
| `/api/v1/attractions/:id/seasonal/` | GET | Seasonal patterns |
| `/api/v1/regions/` | GET | All regions |
| `/api/v1/weather/current/` | GET | Weather by GPS |

**Full Documentation:** [API.md](docs/API.md)

### **Example Response**
```json
{
  "id": 1,
  "name": "Mount Kilimanjaro",
  "region": "Kilimanjaro",
  "latitude": -3.0674,
  "longitude": 37.3556,
  "altitude_meters": 5895,
  "difficulty": "difficult",
  "nearest_airport": "Kilimanjaro International Airport (JRO)",
  "description": "Africa's highest mountain...",
  "weather": {
    "temperature_c": 22.5,
    "condition": "Clear",
    "rain_mm": 0.0,
    "updated_at": "2026-02-10T10:30:00Z"
  },
  "seasonal_info": {
    "dry_season": "June-October, January-February",
    "rainy_season": "March-May (long rains), November-December (short rains)",
    "best_time_to_visit": "June-October"
  },
  "is_verified": true,
  "last_updated": "2026-02-01T08:00:00Z"
}
```

---

## 🌟 Key Features

### **For Tourists:**
- 📍 Browse attractions by region
- 🗺️ Interactive map view
- 🌤️ Real-time weather at each location
- 📊 Historical weather trends
- ⛰️ Clear difficulty ratings
- 📅 Seasonal planning guides
- ✈️ Nearest airports & access info

### **For Developers:**
- 🔌 RESTful API
- 📖 OpenAPI documentation
- 🔑 API key support (coming soon)
- 🚀 Fast response times
- 🆓 Free & open-source

---

## 🤝 Contributing

We welcome contributions! Here's how you can help:

### **Ways to Contribute:**
- 🗺️ **Add new attractions** — know a hidden gem?
- 📸 **Upload photos** — share your travel photos
- 🐛 **Report bugs** — found an issue?
- 💡 **Suggest features** — have ideas?
- 📖 **Improve docs** — help others understand
- 🔧 **Fix bugs** — submit a PR
- 🌐 **Translate** — add language support

### **Getting Started:**
1. Read [CONTRIBUTING.md](CONTRIBUTING.md)
2. Check [open issues](https://github.com/yourusername/tz-tourism/issues)
3. Fork the repo
4. Create a feature branch
5. Submit a pull request

---

## ⚠️ Important Disclaimers

### **Please Read Before Using:**

This platform provides information **for planning purposes only**.

**We are NOT responsible for:**
- [x] Injuries or accidents during travel
- [x] Weather-related incidents
- [x] Inaccurate or outdated information
- [x] Third-party tour operator services

**You should:**
- [✔] Verify all information with local authorities
- [✔] Check real-time weather before traveling
- [✔] Consult professional guides for challenging activities
- [✔] Get medical advice for high-altitude areas
- [✔] Use this as a **planning tool**, not a guarantee

### **Data Accuracy:**
- Weather data: Third-party APIs (Open-Meteo)
- Seasonal info: Historical patterns (not forecasts)
- Attraction data: Crowd-sourced and moderated
- Difficulty ratings: Subjective estimates

**Full Terms:** [TERMS.md](legal/TERMS.md) | **Privacy:** [PRIVACY.md](legal/PRIVACY.md)

---

## 📊 Project Status

### **Current Features:**
- [✔] Core attraction database
- [✔] REST API
- [✔] Real-time weather integration
- [✔] Interactive map
- [✔] Responsive web interface
- [✔] Content moderation system

### **Roadmap:**
- [✔] User reviews (moderated)
- [✔] Tour operator directory
- [✔] Multi-language support (Swahili, French)
- [✔] Mobile app (React Native)
- [✔] Offline PWA mode
- [✔] Advanced search & filters
- [✔] Trip planning tool
- [✔] Community forum

---

## 🛠️ Tech Stack

### **Backend:**
- **Framework:** Django 4.2+ / Django REST Framework
- **Database:** PostgreSQL (production) / SQLite (dev)
- **Weather:** Open-Meteo API
- **Hosting:** PythonAnywhere / Railway / Heroku

### **Frontend:**
- **Framework:** Next.js 14+ (React)
- **Styling:** Tailwind CSS
- **Maps:** Leaflet / Mapbox
- **State:** React Context / Zustand
- **Hosting:** Vercel / Netlify

### **DevOps:**
- **CI/CD:** GitHub Actions
- **Version Control:** Git
- **Testing:** pytest (backend), Jest (frontend)
- **Monitoring:** Sentry (coming soon)

---

## 📖 Documentation

- [API Documentation](docs/API.md)
- [Contributing Guide](CONTRIBUTING.md)
- [Code of Conduct](CODE_OF_CONDUCT.md)
- [Terms of Service](legal/TERMS.md)
- [Privacy Policy](legal/PRIVACY.md)
- [Moderation Policy](legal/MODERATION.md)

---

## 💖 Support This Project

If this project helps you, consider:

- ⭐ **Star this repository**
- 🐛 **Report bugs or issues**
- 💡 **Suggest new features**
- 🔀 **Submit pull requests**
- 📢 **Share with others**
- ☕ [**Buy me a coffee**](https://buymeacoffee.com/yourusername)

---

## 📜 License

MIT License - see [LICENSE](LICENSE) for details.

**Summary:** Free to use, modify, and distribute. No warranty provided.

---

## 🌍 About

Built by a Tanzanian developer to provide **honest, accurate tourism information** for Tanzania.

**Mission:** Enable safe, informed, and meaningful tourism through open data.

---

## 📬 Contact

- **Issues:** [GitHub Issues](https://github.com/yourusername/tz-tourism/issues)
- **Email:** your.email@example.com
- **LinkedIn:** [Your Profile](https://linkedin.com/in/yourprofile)
- **Twitter:** [@yourusername](https://twitter.com/yourusername)

---

## 🙏 Acknowledgments

- Weather data: [Open-Meteo](https://open-meteo.com)
- Maps: [OpenStreetMap](https://www.openstreetmap.org) contributors
- Icons: [Lucide Icons](https://lucide.dev)
- Community contributors: [See all](https://github.com/yourusername/tz-tourism/graphs/contributors)

---

**⚡ Built with Django + Next.js | 🇹🇿 Made in Tanzania | 🌍 For the World**