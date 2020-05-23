import pymongo

mongo = pymongo\
    .MongoClient('mongodb+srv://testUser:testtest@newslist-dmspe.mongodb.net/test?retryWrites=true&w=majority')
db = pymongo.database.Database(mongo, 'news-list')
col = pymongo.collection.Collection(db, 'news-list')
