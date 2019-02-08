from app import db
from ..model import BaseModel


class User(BaseModel):
    id = db.Column(db.String(20), primary_key=True)
    password = db.Column(db.String(30), nullable=False)
    name = db.Column(db.String(20), unique=True, nullable=False)
    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

