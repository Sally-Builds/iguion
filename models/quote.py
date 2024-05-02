from app import db
from config.constants import QUOTE_TABLE
from movieAPI import MovieAPI


class Quote(db.Model):
    __tablename__ = QUOTE_TABLE

    qid = db.Column(db.Integer, primary_key=True)
    movie_id = db.Column(db.Integer, nullable=False)
    character_id = db.Column(db.Integer, nullable=False)
    movie_type = db.Column(db.Enum('TV Show', 'Movie'), nullable=False)
    category_id = db.Column(db.ForeignKey('categories.cid'))
    quote = db.Column(db.String, nullable=False)

    @classmethod
    def find_all(cls):
        quotes = cls.query.all()

        quotes = [{"id": quote.qid, "movie_id": MovieAPI().get_movie_name(quote.movie_type, quote.movie_id),
                   "movie_type": quote.movie_type,
                   "character_id": MovieAPI().get_character_name(quote.character_id), "quotes": quote.quote} for quote
                  in quotes]

        return quotes

    def __repr__(self):
        return f'({self.qid}, {self.movie_id}, {self.character_id}, {self.movie_type}, {self.category_id}, {self.quote})'
