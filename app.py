from flask import Flask, request, jsonify, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'


users = []

class UserForm(FlaskForm):
    id = IntegerField('ID', validators=[DataRequired()])
    name = StringField('Nome', validators=[DataRequired()])
    submit = SubmitField('Salvar')

@app.route('/')
def home():
    return render_template('home.html', users=users)

@app.route('/add', methods=['GET', 'POST'])
def add_user():
    form = UserForm()
    if form.validate_on_submit():
        user = {'id': form.id.data, 'name': form.name.data}
        users.append(user)
        return redirect(url_for('home'))
    return render_template('add_user.html', form=form)

@app.route('/update/<int:user_id>', methods=['GET', 'POST'])
def update_user(user_id):
    user = next((u for u in users if u['id'] == user_id), None)
    if user:
        form = UserForm()
        if form.validate_on_submit():
            user['name'] = form.name.data
            return redirect(url_for('home'))
        form.id.data = user['id']
        form.name.data = user['name']
        return render_template('update_user.html', form=form)
    return redirect(url_for('home'))

@app.route('/delete/<int:user_id>')
def delete_user(user_id):
    global users
    users = [u for u in users if u['id'] != user_id]
    return redirect(url_for('home'))

@app.route('/data')
def data():
    return jsonify(users)

if __name__ == '__main__':
    app.run(debug=True)
