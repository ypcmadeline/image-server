from pymongo import MongoClient

def get_database():
    client = MongoClient('mongodb+srv://ypcmadeline:Igotoschoolbybus@cluster0.ibt1zxz.mongodb.net/?retryWrites=true&w=majority')
    return client['image_database']