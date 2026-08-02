# Decision Log

## Purpose

This document records significant architectural, design, and product decisions made throughout the development of Versity.

Rather than relying on memory, every important decision is documented together with the reasoning behind it.

When future changes are proposed, this log should be consulted to understand why previous decisions were made.

---

# Decision #001

## Title

Build Versity as a Product, Not Just a Student Project

### Decision

Versity will be developed as a real software product intended for long-term growth.

### Reason

Building with real-world standards results in cleaner architecture, better maintainability, and a platform capable of evolving beyond academic requirements.

### Status

Active

---

# Decision #002

## Title

Adopt Agile Development

### Decision

Development follows sprint-based Agile methodology instead of the traditional Waterfall approach.

### Reason

Agile allows continuous improvement, easier testing, better documentation, and incremental delivery.

### Status

Active

---

# Decision #003

## Title

One Administrator Dashboard Only (Version 1)

### Decision

Version 1 contains only one dashboard.

This dashboard belongs exclusively to the administrator.

### Reason

Multiple dashboards increase development complexity without improving validation of the business model.

Version 1 focuses on validating the marketplace.

### Future

Student dashboards are planned for Version 3.

### Status

Active

---

# Decision #004

## Title

WhatsApp Purchasing

### Decision

Customers purchase projects through WhatsApp.

### Reason

WhatsApp is familiar, trusted, simple, and requires minimal infrastructure.

It allows the marketplace to validate demand before investing in automated payment systems.

### Future

Online payment automation belongs to Version 2.

### Status

Active

---

# Decision #005

## Title

Use Static Project Data During Version 1

### Decision

Projects are stored in data.py instead of a database.

### Reason

The current project catalogue is small.

Static data accelerates development and keeps the application simple.

### Future

Migration to a relational database will occur when business requirements justify it.

### Status

Active

---

# Decision #006

## Title

Reusable Components Everywhere

### Decision

Repeated interface elements must become reusable templates.

### Reason

Reusable components improve consistency, reduce duplication, and simplify maintenance.

### Examples

- Navigation
- Project Card
- Department Card
- Footer
- Back Button

### Status

Active

---

# Decision #007

## Title

Invisible Design

### Decision

Versity adopts "Invisible Design" as its core design philosophy.

### Reason

The interface should quietly support the user's goals rather than draw attention to itself.

### Status

Permanent

---

# Decision #008

## Title

Design Before Features

### Decision

Consistency and user experience take priority over rapidly adding new functionality.

### Reason

A polished product creates trust and reduces future redesign work.

### Status

Permanent

---

# Decision #009

## Title

Documentation First

### Decision

Major architectural and product decisions must be documented before or alongside implementation.

### Reason

Good documentation improves long-term maintainability and preserves development context.

### Status

Permanent

---

# Decision #010

## Title

Every Feature Must Belong to a Version

### Decision

No feature should be implemented simply because it is technically possible.

Every feature must align with the objectives of the current product version.

### Reason

This prevents feature creep and keeps development focused.

### Status

Permanent

---

# Adding Future Decisions

Each new decision should include:

- Decision Number
- Title
- Description
- Reason
- Future Impact (if applicable)
- Status

---

Last Updated

Version 1 Development
