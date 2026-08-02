# UI Component Guide

## Purpose

This document defines every reusable user interface component used throughout Versity.

The goal is to ensure visual consistency, predictable behaviour, and maintainability as the application grows.

Whenever a new component is introduced, it should be documented here.

---

# Design Philosophy

Every component must follow the principles defined in the Design Bible.

Components should be:

- Simple
- Reusable
- Predictable
- Accessible
- Responsive

A component should solve one problem well.

---

# Navigation Bar

## Purpose

Provides primary navigation throughout the platform.

---

## Includes

- Versity logo
- Desktop navigation
- Search button
- Browse Projects button
- Mobile hamburger menu

---

## Behaviour

Desktop

- Full navigation visible

Mobile

- Hamburger menu
- Slide-down navigation
- Touch-friendly spacing

---

## Rules

Always remains consistent across every page.

---

# Hero Section

## Purpose

Introduces the platform and guides users toward searching or browsing.

---

## Includes

- Main heading
- Supporting description
- Search bar
- Primary call-to-action
- Statistics

---

## Behaviour

Desktop

Two-column layout

Mobile

Single-column layout

Reduced vertical spacing

---

# Search Bar

## Purpose

Allows users to quickly locate projects.

---

## Used On

- Homepage
- Browse All Projects
- Search Results

---

## Behaviour

- Accepts keywords
- Searches title
- Searches department
- Searches category
- Searches technology

---

## Rules

Appearance must remain identical everywhere.

---

# Department Card

## Purpose

Represents a department.

---

## Contains

- Department icon
- Department name
- Project count
- Navigation

---

## Behaviour

Hover

- Slight elevation
- Soft shadow
- Cursor feedback

---

## Rules

Cards should always have identical sizing and spacing.

---

# Project Card

## Purpose

Displays a project summary.

---

## Contains

- Project image
- Department badge
- Project title
- Description
- Technology badges
- Price
- Preview button

---

## Behaviour

Entire card is clickable.

Hover effects are subtle.

Buttons remain consistent.

---

## Rules

Never duplicate project card markup.

Always use the reusable partial.

---

# Technology Badge

## Purpose

Highlights technologies used within a project.

Examples

- Python
- Flask
- HTML
- CSS
- JavaScript

---

## Behaviour

Static.

No hover animation required.

---

# Purchase Box

## Purpose

Displays purchasing information.

---

## Contains

- Price
- Purchase button
- WhatsApp action

---

## Behaviour

Primary purchase action should always remain visually dominant.

---

# Report Preview Card

## Purpose

Introduces report preview functionality.

---

## Contains

- Icon
- Description
- Preview button

---

## Future

Will later support document preview modal.

---

# Back Button

## Purpose

Returns users to their previous location.

---

## Behaviour

Uses browser history when available.

Falls back to the homepage if no previous history exists.

---

## Rules

Should appear consistently across all internal pages.

---

# Breadcrumb Navigation

## Purpose

Shows the user's current location.

Example

Home

>

Projects

>

Fuel Price Prediction System

---

## Rules

Only appears where appropriate.

Should never replace the Back button.

The Back button is the primary navigation aid.

---

# Buttons

## Primary

Used for the main action.

Examples

- Browse Projects
- Purchase Project
- Search

---

## Secondary

Used for supporting actions.

Examples

- Learn More
- Preview Report

---

## Future Buttons

Success

Warning

Danger

Outlined

Disabled

---

# Empty State

## Purpose

Provides feedback when no data exists.

Examples

- No search results
- No department projects

---

## Behaviour

Should always guide users toward their next action.

Never leave users at a dead end.

---

# Footer

## Purpose

Provides secondary navigation and company information.

Future additions include

- Contact
- Policies
- Social media
- Copyright
- Quick links

---

# Responsive Behaviour

Every component must work correctly on:

- Mobile
- Tablet
- Laptop
- Desktop

Responsiveness is a requirement, not an enhancement.

---

# Component Principles

Every component should satisfy these questions:

- Does it have one responsibility?
- Can it be reused?
- Is it visually consistent?
- Is it accessible?
- Does it follow the Design Bible?

If the answer to any question is "No", the component should be improved.

---

Last Updated

Version 1 Development
