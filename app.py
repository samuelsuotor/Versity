from flask import Flask, render_template
from config import Config
from flask import abort
from data import featured_projects

WHATSAPP_NUMBER = "2348143467785"

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

    
    return render_template(

        "index.html",

        departments=departments,

        featured_projects=featured_projects

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