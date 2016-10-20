
from ming import create_datastore
from ming.odm import ThreadLocalODMSession

DB_PATH = 'mongodb://localhost:27017/library'
SESSION = ThreadLocalODMSession(bind=create_datastore(DB_PATH))
