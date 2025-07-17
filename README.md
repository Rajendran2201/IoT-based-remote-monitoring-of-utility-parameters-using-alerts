# Remote monitoring of Utility Parameters

A full-stack web application that provides real-time monitoring and predictive analytics for industrial operations. The dashboard uses machine learning models to predict:

1. Greenhouse gas (GHG) emissions  
2. Equipment faults in motors and pumps  
3. Filter clogging in filtration units  
4. Tank overfilling and inventory levels

Built with **Next.js**, **FastAPI**, and **Tailwind CSS**, this system empowers plant operators and analysts with actionable insights through an interactive dashboard.

---

##  Features

- Live dashboard with charts and alerts
- Predictive insights from trained ML models
- Fault detection in pumps and motors
- Emission estimation based on utility parameters
- Filter clogging detection via pressure anomalies
- Tank overfilling alerts using level and flow rate analysis
- Secure API integration and environment-based config

---

##  Tech Stack

| Layer       | Technology        |
|-------------|-------------------|
| Frontend    | Next.js, Tailwind CSS, Recharts |
| Backend     | FastAPI, Python |
| ML Models   | scikit-learn, RandomForestRegressor |
| Database    | MongoDB  |
| Visualization | Grafana (iframe embedding) |
| Deployment  |Render|

---


## Architecture

```mermaid
graph TD
    A[Sensor Data Sources<br>Voltage, Pressure, Flow, Level, etc.] -->|Streaming / Upload| B[FastAPI Backend]

    B --> C1[Emission Prediction]
    B --> C2[Fault Detection]
    B --> C3[Filter Clogging Detection]
    B --> C4[Tank Overflow Prediction]

    B --> D[Database]
    B --> E[REST API Endpoints]

    E --> F[Next.js Frontend Dashboard]
    F --> G1[Realtime Charts]
    F --> G2[Alerts & Notifications]
    F --> G3[Grafana Panels]

    style A fill:#fdf6e3,stroke:#b58900,stroke-width:2px
    style B fill:#eee8d5,stroke:#268bd2,stroke-width:2px
    style C1 fill:#e0f7fa,stroke:#00796b,stroke-width:2px
    style C2 fill:#e0f7fa,stroke:#00796b,stroke-width:2px
    style C3 fill:#e0f7fa,stroke:#00796b,stroke-width:2px
    style C4 fill:#e0f7fa,stroke:#00796b,stroke-width:2px
    style D fill:#f3e5f5,stroke:#6a1b9a,stroke-width:2px
    style E fill:#dcedc8,stroke:#558b2f,stroke-width:2px
    style F fill:#d0f0fd,stroke:#01579b,stroke-width:2px
    style G1 fill:#ffffff,stroke:#424242,stroke-width:1px
    style G2 fill:#ffffff,stroke:#424242,stroke-width:1px
    style G3 fill:#ffffff,stroke:#424242,stroke-width:1px


```
