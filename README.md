
# Movie Recommendation Backend — Project Nexus (ProDev BE)

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)]()
[![CI](https://img.shields.io/badge/ci-GitHub%20Actions-lightgrey.svg)]()

## Overview

A backend API for a Movie Recommendation application built for **Project Nexus (ProDev Backend)**.
Features: trending & recommended movies (TMDb), JWT authentication, user favorites, Redis caching, Swagger documentation.

## Demo & Deliverables

- ERD diagram: (link to Lucidchart / draw.io)
- Demo video (≤ 5 min): (link to recorded demo)
- Slides: (Google Slides link)
- Hosted API: (link if deployed)

> Make sure the links above are accessible to reviewers/mentors.

## Tech stack

- **Language:** Python 3.11+
- **Framework:** Django 4.x, Django REST Framework
- **Auth:** djangorestframework-simplejwt (JWT)
- **DB:** PostgreSQL
- **Cache:** Redis
- **External API:** TMDb (The Movie Database)
- **Docs:** Swagger (drf-yasg) or drf-spectacular
- **Containerization / Dev:** Docker, docker-compose
- **CI:** GitHub Actions

## Quickstart (Docker)

1. Copy `.env.example` → `.env` and fill values (especially `TMDB_API_KEY`).
2. Build & run:

```bash
docker-compose up --build -d
docker compose exec web python manage.py migrate
docker compose exec web python manage.py createsuperuser
```
