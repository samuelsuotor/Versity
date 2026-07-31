from flask import Flask, render_template, request, abort, jsonify
from config import Config
from data import featured_projects

WHATSAPP_NUMBER = "2348143467785"

departments = [

        {
            "icon":"💻",
            "name":"Computer Science",
            "slug":"computer-science",
        
       },

        {
            "icon":"⚙️",
            "name":"Software Engineering",
            "slug":"software-engineering",
            
        },

        {
            "icon":"🌐",
            "name":"Information Technology",
            "slug":"information-technology",
            
        },

        {
            "icon":"🛡️",
            "name":"Cyber Security",
            "slug":"cyber-security",
            
        },

        {
            "icon":"💼",
            "name":"Business Administration",
            "slug":"business-administration",
            
        },

        {
            "icon":"📊",
            "name":"Accounting",
            "slug":"accounting",
            
        },

        {
            "icon":"📈",
            "name":"Economics",
            "slug":"economics",
            
        },

        {
            "icon":"📣",
            "name":"Marketing",
            "slug":"marketing",
            
        }

    ]

app = Flask(__name__)
app.config.from_object(Config)


@app.route("/")
def home():
    
    departments_with_counts = []

    for department in departments:

        project_count = sum(

            1

            for project in featured_projects

            if project["department"] == department["name"]

        )

        department_copy = department.copy()

        department_copy["projects"] = project_count

        departments_with_counts.append(department_copy)

    return render_template(

        "index.html",

        departments=departments_with_counts,

        featured_projects=featured_projects,

        whatsapp_number=WHATSAPP_NUMBER

    )

@app.route("/search")
def search_projects():

    search_query = request.args.get("search", "").strip()

    filtered_projects = featured_projects

    if search_query:

        filtered_projects = [

            project

            for project in featured_projects

            if (

                search_query.lower() in project["title"].lower()

                or search_query.lower() in project["department"].lower()

                or search_query.lower() in project["category"].lower()

                or any(

                    search_query.lower() in technology.lower()

                    for technology in project["technology"]

                )

            )

        ]

    return render_template(

        "project-results.html",

        featured_projects=filtered_projects,

        search_query=search_query,

        page_title="Search Results",

        whatsapp_number=WHATSAPP_NUMBER

    )

@app.route("/departments/<department_slug>")
def department_projects(department_slug):

    department = next(

        (
            dept

            for dept in departments

            if dept["slug"] == department_slug

        ),

        None

    )

    if not department:

        abort(404)

    filtered_projects = [

        project

        for project in featured_projects

        if project["department"] == department["name"]

    ]

    return render_template(

        "project-results.html",

        featured_projects=filtered_projects,

        page_title=department["name"],

        page_description=f"Showing {len(filtered_projects)} project(s) from the {department['name']} department.",

        search_query="",

        whatsapp_number=WHATSAPP_NUMBER

    )

@app.route("/projects/<slug>")
def project_details(slug):

    project = next(

        (p for p in featured_projects if p["slug"] == slug),

        None

    )

    if project is None:
        abort(404)

    return render_template(
        "project-details.html",
        project=project,
        whatsapp_number=WHATSAPP_NUMBER
    )

if __name__ == "__main__":
    app.run(port=5000, host="0.0.0.0", debug=True)