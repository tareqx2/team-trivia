from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import create_session
from sqlalchemy import create_engine

Base = automap_base()

engine = create_engine("sqlite:///clues.db")

# reflect the tables
Base.prepare(engine, reflect=True)

# mapped classes are now created with names by default
# matching that of the table name.
Clues = Base.classes.clues
Airdates = Base.classes.airdates
Documents = Base.classes.documents
Categories = Base.classes.categories

session =  create_session(bind = engine)
