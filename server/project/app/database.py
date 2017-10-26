#!/usr/bin/env python
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.declarative import (
    declared_attr,
    declarative_base,
)
from sqlalchemy.ext.hybrid import hybrid_property


class BaseModel(object):
    @declared_attr
    def __tablename__(cls):
        return cls.__name__

    @hybrid_property
    def query(cls):
        return db.session.query(cls)

    def __repr__(self):
        return self.name


db = SQLAlchemy()
db.Model = declarative_base(cls=BaseModel)
