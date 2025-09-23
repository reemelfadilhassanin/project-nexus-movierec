
# Movie Recommendation Backend — Project Nexus (ProDev BE)

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)]()
[![CI](https://img.shields.io/badge/CI-GitHub%20Actions-lightgrey.svg)]()

## Overview

A backend API for a **Movie Recommendation** application, built as part of **Project Nexus (ProDev Backend)**.
It provides endpoints for trending movies, personalized recommendations, JWT-based authentication, user favorites, Redis caching, and auto-generated API docs.

---

## Demo & Deliverables

- **ERD diagram:** ()
- **Demo video (≤ 5 min):** (🔗 )
- **Slides:** (🔗 )
- **Hosted API (if deployed):** (🔗)

---

## Tech Stack

- **Language:** Python 3.11+
- **Framework:** Django 4.x, Django REST Framework
- **Auth:** djangorestframework-simplejwt (JWT)
- **Database:** PostgreSQL
- **Cache:** Redis
- **External API:** [TMDb](https://www.themoviedb.org/) (The Movie Database)
- **Docs:** Swagger UI (drf-yasg) / drf-spectacular
- **Containerization / Dev:** Docker & docker-compose
- **CI/CD:** GitHub Actions

---

## Quickstart (Docker)

1. Copy environment variables:
   ```bash
   cp .env.example .env
   ```
