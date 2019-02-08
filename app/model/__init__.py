from app import db


class BaseModel(db.Model):
    __abstract__ = True

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self, **kwargs):
        for attr, val in kwargs.items():
            setattr(self, attr, val)
        db.session.commit()

    def remove(self):
        db.session.delete(self)
        db.session.commit()

    def to_dict(self):
        attrs = self.__dict__.copy()
        del attrs['_sa_instance_state']

        return attrs


from .user import *

