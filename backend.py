from flask import Blueprint, current_app, jsonify, redirect, request, url_for, render_template
import survey_logic

form_api = Blueprint("form", __name__, url_prefix="")


@form_api.route("/form", methods=["GET"])
def form_show():
    """Show user the login page
    """
    return render_template('form.html'), 200

@form_api.route("/")
def home_create():
    return render_template("home.html")

@form_api.route("/form", methods=["POST"])
def form_create():
    """Attempts to authorize the user
    """
    print(request.form)
    mentor_name = survey_logic.my_data(request.form)

    mentor1 = {
        'id': 'Laurel',
        'name': 'Laurel Hitchens',
        'position': 'Architect',
        'interests': 'Math, I love working in teams!, I prefer to use a logical approach, From home',
        'className': 'Laurel',
        'imageURL': "Architect.jpg"
    }

    mentor2 = {
        'id': 'Benjamin',
        'name': 'Benjamin Stewart',
        'position': 'Website Designer',
        'interests': 'Arts, I prefer to work alone, I prefer to go with my gut, From home',
        'className': 'Benjamin',
        'imageURL': "Web Designer.jpg"
    }

    mentor3 = {
        'id': 'Steven',
        'name': 'Steven Marrow',
        'position': 'College History Professor',
        'interests': 'English, Working in teams is okay, I prefer to go with my gut, In an office',
        'className': 'Steven',
        'imageURL': "Prof.jpg"
    }

    mentor4 = {
        'id': 'Sarah',
        'name': 'Sarah Powers',
        'position': 'Product Manager',
        'interests': 'Math, I love working in teams!, I prefer to use a logical approach, In an office',
        'className': 'Sarah',
        'imageURL': "Product Manager.jpeg"
    }

    mentor5 = {
        'id': 'Amanda',
        'name': 'Amanda Herrings',
        'position': 'Auto Repair Mechanic',
        'interests': 'Science, Working in teams is okay, I prefer to use a logical appraoch, Outside',
        'className': 'Amanda',
        'imageURL': "Mechanic.jpeg"
    }

    mentor6 = {
        'id': 'Joshua',
        'name': 'Joshua Argus',
        'position': 'Dietician',
        'interests': 'Science, I prefer to work alone, I prefer to go with my gut, In an office',
        'className': 'Joshua',
        'imageURL': "Dietician.jpg"
    }

    if mentor_name == mentor1['id']:
        mentor = mentor1
    elif mentor_name == mentor2['id']:
        mentor = mentor2
    elif mentor_name == mentor3['id']:
        mentor = mentor3
    elif mentor_name == mentor4['id']:
        mentor = mentor4
    elif mentor_name == mentor5['id']:
        mentor = mentor5
    else:
        mentor = mentor6

    return render_template('index.html', mentor=mentor), 200
