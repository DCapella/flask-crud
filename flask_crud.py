import os

from flask import Flask
from flask import render_template
from flask import request

from flask_sqlalchemy import SQLAlchemy

project_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(project_dir, 'cruddatabase.db')
database_file = f'sqlite:///{db_path}'

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = database_file

db = SQLAlchemy(app)

class Item(db.Model):
    title = db.Column(db.String(80),
                      unique=True,
                      nullable=False,
                      primary_key=True)
                
    def __repr__(self):
        return f'<Title: {self.title}>'

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.form:
        item = Item(title=request.form.get('title'))
        db.session.add(item)
        db.session.commit()
    items = Item.query.all()
    return render_template('home.html', items=items)

if __name__ == '__main__':
    app.run(debug=True)