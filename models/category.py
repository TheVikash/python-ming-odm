
from ming import schema
from ming.odm import MappedClass
from ming.odm import FieldProperty, ForeignIdProperty
from datetime import datetime
from ming import create_datastore
from ming.odm import ThreadLocalODMSession
from ming.odm import Mapper

session = ThreadLocalODMSession(bind=create_datastore('mongodb://localhost:27017/tutorial'))


class Category(MappedClass):
    class __mongometa__:
        name = 'category'
        session = None
    _id = FieldProperty(schema.ObjectId)
    name = FieldProperty(schema.String(required=True))
    created_at = FieldProperty(schema.DateTimeTZ())
    updated_at = FieldProperty(schema.DateTimeTZ())
    def __init__(self,session, name):
        self.__mongometa__.session = session
        self.name = name
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
Mapper.compile_all()

category = Category(session,"Science")
print(category)


