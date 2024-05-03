from sqlalchemy import Column, Integer, String
from main import db


class Quote(db.Model):
    __tablename__ = 'quotes'

    qid = Column(Integer, primary_key=True)
    movie_type = Column(String, required=True)
    movie_id = Column(Integer, required=True)
    cast_id = Column(String, required=True)
    quote = Column(String(600), required=True)

    def __repr__(self):
        return f'Quote({self.qid}, {self.movie_type}, {self.movie_id}, {self.cast_id}, {self.quote})'

    @classmethod
    def save(cls, data):
        db.session.add(data)
        db.session.commit()
        return 'data created'
