# Versity Design System

## Purpose

The Versity Design System defines the visual language of the platform.

While the Design Bible explains the philosophy behind the interface, this document specifies the exact implementation standards developers should follow.

Every page, component, and interaction must align with this system.

---

# Design Philosophy

The Versity interface follows one central belief:

> Good design should quietly help users accomplish their goals.

The interface should never compete with the user's task.

Instead, it should disappear into the background and make every interaction feel natural.

---

# Colour System

## Primary Brand

Royal Blue

```
#2563EB
```

Purpose

- Primary buttons
- Active navigation
- Links
- Icons
- Highlights

---

## Primary Hover

```
#1D4ED8
```

---

## Primary Active

```
#1E40AF
```

---

## Background

```
#FAFAFA
```

Purpose

Application background.

Avoid pure white whenever possible.

---

## Surface

```
#FFFFFF
```

Purpose

Cards

Dropdowns

Panels

Modals

---

## Primary Text

```
#111827
```

---

## Secondary Text

```
#6B7280
```

---

## Borders

```
#E5E7EB
```

---

## Success

```
#16A34A
```

---

## Warning

```
#F59E0B
```

---

## Error

```
#DC2626
```

---

# Typography

## Primary Font

Inter

Weights

300

400

500

600

700

---

## Heading Scale

H1

48px

---

H2

36px

---

H3

28px

---

H4

22px

---

H5

18px

---

Body

16px

---

Small Text

14px

---

Caption

12px

---

# Spacing System

Use a consistent spacing scale.

```
4px

8px

12px

16px

24px

32px

48px

64px

96px
```

Avoid arbitrary spacing values.

Spacing should feel rhythmic throughout the application.

---

# Border Radius

Buttons

10px

---

Inputs

10px

---

Cards

16px

---

Images

16px

---

Modals

20px

---

Badges

999px

---

# Shadows

Use shadows sparingly.

Level 1

```
0 2px 8px rgba(0,0,0,.05)
```

---

Level 2

```
0 8px 24px rgba(0,0,0,.08)
```

---

Level 3

Reserved for modals only.

```
0 20px 60px rgba(0,0,0,.12)
```

---

# Buttons

## Primary Button

Background

Primary Blue

Text

White

Hover

Primary Hover

Border Radius

10px

Transition

200ms

---

## Secondary Button

White background

Primary border

Primary text

---

## Danger Button

Error Red

Reserved for destructive actions.

---

# Inputs

Height

48px

Radius

10px

Border

Light Gray

Focus

Primary Blue

---

# Cards

Cards should contain:

- White background
- 16px radius
- Soft shadow
- Comfortable padding
- Clear hierarchy

Cards should never appear visually heavy.

---

# Icons

Icons should be:

Simple

Recognisable

Consistent

Avoid decorative icons.

Icons must support meaning.

---

# Motion

Animations should explain interactions.

Recommended durations

150ms

200ms

300ms

Avoid long animations.

---

Hover animations

Subtle scale

```
scale(1.02)
```

or

Small elevation.

Never dramatic movement.

---

# Breakpoints

Mobile

```
0–767px
```

Tablet

```
768–1023px
```

Laptop

```
1024–1439px
```

Desktop

```
1440px+
```

---

# Containers

Maximum Width

```
1200px
```

Horizontal Padding

Desktop

32px

Tablet

24px

Mobile

20px

---

# Section Spacing

Standard section spacing

Desktop

```
80px
```

Tablet

```
64px
```

Mobile

```
48px
```

Compact sections

```
32px
```

---

# Component Behaviour

Every reusable component must:

- Look identical wherever used.
- Behave identically wherever used.
- Use the same spacing rules.
- Use the same typography.
- Use the same animations.

Consistency is mandatory.

---

# Accessibility

Minimum text contrast should satisfy WCAG recommendations.

Interactive elements must include visible focus states.

Touch targets should be at least 44×44 pixels.

Navigation should be keyboard accessible wherever possible.

---

# Responsive Design

Responsive behaviour is not optional.

Every page should feel intentionally designed for:

- Mobile
- Tablet
- Laptop
- Desktop

Layouts should adapt naturally without breaking visual hierarchy.

---

# Future Expansion

As Versity evolves, this document will also define:

- Data tables
- Charts
- Dashboard widgets
- Notifications
- Toast messages
- Payment components
- Seller interface
- Admin interface

---

# Final Principle

Whenever a new component is designed, ask:

- Does it look like Versity?
- Does it behave like Versity?
- Would a user immediately recognise it as part of the same product?

If not, redesign it before implementation.

---

Last Updated

Version 1 Development
