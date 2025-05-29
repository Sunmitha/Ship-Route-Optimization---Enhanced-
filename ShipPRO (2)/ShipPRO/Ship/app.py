from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'your-secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# ─── Models ──────────────────────────────────────
class User(db.Model):
    id            = db.Column(db.Integer, primary_key=True)
    username      = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    def set_password(self, pw):
        self.password_hash = generate_password_hash(pw)

    def check_password(self, pw):
        return check_password_hash(self.password_hash, pw)

# Create tables
with app.app_context():
    db.create_all()

# ─── Routes ──────────────────────────────────────
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        uname = request.form['username'].strip()
        pw = request.form['password'].strip()

        if User.query.filter_by(username=uname).first():
            flash('Username already taken', 'error')
            return redirect(url_for('signup'))

        new_u = User(username=uname)
        new_u.set_password(pw)
        db.session.add(new_u)
        db.session.commit()

        # Redirect to ind.html after successful signup
        return redirect(url_for('route_form'))

    return render_template('signup.html')



@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        uname = request.form['username'].strip()
        pw = request.form['password'].strip()
        u = User.query.filter_by(username=uname).first()

        if u and u.check_password(pw):
            # Redirect to ind.html after successful login
            return redirect(url_for('ind'))

        flash('Invalid username or password', 'error')
        return redirect(url_for('login'))

    return render_template('index.html')



@app.route('/route-form')
def route_form():
    return render_template('ind.html')



if __name__ == '__main__':
    app.run(debug=True)
