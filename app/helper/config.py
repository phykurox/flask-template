import os
import boto3

# Config class for databases
class MongoConfig(object):
    # For MongoDB compatible
    DB_NAME = os.getenv('DB_NAME', default='test_db')
    DB_COLLECTION_NAME = os.getenv(
            'DB_COLLECTION_NAME',
            default='test_collection')
    DB_CONNECTION_STRING = os.getenv(
            'DB_CONNECTION_STRING',
            default='mongodb://localhost/')

class RDSConfig(object):
    def __init__(self):
        self.client = boto3.client('rds-data')
    database_name = os.getenv('RDS_NAME', default='database-1')
    db_cluster_arn = os.getenv('ARN_AWS', default='')
    db_credentials_secrets_store_arn = ''
