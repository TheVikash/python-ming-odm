"""
Category class  
"""
from datetime import datetime
from ming import schema
from ming.odm import FieldProperty,MappedClass,Mapper
from app.config import SESSION as session


class Category(MappedClass):
    class __mongometa__:
        name = 'category'
        unique_indexes = [('name',)]
        session = session
    _id = FieldProperty(schema.ObjectId)
    name = FieldProperty(schema.String(required=True))
    created_at = FieldProperty(schema.DateTimeTZ(if_missing=datetime.now()))
    updated_at = FieldProperty(schema.DateTimeTZ(if_missing=datetime.now()))
    def __str__(self):
        print("name :", self.name)
        print("created at :", self.created_at)
        print("updated at :", self.updated_at)
        return '_id : '+ str(self._id)
Mapper.compile_all()

