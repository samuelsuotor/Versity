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
    return render_template(
        "index.html",
        departments=departments
    )

if __name__ == "__main__":
    app.run(port=5000, host="0.0.0.0", debug=True)