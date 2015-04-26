import db
from flask import Flask, jsonify
from flask import abort
from flask import request
from passlib.hash import pbkdf2_sha256
 
app = Flask(__name__)


##############################################################################################
@app.route('/api/v1.0/questions', methods=['GET'])
def get_questions():

	questionResponse = {}
	index = 0
	category_values = []
	clue_ids = []
	#Get 8 random categories that contain at least 6 questions
	categories = db.session.query(db.Classifications).\
					group_by(db.Classifications.category_id).\
					having(db.func.count(db.Classifications.category_id) > 5).\
					order_by(db.func.random()).\
					limit(8).all()
	

	for cat in categories:
		category_values.append(cat.category_id)

	#get all the question Id's (this is probably inefficient and could be done in the first query)
	clueIds = db.session.query(db.Classifications).\
				filter(db.Classifications.category_id.in_(category_values)).\
				all()

	for clueid in clueIds:
		clue_ids.append(clueid.clue_id)

	questions = db.session.query(db.Documents,db.Categories).\
				join(db.Classifications).\
				join(db.Categories).\
				filter(db.Documents.id.in_(clue_ids)).\
				all()

	for val in questions:
		clue = {'category': val.Categories.category,'clue':val.Documents.clue,'answer':val.Documents.answer}
		questionResponse['question'+str(index)] = clue
		index = index+1

	return jsonify(questionResponse),200

##############################################################################################

@app.route('/api/v1.0/scores', methods=['GET'])
def get_scores():
	scores = db.session.query(db.Scores).all()

	return jsonify(json_list=[i.serialize for i in scores]),200

##############################################################################################

@app.route('/api/v1.0/scores/<int:userid>', methods=['GET'])
def get_user_scores(userid):
	scores = db.session.query(db.Scores).\
				filter(scores.userid == userid)

	return jsonify(json_list=[i.serialize for i in scores]),200

##############################################################################################

@app.route('/api/v1.0/scores/<int:userid>', methods=['PUT'])
def update_scores(userid):
	if not request.json or not 'score' in request.json:
		abort(400)
	scores = db.session.query(db.Scores).\
				filter(scores.userid == userid).\
				update({"score": request.json['score']})

	return jsonify(json_list=[i.serialize for i in scores]),201

##############################################################################################

@app.route('/api/v1.0/user/adduser/<string:password>', methods=['PUT'])
def add_user(password):
	hash = pbkdf2_sha256.encrypt("password", rounds=200000, salt_size=16)

	#store hash password

	return 200

##############################################################################################

@app.route('/api/v1.0/user/login', methods=['POST'])
def login_user(password):
	successfulLogin = pbkdf2_sha256.verify("password", hash)
	if not successfulLogin:
		abort(400)
	return 200

##############################################################################################

if __name__ == '__main__':
	app.run()