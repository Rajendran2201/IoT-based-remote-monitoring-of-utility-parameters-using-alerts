# Contributing to Factory ML Dashboard

Thank you for considering contributing to the **Factory ML Dashboard** project!  
We welcome all kinds of contributions — from bug fixes and new features to documentation and ideas.

---

## Table of Contents

- [Project Overview](#-project-overview)
- [How to Contribute](#-how-to-contribute)
- [Project Structure](#-project-structure)
- [Guidelines](#-guidelines)
- [Tech Stack](#-tech-stack)
- [Questions](#-questions)

---

## Project Overview

This project is a web-based industrial monitoring system with predictive analytics for:
- Emission forecasting
- Equipment fault detection
- Filter clogging detection
- Tank overfilling prediction

It uses **Next.js** for the frontend and **FastAPI** with ML models in the backend.

---

## How to Contribute

### 1. Fork the repository

Click the **Fork** button on the top right corner of this page.

### 2. Clone your fork

```bash
git clone https://github.com/Rajendran2201/IoT-based-remote-monitoring-of-utility-parameters-using-alerts.git
```

### 3. Create a new branch
̌
```bash
git checkout -b your-feature-name
```

### 4. Make your changes

* Add new features, fix bugs, or update documentation.
* Please keep commits clean and descriptive.

### 5. Commit and push

```bash
git add .
git commit -m "Add: [Short description of your change]"
git push origin your-feature-name
```

### 6. Open a Pull Request

* Go to your forked repo
* Click **Compare & Pull Request**
* Describe your changes and submit

---

## Project Structure

```
factory-ml-dashboard/
├── backend/          # FastAPI + ML models
├── src/              # Next.js frontend
│   ├── app/
│   ├── components/
│   ├── styles/
│   └── types/
├── public/
├── .env.example
├── README.md
├── CONTRIBUTING.md
```

---

## Guidelines

* Use clear, consistent naming conventions.
* Format your code (use Prettier or ESLint).
* Keep UI clean and consistent with Tailwind styles.
* Write meaningful commit messages.
* Avoid pushing `.env`, `node_modules/`, or model files.

---

## Tech Stack

| Layer                     | Technology           |
| ------------------------- | -------------------- |
| **Frontend**              | **Next.js, Tailwind CSS, TypeScript**          |
| **Charts & Dashboard UI** | Grafana              |
| **Backend**               | **FastAPI** (Python) |
| **Machine Learning**      | relevant ML models   |
| **Authentication**        | **Firebase Auth**    |
| **Hosting / DevOps**      | Render               |
| **Optional (Edge/IoT)**   | Raspberry PI         |
---

## Questions?

Have questions or suggestions?
Open an issue or contact the maintainer.

Happy coding! 💙

