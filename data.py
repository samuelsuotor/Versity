featured_projects = [

    {
        "id": 1,
        "slug": "fuel-price-prediction-system",
        "title": "Fuel Price Prediction System",
        "department": "Computer Science",
        "category": "Machine Learning",
        "technology": [
            "Python",
            "Flask",
            "HTML",
            "CSS",
            "JavaScript"
        ],
        "price": 15000,
        "status": "completed",
        "software_images": [
            "fuel-price-1.png",
            "fuel-price-2.jpg",
            "fuel-price-3.jpg",
            "fuel-price-4.jpg"
        ],
        "report_preview_images": [
            "fuel-price-1.png",
            "fuel-price-2.jpg",
            "fuel-price-3.jpg",
            "fuel-price-4.jpg"
            ],
        "description": "An intelligent system that predicts future fuel prices using historical data and machine learning techniques.",
        "includes": [
            {
                "label": "Chapter 1–5 Microsoft Word Documentation",
                "available": True
            },
            {
                "label": "Complete Source Code",
                "available": True
            },
            {
                "label": "Database Files",
                "available": True
            },
            {
                "label": "Installation Guide",
                "available": True
            }
        ],
        "features": [
            "Accurate Fuel Price Predictions",
            "User-Friendly Interface",
            "Real-Time Data Analysis",
            "Customizable Prediction Models"
        ]
    },

    {
        "id":2,
        "slug": "complaint-maintenance-tracking-system",
        "title":"Complaint & Maintenance Tracking System",
        "department":"Information Technology",
        "technology":[
            "PHP",
            "MySQL"
        ],
        "category": "Data Science",
        "includes": [
            {
                "label": "Chapter 1–5 Microsoft Word Documentation",
                "available": True
            },
            {
                "label": "Complete Source Code",
                "available": True
            },
            {
                "label": "Database Files",
                "available": True
            },
            {
                "label": "Installation Guide",
                "available": True
            }
        ],
        "status": "completed",
        "price": 18000,
        "software_images": [
            "complaint-maintenance-1.webp",
            "complaint-maintenance-2.jpg",
            "complaint-maintenance-3.jpg",
            "complaint-maintenance-4.jpg"
        ],
        "report_preview_images": [
            "complaint-maintenance-1.webp",
            "complaint-maintenance-2.jpg",
            "complaint-maintenance-3.jpg",
            "complaint-maintenance-4.webp"
        ],
        "description": "A comprehensive system for tracking complaints and maintenance requests in real-time.",
        "features": [
            "Real-time Tracking",
            "Automated Notifications",
            "Comprehensive Reporting",
            "User-Friendly Interface"
        ]
    },

    {
        "id":3,
        "slug": "digital-queue-management-system",
        "title":"Digital Queue Management System",
        "department":"Software Engineering",
        "technology":[
            "Python",
            "Flask"
        ],
        "category": "Web Development",
        "includes": [
            {
                "label": "Chapter 1–5 Microsoft Word Documentation",
                "available": True
            },
            {
                "label": "Complete Source Code",
                "available": True
            },
            {
                "label": "Database Files",
                "available": True
            },
            {
                "label": "Installation Guide",
                "available": True
            }
        ],
        "status": "completed",
        "price": 20000,
        "software_images": [
            "digital-queue-1.webp",
            "digital-queue-2.jpg",
            "digital-queue-3.jpg",
            "digital-queue-4.jpg"
        ],
        "report_preview_images": [
            "digital-queue-1.webp",
            "digital-queue-2.jpg",
            "digital-queue-3.jpg",
            "digital-queue-4.jpg"
        ],
        "description": "A modern solution for managing queues in various settings.",
        "features": [
            "Digital Queue Management",
            "Real-time Updates",
            "User Notifications",
            "Analytics and Reporting"
        ]
    },

    {
        "id":4,
        "slug": "student-marketplace-platform",
        "title":"Student Marketplace Platform",
        "department":"Computer Science",
        "technology":[
            "Python",
            "Flask"
        ],
        "category": "Artificial Intelligence",
        "includes": [
            {
                "label": "Chapter 1–5 Microsoft Word Documentation",
                "available": True
            },
            {
                "label": "Complete Source Code",
                "available": True
            },
            {
                "label": "Database Files",
                "available": True
            },
            {
                "label": "Installation Guide",
                "available": True
            }
        ],
        "status": "completed",
        "price": 22000,
        "software_images": [
            "student-marketplace-1.png",
            "student-marketplace-2.jpg",
            "student-marketplace-3.jpg",
            "student-marketplace-4.jpg"
        ],
        "report_preview_images": [
            "student-marketplace-1.png",
            "student-marketplace-2.jpg",
            "student-marketplace-3.jpg",
            "student-marketplace-4.jpg"
        ],
        "description": "A platform for students to buy and sell used textbooks and supplies.",
        "features": [
            "Online Marketplace",
            "Secure Transactions",
            "User Reviews and Ratings",
            "Search and Filter Options"
        ]
    }
]


# --------------------------------------------------
# Development Seed Projects
# Remove before production

# --------------------------------------------------

demo_projects = []

for i in range(5, 25):

    base = featured_projects[(i - 1) % len(featured_projects)].copy()

    base["id"] = i

    base["title"] = f"{base['title']} ({i})"

    base["slug"] = f"{base['slug']}-{i}"

    demo_projects.append(base)

featured_projects.extend(demo_projects)

project_catalog = featured_projects.copy()

featured_projects = project_catalog[:4]