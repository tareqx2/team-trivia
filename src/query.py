import db
from flask import Flask, jsonify
from flask import abort
from flask import request

app = Flask(__name__)

@app.route('/api/v1.0/questions', methods=['GET'])
def get_questions():
	count = request.args.get('count') if request.args.get('count') else 0
	if count==0
		abort(400)
	questions = db.session.query(db.Documents).limit(count) if count != 0 else db.session.query(db.Documents)
	return jsonify({'questions',questions.clues}),200

@app.route('/api/v1.0/questions/<int:id>', methods=['GET'])
def get_questions(id):
	questions = db.session.query(db.Documents).\
    				filter(documents.id == id)
	return jsonify({'questions',questions.clues}),200

@app.route('/api/v1.0/questions', methods=['POST'])
def add_questions():
	if not request.json or not 'question' in request.json:
        abort(400)
    abort(500)

@app.route('/api/v1.0/scores/', methods=['GET'])
def get_scores():
	scores = db.session.query(db.Scores)
	return jsonify({'scores',scores}),200

@app.route('/api/v1.0/scores/<int:userid>', methods=['GET'])
def get_scores(userid):
	scores = db.session.query(db.Scores).\
				filter(scores.userid == userid)
	return jsonify({'scores',scores}),200

@app.route('/api/v1.0/scores/<int:userid>', methods=['PUT'])
def update_scores(userid):
	 if not request.json or not 'score' in request.json:
        abort(400)
	scores = db.session.query(db.Scores).\
				filter(scores.userid == userid).\
    			update({"score": request.json['score']})
    return jsonify({'scores',scores}),201

if __name__ == '__main__':
    app.run()