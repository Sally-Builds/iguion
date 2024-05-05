from sqlalchemy import Column, Integer, String
from app import my_db


class Quote(my_db.Model):
    __tablename__ = 'quotes'

    qid = Column(Integer, primary_key=True)
    movie_type = Column(String, nullable=False)
    movie_id = Column(Integer, nullable=False)
    cast_id = Column(String, nullable=False)
    quote = Column(String(600), nullable=False)

    def __repr__(self):
        return f'Quote({self.qid}, {self.movie_type}, {self.movie_id}, {self.cast_id}, {self.quote})'

    @classmethod
    def save(cls, data):
        my_db.session.add(data)
        my_db.session.commit()
        return 'data created'
