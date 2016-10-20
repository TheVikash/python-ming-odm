
from app.models.category import Category
from app.config import SESSION as session
from app.sample_data import CATEGORIES


"""
scripts functions 
"""

def category_insertion():

    for category in CATEGORIES:
        obj = Category(name=category['name'] )
        print(obj)
    print(session)    
    session.flush()
    session.clear()




