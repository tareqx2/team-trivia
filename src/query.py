import db
import flask

def get_questions(count=1000):
	questions = db.session.query(db.Documents).limit(count)
	return questions


questions = get_questions()