# System Architecture

## Purpose

This document describes the architecture of the Versity platform.

It explains how the project is organised, how data flows through the application, and how the frontend and backend interact.

The objective is to make the project easy to understand, maintain, and extend.

---

# Architecture Overview

Versity follows a traditional server-side rendered architecture using Flask.

The application uses reusable templates, dynamic routing, and shared UI components to maintain consistency throughout the platform.

```
                Browser
                    │
                    ▼
              Flask Application
                    │
        ┌───────────┴───────────┐
        ▼                       ▼
     Routing                 Data Layer
        │                       │
        ▼                       ▼
   Jinja Templates         data.py
        │
        ▼
 Reusable Components
        │
        ▼
 HTML + CSS + JavaScript
        │
        ▼
     User Interface
```

---

# Technology Stack

## Backend

- Python
- Flask

---

## Frontend

- HTML5
- CSS3
- JavaScript (Vanilla)

---

## Template Engine

- Jinja2

---

## Data Storage (Current)

Project information is currently stored in:

```
data.py
```

This simplifies development during Version 1.

Future versions may migrate to a relational database.

---

# Folder Structure

```
VERSITY/

│
├── app.py
├── config.py
├── data.py
├── requirements.txt
│
├── docs/
│
├── static/
│   ├── css/
│   ├── js/
│   └── images/
│
├── templates/
│   ├── layouts/
│   ├── partials/
│   ├── index.html
│   ├── project-details.html
│   ├── project-results.html
│   └── all-projects.html
│
└── ...
```

---

# Backend Architecture

The backend is responsible for:

- Processing requests
- Routing users
- Loading project data
- Searching projects
- Filtering departments
- Rendering templates

Business logic is intentionally kept simple during Version 1.

---

# Frontend Architecture

The frontend is composed of reusable templates.

Rather than duplicating markup across pages, shared interface elements are separated into partial templates.

Examples include:

- Navigation
- Project Cards
- Department Cards
- Search Components
- Footer
- Back Button

This improves maintainability and consistency.

---

# CSS Architecture

Styles are separated by responsibility.

Current organisation includes:

```
css/

variables.css

style.css

animations.css
```

Future versions may further modularise styles as the application grows.

---

# JavaScript Architecture

Client-side behaviour is centralised within:

```
app.js
```

Responsibilities include:

- Mobile navigation
- Gallery interactions
- Hero animations
- Search interactions
- Component behaviour

Future functionality should continue to favour reusable functions over duplicated code.

---

# Data Flow

The typical request flow is:

```
User

↓

Flask Route

↓

Business Logic

↓

Project Data

↓

Template Rendering

↓

HTML Response

↓

Browser
```

---

# Component Architecture

Versity is built around reusable components.

Examples include:

- Navigation
- Hero
- Department Card
- Project Card
- Purchase Box
- Search Bar
- Footer

Every new component should be designed for reuse whenever possible.

---

# Design Philosophy

The technical architecture supports the principles defined in the Design Bible.

The primary architectural goals are:

- Simplicity
- Consistency
- Maintainability
- Scalability
- Reusability

Every new feature should strengthen these principles rather than introduce unnecessary complexity.

---

# Future Evolution

As the platform grows, the architecture is expected to evolve.

Possible future improvements include:

- Database integration
- Service layer
- Repository pattern
- REST API
- Authentication module
- Background task processing

These improvements will only be introduced when they align with the current Version Strategy.

---

Last Updated

Version 1 Development
