from app import db
from config.constants import CATEGORY_TABLE


class Category(db.Model):
    __tablename__ = CATEGORY_TABLE

    cid = db.Column('cid', db.Integer, primary_key=True)
    category_name = db.Column("category_name", db.String)

    @classmethod
    def add(cls, categories):
        for item in categories:
            db.session.add(cls(category_name=item))

        db.session.commit()
        return True

    def __repr__(self):
        return f"({self.cid} {self.category_name})"
