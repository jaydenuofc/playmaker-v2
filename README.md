# PlayMaker V2 – Fantasy Start/Sit Helper

A simple web app that helps fantasy football managers decide who to start or sit using live injury data, lineup validation, and an easy drag-style starter/bench flow.

---

## Table of Contents

- [Overview](#overview)
- [Core Features](#core-features)
- [How It Works](#how-it-works)
- [Tech Stack](#tech-stack)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Lineup Rules](#lineup-rules)
- [How We Used AI](#how-we-used-ai)
- [Future Improvements](#future-improvements)
- [Credits](#credits)

---

## Overview

PlayMaker V2 is a fantasy lineup helper that focuses on **start/sit decisions based on injuries and roster structure**, not full projections.  
It gives a quick, color-coded view of who is healthy, who is risky, and where your lineup breaks roster rules.

---

## Core Features

- **Editable Roster**
  - Add custom players (name, team, position) and manage your own bench.
  - Delete players you don’t want and move them between **Starters** and **Bench**.

- **Injury-Based Status (Color Coded)**
  - Pulls live status data from a backend connected to the Sleeper API.
  - Uses a simple color system:
    - 🟢 **Healthy** – good to start  
    - 🟡 **Questionable** – be careful  
    - 🔴 **Out / IR** – sit candidates  

- **Start/Sit Recommendations**
  - Identifies **yellow/red starters** and suggests a **green bench player** of the **same position** (or FLEX rules when applicable).
  - Recommendations are **injury-only** (they don’t consider projections or matchup).

- **Risk Summary**
  - Shows a quick summary for your current starters:
    - X healthy, Y questionable, Z out/IR.
  - Lets you quickly see how “risky” your lineup is this week.

- **Lineup Validation**
  - Enforces a specific starting lineup format and flags errors if you break it.
  - Highlights invalid starters and shows an error message when the lineup has too many players at a position.

- **Local Storage**
  - Your roster edits and lineup changes are saved in `localStorage`.
  - When you refresh, your last lineup and custom players are restored.

---

## How It Works

- **Frontend**
  - A single-page app built with **HTML, CSS, and vanilla JavaScript**.
  - Renders two lists: **Starters** and **Bench**, with buttons to move or delete players.
  - Applies styling to show health status, invalid starters, and recommendations.

- **Backend**
  - A backend deployed on **Render** at:  
    `https://playmaker-v2-backend.onrender.com`
  - Provides an endpoint that returns current player injury status based on names, powered by the Sleeper API.

---

## Tech Stack

- **Frontend**
  - HTML5
  - CSS3
  - Vanilla JavaScript (no frameworks)

- **Backend**
  - Render-hosted REST API
  - Integrates with the **Sleeper** platform for player injury data

- **Storage**
  - Browser `localStorage` for saving roster and lineup state

---

## Getting Started

### 1. Clone the Repo

```bash
git clone https://github.com/<your-username>/<your-repo-name>.git
cd <your-repo-name>
