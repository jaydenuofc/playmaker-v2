# PlayMaker V2 – Fantasy Start/Sit Helper  
### ENTI 633 – AI‑Assisted Application Project

<img width="611" height="624" alt="image" src="https://github.com/user-attachments/assets/4f57d084-410f-4fad-895a-b6c850da48f7" />


PlayMaker V2 is a lightweight web application built as a class project for ENTI 633 and customized for a classmate’s fantasy football team. It uses live injury data and roster‑structure rules to help users quickly evaluate start/sit decisions. 

---

## 📌 Overview

This project demonstrates how AI can support the end‑to‑end creation of a functional web application.  
The tool provides a clean interface for evaluating fantasy football lineups using injury‑based logic, roster rules, and automated recommendations.

---

## 🚀 Core Features

### **Roster Management**
- Add custom players (name, team, position)
- Move players between **Starters** and **Bench**
- Delete unwanted players
- Automatically saved to browser `localStorage`

### **Live Injury Status Integration**
- Pulls real‑time injury colors (green/yellow/red) from a backend hosted on Render  
- Color coding:
  - 🟢 Healthy  
  - 🟡 Questionable  
  - 🔴 Out / IR  

### **Start/Sit Recommendations**
- Automatically identifies injured starters  
- Recommends bench replacements from matching positions  
- FLEX logic supports RB/WR/TE substitutions  

### **Lineup Validation**
Required starter format:
- 1 DST  
- 1 QB  
- 2 WR  
- 2 RB  
- 1 TE  
- 2 FLEX  
- 1 K  

If the lineup exceeds allowed counts:
- Invalid players are highlighted  
- An error message explains the issue  

### **Risk Summary**
Displays total starters by status:
- Healthy  
- Questionable  
- Out/IR  

---

## 🧠 How It Works

### **Frontend**
- Single‑page app built using **HTML, CSS, vanilla JavaScript**
- Dynamic DOM rendering for roster updates
- Uses browser storage to persist user changes

### **Backend**
Hosted on Render:  
`https://playmaker-v2-backend.onrender.com`

- Exposes `/api/player-status` endpoint
- Maps player names to injury color codes from the Sleeper API

---

## 🛠 Tech Stack

**Frontend:** HTML5, CSS3, JavaScript  
**Backend:** Render-hosted REST API  
**Data Source:** Sleeper injury data  
**Storage:** Browser localStorage  

---

## 🧑‍💻 Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/jaydenuofc/playmaker-v2.git
cd playmaker-v2
```
<br><br>

### 2. Project Structure
```bash
playmaker-v2/
│
├── index.html       # Full app: HTML + CSS + JS
├── logo.png         # UI logo
├── screenshot.png   # App screenshot for README
└── README.md
```
<br><br>

### 3. Running Locally
You have two options:

Option A — Open Directly (Fastest)
Just open `index.html` in your browser.
<br>
Option B — Run a Local Server (Recommended)
Prevents CORS/API issues.
```bash
python -m http.server 8000
```

Then open:
```bash
http://localhost:8000/index.html
```
<br><br>

### 4. Backend Setup (Render)
The app uses a Render-hosted API for injury data.
Frontend references:
```bash
const API_BASE = "https://playmaker-v2-backend.onrender.com";
```
If your backend URL changes, update this constant inside `index.html`.

<br><br>

### 5. Resetting / Updating Roster Data
Roster changes are saved using browser `localStorage`.

To fully reset:
  Click Reset to default lineup
  or
  Clear `localStorage` in DevTools → Application → Local Storage

<br><br>

### 6. Deploying the App
You can deploy this static site on:
  GitHub Pages
  Vercel
  Netlify
  Render

<br><br>
---

### GitHub Pages Example:
  Push code:
  - Go to Settings → Pages
  - Choose “Deploy from Branch” → `main`
  - Your site goes live automatically

---

### Usage Guide
Open the app
1. Click Update injury status from backend
2. Review message colors (green/yellow/red)
3. Check Start/Sit recommendations
4. Modify roster or move players as needed
5. Ensure lineup follows required league structure

---

### Future Enhancements
- Projection and matchup-based recommendations
- Multi-team or multi-league support
- Mobile‑optimized layout
- Export/share lineup features

---

### Credits
Built by jaydenuofc for ENTI 633 using AI-assisted ideation, coding, iteration, and documentation.
Injury data is sourced from Sleeper through a custom backend deployed on Render.








