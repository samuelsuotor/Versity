from flask import Flask, render_template, request, abort, jsonify
from config import Config
from data import featured_projects, project_catalog

WHATSAPP_NUMBER = "2348143467785"
PROJECTS_PER_PAGE = 2

departments_data = [

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

    for department in departments_data:

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

    filtered_projects = project_catalog

    if search_query: 
        filtered_projects = [

            project

            for project in project_catalog

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

@app.route("/departments")
def departments():

    search_query = request.args.get("search", "").strip()

    departments_with_counts = []

    for department in departments_data:

        project_count = sum(
            1
            for project in project_catalog
            if project.get("department") == department["name"]
        )

        department_copy = department.copy()

        department_copy["projects"] = project_count

        departments_with_counts.append(department_copy)


    # ==========================================
    # SEARCH DEPARTMENTS
    # ==========================================

    if search_query:

        search_lower = search_query.lower()

        departments_with_counts = [

            department
            for department in departments_with_counts

            if (
                search_lower in department["name"].lower()
                or search_lower in department.get(
                    "description", ""
                ).lower()
            )

        ]


    total_department_projects = sum(
        department["projects"]
        for department in departments_with_counts
    )


    active_departments = sum(
        1
        for department in departments_with_counts
        if department["projects"] > 0
    )


    return render_template(

        "departments.html",

        departments=departments_with_counts,

        search_query=search_query,

        total_department_projects=total_department_projects,

        active_departments=active_departments,

        whatsapp_number=WHATSAPP_NUMBER

    )


@app.route("/departments/<department_slug>")
def department_projects(department_slug):

    department = next(

        (
            dept

            for dept in departments_data

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
        (p for p in project_catalog if p["slug"] == slug),
        None
    )

    if project is None:
        abort(404)

    related_projects = [
        p for p in project_catalog
        if p["slug"] != project["slug"]
        and p["department"] == project["department"]
    ][:4]

    if len(related_projects) < 4:
        related_projects = [
            p for p in project_catalog
            if p["slug"] != project["slug"]
            and p not in related_projects
        ][:4]

    return render_template(
        "project-details.html",
        project=project,
        related_projects=related_projects,
        whatsapp_number=WHATSAPP_NUMBER
    )

@app.route("/projects")
def all_projects():

    # ==================================================
    # GET FILTER VALUES FROM URL
    # ==================================================

    search = request.args.get("search", "").strip()

    department = request.args.get("department", "").strip()

    category = request.args.get("category", "").strip()

    technology = request.args.get("technology", "").strip()

    price = request.args.get("price", "").strip()

    sort = request.args.get("sort", "default").strip()

    page = request.args.get("page", 1, type=int)

    reset = request.args.get("reset", "").strip()


    # ==================================================
    # RESET FILTERS
    # ==================================================

    if reset:

        search = ""

        department = ""

        category = ""

        technology = ""

        price = ""

        sort = "default"

        page = 1


    # ==================================================
    # START WITH COMPLETE PROJECT CATALOG
    # ==================================================

    projects = project_catalog.copy()


    # ==================================================
    # SEARCH FILTER
    # ==================================================

    if search:

        search_lower = search.lower()

        projects = [

            project

            for project in projects

            if (

                search_lower in project.get("title", "").lower()

                or search_lower in project.get("department", "").lower()

                or search_lower in project.get("category", "").lower()

                or any(

                    search_lower in technology_name.lower()

                    for technology_name
                    in project.get("technology", [])

                )

            )

        ]


    # ==================================================
    # DEPARTMENT FILTER
    # ==================================================

    if department:

        projects = [

            project

            for project in projects

            if project.get("department", "").lower()
            == department.lower()

        ]


    # ==================================================
    # CATEGORY FILTER
    # ==================================================

    if category:

        projects = [

            project

            for project in projects

            if project.get("category", "").lower()
            == category.lower()

        ]


    # ==================================================
    # TECHNOLOGY FILTER
    # ==================================================

    if technology:

        projects = [

            project

            for project in projects

            if any(

                technology.lower()
                == technology_name.lower()

                for technology_name
                in project.get("technology", [])

            )

        ]


    # ==================================================
    # PRICE FILTER
    # ==================================================

    if price == "under_10000":

        projects = [

            project

            for project in projects

            if project.get("price", 0) < 10000

        ]

    elif price == "10000_20000":

        projects = [

            project

            for project in projects

            if 10000 <= project.get("price", 0) <= 20000

        ]

    elif price == "above_20000":

        projects = [

            project

            for project in projects

            if project.get("price", 0) > 20000

        ]


    # ==================================================
    # SORTING
    # ==================================================

    if sort == "az":

        projects.sort(

            key=lambda project:
            project.get("title", "").lower()

        )

    elif sort == "department":

        projects.sort(

            key=lambda project:
            project.get("department", "").lower()

        )

    elif sort == "price_low":

        projects.sort(

            key=lambda project:
            project.get("price", 0)

        )

    elif sort == "price_high":

        projects.sort(

            key=lambda project:
            project.get("price", 0),

            reverse=True

        )


    # ==================================================
    # BUILD DYNAMIC FILTER OPTIONS
    # ==================================================

    filter_departments = sorted({

        project.get("department")

        for project in project_catalog

        if project.get("department")

    })


    filter_categories = sorted({

        project.get("category")

        for project in project_catalog

        if project.get("category")

    })


    filter_technologies = sorted({

        technology_name

        for project in project_catalog

        for technology_name
        in project.get("technology", [])

        if technology_name

    })


    # ==================================================
    # PAGINATION
    # ==================================================

    total_projects = len(projects)

    total_pages = (

        total_projects
        + PROJECTS_PER_PAGE
        - 1

    ) // PROJECTS_PER_PAGE


    # Make sure there is always at least one page

    if total_pages == 0:

        total_pages = 1


    # Prevent invalid page numbers

    if page < 1:

        page = 1

    if page > total_pages:

        page = total_pages


    start = (page - 1) * PROJECTS_PER_PAGE

    end = start + PROJECTS_PER_PAGE

    paginated_projects = projects[start:end]


    # ==================================================
    # SEND DATA TO TEMPLATE
    # ==================================================

    return render_template(

        "all-projects.html",

        featured_projects=paginated_projects,

        current_sort=sort,

        current_page=page,

        total_pages=total_pages,

        total_projects=total_projects,

        current_search=search,

        current_department=department,

        current_category=category,

        current_technology=technology,

        current_price=price,

        filter_departments=filter_departments,

        filter_categories=filter_categories,

        filter_technologies=filter_technologies,

        whatsapp_number=WHATSAPP_NUMBER

    )

@app.route("/search-api")
def search_api():

    query = request.args.get("q", "").strip().lower()

    if not query:
        return jsonify([])

    query = query[:100]  # Limit query length to 100 characters

    try:

        results = []

        for project in project_catalog:

            technologies = " ".join(project.get("technology", []))

            searchable = " ".join([
                project.get("title", ""),
                project.get("department", ""),
                project.get("category", ""),
                technologies,
                project.get("description", "")
            ]).lower()

            if query in searchable:

                results.append({

                    "title": project["title"],
                    "department": project["department"],
                    "technology": ", ".join(project.get("technology", [])[:2]),
                    "slug": project["slug"]

                })

        return jsonify(results[:5])  # Limit to top 5 results

    except Exception:
        app.logger.exception("Search API error")
        return jsonify({
            "error": "Search is temporarily unavailable."
        }), 500

if __name__ == "__main__":
    app.run(port=5000, host="0.0.0.0", debug=True)