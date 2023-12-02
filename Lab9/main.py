from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///notes.db'
db = SQLAlchemy(app)


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(200), nullable=False)
    important = db.Column(db.Boolean, default=False)


with app.app_context():
    db.create_all()


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        text = request.form['text']
        important = request.form.get('important') == 'on'

        note = Note(text=text, important=important)
        db.session.add(note)
        db.session.commit()

    notes = Note.query.all()
    
    return render_template('index.html', notes=notes)


app.run(debug=True)