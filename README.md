# tc_mongodb
MongoDB storage adapter for thumbor.

# Versions

NOT FOR PROD

This projects uses the following versioning scheme:

`<thumbor major>.<mongodb plugin major>.<mongodb plugin minor>`


# Configuration
```
# MONGO STORAGE OPTIONS
MONGO_STORAGE_SERVER_HOST = 'localhost' # MongoDB storage server host
MONGO_STORAGE_SERVER_PORT = 27017 # MongoDB storage server port
MONGO_STORAGE_SERVER_DB = 'thumbor' # MongoDB storage server database name
MONGO_STORAGE_SERVER_COLLECTION = 'images' # MongoDB storage image collection
MONGO_STORAGE_SERVER_USER = '' # user
MONGO_STORAGE_SERVER_PASSWORD = '' # password
MONGO_STORAGE_SERVER_AUTH = '' # credential stored in this db
MONGO_STORAGE_SERVER_REPLICASET = 'myReplica' # name of the replicaset - option
MONGO_STORAGE_SERVER_READ = 'secondaryPreferred'

# MONGO STORAGE OPTIONS
MONGO_RESULT_STORAGE_SERVER_HOST = 'localhost' # MongoDB storage server host
MONGO_RESULT_STORAGE_SERVER_PORT = 27017 # MongoDB storage server port
MONGO_RESULT_STORAGE_SERVER_DB = 'thumbor' # MongoDB storage server database name
MONGO_RESULT_STORAGE_SERVER_COLLECTION = 'images' # MongoDB storage image collection
MONGO_RESULT_STORAGE_SERVER_USER = '' # user
MONGO_RESULT_STORAGE_SERVER_PASSWORD = '' # password
MONGO_RESULT_STORAGE_SERVER_AUTH = '' # credential stored in this db
MONGO_RESULT_STORAGE_SERVER_REPLICASET = 'myReplica' # name of the replicaset - option
MONGO_RESULT_STORAGE_SERVER_READ = 'secondaryPreferred'
```
