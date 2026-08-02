from flask import Flask, render_template, request, abort, jsonify
from config import Config
from data import featured_projects, project_catalog

WHATSAPP_NUMBER = "2348143467785"
PROJECTS_PER_PAGE = 2

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

            for project in project_catalog

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

@app.route("/projects")
def all_projects():

    sort = request.args.get("sort", "default")

    page = request.args.get("page", 1, type=int)

    projects = project_catalog.copy()

    if sort == "az":

        projects.sort(
            key=lambda project: project["title"]
        )

    elif sort == "department":

        projects.sort(
            key=lambda project: project["department"]
        )

    elif sort == "price_low":

        projects.sort(
            key=lambda project: project["price"]
        )

    elif sort == "price_high":

        projects.sort(
            key=lambda project: project["price"],
            reverse=True
        )

    total_projects = len(projects)

    total_pages = (
        total_projects + PROJECTS_PER_PAGE - 1
    ) // PROJECTS_PER_PAGE

    start = (page - 1) * PROJECTS_PER_PAGE

    end = start + PROJECTS_PER_PAGE

    paginated_projects = projects[start:end]

    return render_template(

        "all-projects.html",

        featured_projects=paginated_projects,

        current_sort=sort,

        current_page=page,

        total_pages=total_pages,

        whatsapp_number=WHATSAPP_NUMBER

    )

if __name__ == "__main__":
    app.run(port=5000, host="0.0.0.0", debug=True)