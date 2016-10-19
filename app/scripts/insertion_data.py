
from app.models.category import Category
from ming import create_datastore
from ming.odm import ThreadLocalODMSession

"""
scripts functions 
"""

session = ThreadLocalODMSession(bind=create_datastore('mongodb://localhost:27017/tutorial'))
def category_insertion():
    category = Category(session,"Science")
    print(category)


