from flask import Flask, render_template, request, redirect, session
from user import User
app = Flask(__name__)
app.secret_key = 'kajgkjafsg'

@app.route('/')
def load():
    return redirect('/read')

@app.route('/create')
def create():
    return render_template('create.html')

@app.route('/submit', methods=['POST'])
def submit():
    data = {
        'fname' : request.form['fname'],
        'lname' : request.form['lname'],
        'email' : request.form['email']
        }
    User.save(data)
    return redirect('/read')

@app.route('/read')
def read():
    users = User.get_all()
    return render_template('read.html', users=users)

@app.route('/profile/<user_id>')
def profile(user_id):
    data = {'user_id' : user_id}
    user = User.get_one(data)
    return render_template('profile.html', user=user[0])

@app.route('/edit/<user_id>')
def edit(user_id):
    data = {'user_id' : user_id}
    user = User.get_one(data)
    return render_template('edit.html', user=user[0])

@app.route('/update/<user_id>', methods=['POST'])
def update(user_id):
    data = {
        'user_id' : user_id,
        'fname' : request.form['fname'],
        'lname' : request.form['lname'],
        'email' : request.form['email']
        }
    User.update(data)
    return redirect('/profile/' + user_id)

@app.route('/delete/<user_id>')
def delete(user_id):
    data = {'user_id' : user_id}
    User.delete(data)
    return redirect('/read')

if __name__=="__main__":
    app.run(debug=True)

