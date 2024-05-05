from sqlalchemy import create_engine, inspect, ForeignKey, Column, String, Integer, CHAR, Enum
from sqlalchemy.orm import sessionmaker, declarative_base

Base = declarative_base()


class Quote(Base):
    __tablename__ = "quotes"

    qid = Column("qid", Integer, primary_key=True)
    movie_id = Column("movie_id", Integer)
    character_id = Column("character_id", Integer)
    movie_type = Column("movie_type", Enum('TV Show', 'movie'))
    quote = Column('quote', String)

    def __init__(self, qid, movie_id, character_id, movie_type, quote):
        self.qid = qid
        self.movie_id = movie_id
        self.character_id = character_id
        self.movie_type = movie_type
        self.quote = quote

    def __repr__(self):
        return f"({self.qid} {self.movie_id} ${self.character_id}, ${self.movie_type}, ${self.quote})"


engine = create_engine('sqlite:///mydb.db', echo=True)

Base.metadata.create_all(bind=engine)

# Session = sessionmaker(bind=engine)
# session = Session()

# myQuote = Quote(1, 3445, 45, "TV Show", "I am the Danger!!!")nam
# session.add(myQuote)
# session.commit()

enum_values = Quote.movie_type.type.enums
print(enum_values)