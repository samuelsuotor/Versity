from flask import Flask, render_template
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

@app.route("/")
def home():
    departments = [

        {
            "icon":"💻",
            "name":"Computer Science",
            "projects":128
        },

        {
            "icon":"⚙️",
            "name":"Software Engineering",
            "projects":74
        },

        {
            "icon":"🌐",
            "name":"Information Technology",
            "projects":59
        },

        {
            "icon":"🛡️",
            "name":"Cyber Security",
            "projects":41
        },

        {
            "icon":"💼",
            "name":"Business Administration",
            "projects":63
        },

        {
            "icon":"📊",
            "name":"Accounting",
            "projects":56
        },

        {
            "icon":"📈",
            "name":"Economics",
            "projects":38
        },

        {
            "icon":"📣",
            "name":"Marketing",
            "projects":27
        }

    ]

    featured_projects = [

    {
        "id":1,
        "title":"Fuel Price Prediction System",
        "department":"Computer Science",
        "technology":"Python • Flask • MySQL",
        "price":"₦15,000",
        "image":"project-placeholder.jpg"
    },

    {
        "id":2,
        "title":"Complaint & Maintenance Tracking System",
        "department":"Information Technology",
        "technology":"PHP • MySQL",
        "price":"₦18,000",
        "image":"project-placeholder.jpg"
    },

    {
        "id":3,
        "title":"Digital Queue Management System",
        "department":"Software Engineering",
        "technology":"Python • Flask",
        "price":"₦20,000",
        "image":"project-placeholder.jpg"
    },

    {
        "id":4,
        "title":"Student Marketplace Platform",
        "department":"Computer Science",
        "technology":"Python • Flask",
        "price":"₦22,000",
        "image":"project-placeholder.jpg"
    }
    ]
    
    return render_template(
        "index.html",
        departments=departments,
        featured_projects=featured_projects
    )

if __name__ == "__main__":
    app.run(port=5000, host="0.0.0.0", debug=True)