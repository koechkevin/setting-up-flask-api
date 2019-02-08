from run import request, app, jsonify
from models import db, User, user_schema

@app.route('/user', methods=['POST'])
def create_user():
    name = request.json['name']
    new_user = User(name)
    db.session.add(new_user)
    db.session.commit()
    return user_schema.jsonify(new_user)