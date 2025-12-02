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


