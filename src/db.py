from sqlalchemy import Column, ForeignKey, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import create_session, relationship, load_only
from sqlalchemy import create_engine
from sqlalchemy.sql.expression import func, select

Base = declarative_base()

engine = create_engine("sqlite:///clues.db")

class Categories(Base):
	__tablename__ = 'categories'
	id = Column(Integer,primary_key=True)
	category = Column(Text)

	def __init__(self, id, category):
		self.id = id
		self.category = category

	@property
	def serialize(self):
		return {
			'id' : self.id,
			'category': self.category,
		}

class Classifications(Base):
	__tablename__ = "classifications"
	clue_id = Column(Integer,primary_key=True)
	category_id = Column(Integer,ForeignKey(Categories.id))
	clues = relationship("Documents")

	def __init__(self, clue_id, category_id):
		self.clue_id = clue_id
		self.category_id = category_id

	@property
	def serialize(self):
		return {
			'clue_id' : self.clue_id,
			'category_id': self.category_id,
		}

class Documents(Base):
	__tablename__ = 'documents'
	id = Column(Integer, ForeignKey(Classifications.clue_id), primary_key=True)
	clue = Column(Text)
	answer = Column(Text)

	def __init__(self, id, clue, answer):
		self.id = id
		self.clue = clue
		self.answer = answer
	@property
	def serialize(self):
		return {
			'id' : self.id,
			'clue': self.clue,
			'answer': self.answer
		}

class Users(Base):
	__tablename__ = 'users'
	id = Column(Integer,primary_key=True)
	username = Column(String(32))
	password = Column(Text)
	
	def __init__(self, username, id = 0,password = ""):
		self.id = id
		self.username = username
		self.password = password

	@property
	def serialize(self):
		return {
			'id' : self.id,
			'username': self.username,
			'password': self.password
		}

class Scores(Base):
	__tablename__ = 'scores'
	id = Column(Integer,primary_key=True)
	score = Column(Integer)
	user_id = Column(Integer,ForeignKey(Users.id))

	def __init__(self, id, score, user_id):
		self.id = id
		self.score = score
		self.user_id = user_id

	@property
	def serialize(self):
		return {
			'id' : self.id,
			'score': self.score,
			'user_id': self.user_id
		}

session =  create_session(bind = engine)
