# Coding Standards

## Purpose

This document defines the coding standards used throughout the Versity project.

Its objective is to ensure that every file, function, template, and component follows a consistent style regardless of when it was written.

Consistency improves readability, maintainability, scalability, and collaboration.

---

# General Principles

Every line of code should satisfy the following principles:

- Readability over cleverness.
- Consistency over personal preference.
- Simplicity over unnecessary complexity.
- Reusability over duplication.
- Maintainability over shortcuts.

Code should be written for future developers, including your future self.

---

# Project Structure

Application files should remain organised by responsibility.

```
app.py
```

Contains:

- Flask routes
- Application entry point
- View rendering

---

```
config.py
```

Contains:

- Application configuration
- Environment settings
- Global constants

---

```
data.py
```

Contains:

- Project data
- Department data
- Static application data

Business logic should not be placed inside data.py.

---

# Python Standards

## Naming

Variables

Use:

```python
project_title
department_name
featured_projects
```

Avoid:

```python
ProjectTitle
projectTitle
PT
```

---

Functions

Use descriptive names.

Good:

```python
search_projects()
department_projects()
project_details()
```

Avoid:

```python
search()
run()
page()
```

---

Constants

Use uppercase.

Example:

```python
WHATSAPP_NUMBER

PROJECTS_PER_PAGE
```

---

Routes

Each route should have one clear responsibility.

Avoid combining unrelated logic inside a single route.

---

# Template Standards

Templates should remain clean.

Business logic belongs in Python whenever possible.

Templates should primarily handle presentation.

---

Reusable Components

If a block appears more than once, move it into:

```
templates/partials/
```

Examples:

- Project Card
- Department Card
- Navigation
- Footer
- Back Button

Avoid duplicating markup.

---

Layout

Every page should extend:

```
layouts/base.html
```

Never duplicate the base layout.

---

# HTML Standards

Use semantic HTML whenever possible.

Preferred:

```
<header>

<nav>

<main>

<section>

<article>

<footer>
```

Avoid unnecessary wrapper divs.

---

Indentation

Use consistent indentation throughout every template.

Nested elements should remain visually easy to follow.

---

Accessibility

Whenever possible:

- Use descriptive button text.
- Provide image alt text.
- Use aria-label where appropriate.
- Maintain logical heading hierarchy.

---

# CSS Standards

The Design Bible is the authority.

Every stylesheet must follow it.

---

Colours

Never hardcode colours unless absolutely necessary.

Use variables defined in:

```
variables.css
```

---

Spacing

Spacing should follow a consistent scale.

Avoid arbitrary values whenever possible.

Preferred spacing system:

```
4px

8px

12px

16px

24px

32px

48px

64px
```

---

Border Radius

Follow the Design Bible.

Buttons

10px

Inputs

10px

Cards

16px

Modals

20px

---

Animations

Animations must have purpose.

They should:

- Explain interaction
- Improve feedback
- Never distract

---

# JavaScript Standards

Current JavaScript resides in:

```
app.js
```

As functionality grows, organise related behaviour into clearly separated sections.

---

Naming

Use camelCase.

Example:

```javascript
mainPreview

heroSearch

departmentCards
```

---

Functions

Each function should perform one responsibility.

Avoid extremely large functions.

---

Events

Keep event listeners grouped logically.

Example:

Navigation

↓

Hero

↓

Gallery

↓

Search

↓

Utilities

---

# Reusability

Before writing new code, ask:

Can this already be reused?

If yes,

reuse it.

If no,

create a reusable component.

Avoid duplication.

---

# Documentation

Major changes should also update:

- CHANGELOG.md
- SPRINT_PROGRESS.md

When architecture changes significantly, update:

- ARCHITECTURE.md

---

# Git Standards

Each commit should represent one logical change.

Good examples:

```
Improve project card layout

Add pagination

Refactor search functionality

Fix mobile navigation
```

Avoid commits such as:

```
Update

Fix

Changes

Final
```

Commit messages should clearly explain what changed.

---

# Final Rule

Before committing code, ask:

- Is it readable?
- Is it reusable?
- Is it consistent?
- Does it follow the Design Bible?
- Would another developer immediately understand it?

If the answer to any question is "No", improve the code before committing.

---

Last Updated

Version 1 Development