#  TravelMind – AI Travel Planning Agent

TravelMind is an AI-powered travel planning assistant that helps users generate personalized travel packages based on their destination, travel dates, budget, and number of travelers.

The application uses LangGraph to orchestrate an AI agent that searches for flights and hotels, recommends multiple travel packages, and allows users to approve a package and automatically create a Google Calendar event.

##  Live Demo

**Website:** https://travelmind.software

---

##  Features

* 🤖 AI-powered travel planning
* ✈️ Flight search integration
* 🏨 Hotel search integration
* 💰 Budget-aware package recommendations
* 📦 Multiple package options
* 📅 Google Calendar event creation
* 🧠 Conversation memory using LangGraph
* 🖼️ Destination images
* 🌐 Custom domain with HTTPS
* 🔄 Automatic deployment using GitHub Actions

---

##  Tech Stack

### Frontend

* Streamlit

### AI Framework

* LangGraph
* LangChain

### Backend

* Python

### APIs

* Flight API
* Hotel API
* Google Calendar API

### Deployment

* Microsoft Azure Ubuntu VM
* Nginx Reverse Proxy
* GitHub Actions (CI/CD)
* Let's Encrypt SSL
* Custom Domain

---

##  Project Architecture

```text
User
   │
   ▼
Streamlit Frontend
   │
   ▼
LangGraph AI Agent
   │
   ├── Flight Tool
   ├── Hotel Tool
   └── Google Calendar Tool
   │
   ▼
Travel Packages
   │
   ▼
Package Approval
   │
   ▼
Google Calendar Event
```

---

## ⚙️ Local Installation

Clone the repository:

```bash
git clone https://github.com/zainameen335/travel-agent.git
cd travel-agent
```

Create a virtual environment:

```bash
python -m venv ai_env
```

Activate the environment:

### Windows

```bash
ai_env\Scripts\activate
```

### Linux

```bash
source ai_env/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file and configure your API keys.

Run the application:

```bash
streamlit run frontend.py
```

---

##  Deployment

This project is deployed on:

* Microsoft Azure Ubuntu VM
* Nginx Reverse Proxy
* HTTPS using Let's Encrypt
* Custom Domain
* GitHub Actions CI/CD for automatic deployment

Every push to the `main` branch automatically deploys the latest version to the Azure server.

---

##  Project Structure

```text
travel-agent/
│
├── assets/
├── tools/
│   ├── flight_tool.py
│   ├── hotel_tool.py
│   └── calendar_tool.py
│
├── frontend.py
├── backend.py
├── agent.py
├── requirements.txt
└── README.md
```

---

##  Environment Variables

The following sensitive files are excluded from version control:

* `.env`
* `credentials.json`
* `token.json`

---

## 📌 Future Improvements

* Currency conversion for accurate total package cost
* Flight booking integration
* Hotel booking integration
* User authentication
* Trip history
* Email itinerary sharing

---

##  Author

**Zain Ameen**

GitHub: https://github.com/zainameen335

LinkedIn: https://www.linkedin.com/in/zainameen335/

