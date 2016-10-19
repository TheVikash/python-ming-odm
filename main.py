from app.models.category import Category
from app.models.category import Category
from ming import create_datastore
from ming.odm import ThreadLocalODMSession



session = ThreadLocalODMSession(bind=create_datastore('mongodb://localhost:27017/tutorial'))
category = Category(session,"Science")
print(category)