from app import db
from config.constants import USER_TABLE
from movieAPI import MovieAPI


class User(db.Model):
    __tablename__ = USER_TABLE

    uid = db.Column(db.Integer, primary_key=True)
    password = db.Column(db.String(60), nullable=False)
    username = db.Column(db.String, unique=True, nullable=False)

    def __repr__(self):
        return f'({self.uid}, {self.username})'

    @classmethod
    def get_by_id(cls, uid):
        data = User.query.filter_by(uid=uid).first()
        print(data)
        return {"uid": data.uid, "username": data.username}
