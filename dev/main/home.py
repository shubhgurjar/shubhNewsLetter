from flask import render_template, request, Blueprint, jsonify
from dev.models.db_model import User, db

main = Blueprint('main', __name__)

@main.route("/")
@main.route("/home")
def home():
    return render_template("home.html")


#Setting route to about page
@main.route("/about")
def about():
    # return "<h1>About Page</h1>"
    return render_template('about.html', title='About')

@main.route('/create_user', methods=['POST'])
def create_user():
    data = request.get_json()
    new_user = User(username=data['username'], email=data['email'], password=data['password'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User created successfully'}), 201

@main.route('/get_users', methods=['GET'])
def get_users():
    users = User.query.all()
    output = []
    for user in users:
        user_data = {
            'id': user.id,
            'username': user.username,
            'email': user.email
        }
        output.append(user_data)
    return jsonify({'users': output}), 200