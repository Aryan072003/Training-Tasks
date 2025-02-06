from flask import *
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

migrate = Migrate(app, db)

class Education(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    years = db.Column(db.String())
    degree = db.Column(db.String())
    university = db.Column(db.String)
    address = db.Column(db.String())
    description = db.Column(db.String)

class Experience(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    years = db.Column(db.String())
    post = db.Column(db.String())
    company = db.Column(db.String)
    address = db.Column(db.String())
    description = db.Column(db.String)

class Skills(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    skill = db.Column(db.String())
    knowledge = db.Column(db.String())

educations = [
    Education(
        years = "2008-2010",
        degree = "Master of computer engineering",
        university = "\nuniversity of north carolina\n",
        address = "North Carolina, USA",
        description = "Duis aute irure dolor in reprehenderit in vol patate velit esse cillum dolore eu fugiat nulla pari. Excepteur sint occana inna tecat cupidatat non proident."
),
    Education(
        years = "2004-2008",
        degree = "Bachelor of computer engineering",
        university = "\nuniversity of north carolina\n",
        address = "North Carolina, USA",
        description = "Duis aute irure dolor in reprehenderit in vol patate velit esse cillum dolore eu fugiat nulla pari. Excepteur sint occana inna tecat cupidatat non proident."
    ),
    Education(
        years = "2004-2008",
        degree = "Bachelor of creative design",
        university = "\nuniversity of bolton\n",
        address = "Bolton, UK",
        description = "Duis aute irure dolor in reprehenderit in vol patate velit esse cillum dolore eu fugiat nulla pari. Excepteur sint occana inna tecat cupidatat non proident."
)
]

experiences = [
  Experience(
    years = "2018-present",
    company = "hoplony tech limited\n",
    post = "creative director",
    address = "newyork, USA",
    description = "Duis aute irure dolor in reprehenderit in vol patate velit esse cillum dolore eu fugiat nulla pari. Excepteur sint occana inna tecat cupidatat non proident."
  ),
  Experience(
    years = "2016-2018",
    company = "hoplony tech limited\n",
    post = "associate design director",
    address = "newyork, USA",
    description = "Duis aute irure dolor in reprehenderit in vol patate velit esse cillum dolore eu fugiat nulla pari. Excepteur sint occana inna tecat cupidatat non proident."
  ),
  Experience(
    years = "2013-2016",
    company = "hoplony tech limited\n",
    post = "senior ui/ux designer",
    address = "newyork, USA",
    description = "Duis aute irure dolor in reprehenderit in vol patate velit esse cillum dolore eu fugiat nulla pari. Excepteur sint occana inna tecat cupidatat non proident."
  ),
  Experience(
    years = "2012-2013",
    company = "hoplony tech limited\n",
    post = "ui/ux designer",
    address = "newyork, USA",
    description = "Duis aute irure dolor in reprehenderit in vol patate velit esse cillum dolore eu fugiat nulla pari. Excepteur sint occana inna tecat cupidatat non proident."
  ),
  Experience(
    years = "2010-2012",
    company = "hoplony tech limited\n",
    post = "frontend developer",
    address = "newyork, USA",
    description = "Duis aute irure dolor in reprehenderit in vol patate velit esse cillum dolore eu fugiat nulla pari. Excepteur sint occana inna tecat cupidatat non proident."
  )
]

skills1 = [
    Skills(
        skill = "adobe photoshop",
        knowledge = "90%"
    ),
    Skills(
        skill = "adobe illustrator",
        knowledge = "85%"
    ),
    Skills(
        skill = "adobe after effects",
        knowledge = "97%"
    ),
    Skills(
        skill = "sketch",
        knowledge = "90%"
    )
]

skills2 = [
    Skills(
        skill = "html5",
        knowledge = "90%"
    ),
    Skills(
        skill = "css3 animation",
        knowledge = "85%"
    ),
    Skills(
        skill = "coomunication",
        knowledge = "97%"
    ),
    Skills(
        skill = "creativity",
        knowledge = "90%"
    )
]

def create_app():
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object("config.Config")
    db.init_app(app)

with app.app_context():
    db.create_all()
    db.session.add_all(educations)
    db.session.add_all(experiences)
    db.session.add_all(skills1)
    db.session.add_all(skills2)
    db.session.commit()
    education = Education.query.all()
    experience = Experience.query.all()
    skill = Skills.query.all()

@app.route('/')
def hello():
    return render_template("index.html", education = educations, skills1 = skills1, skills2 = skills2,  experience = experiences)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)