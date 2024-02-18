from flask import render_template, request, Blueprint, jsonify
from dev.users.forms import RegistrationForm

users = Blueprint('users', __name__)


@users.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    # if form.validate_on_submit():
    #     hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
    #     user = User(username=form.username.data, email=form.email.data, password=hashed_password)
    #     db.session.add(user)
    #     db.session.commit()
    #     flash(f'Your account has been created! You are now able to log in', 'success')
    #     return redirect(url_for('users.login'))
    return render_template('register.html', title='Register', form=form)