import boto3
from flexicache import Cache, MemoryCache, FileCache, DDBCache


# pip install flexicache

def exmaple_mem():
    # Memory caching
    memory_cache = MemoryCache()
    
    @Cache(memory_cache)
    def memory_cached_function(a, b):
        return a + b
    
    result = memory_cached_function(2, 2)
    print(f"memory_cached_function(2, 2) = {result}")
    assert result == 2 + 2


def exmaple_file():
    # Local file system caching
    file_cache = FileCache('cache.json')
    
    @Cache(file_cache)
    def file_cached_function(a, b):
        return a * b
    
    result = file_cached_function(2, 2)
    print(f"file_cached_function(2, 2) = {result}")
    assert result == 2 * 2


def exmaple_ddb():
    # AWS DynamoDB caching
    aws_ddb_client = boto3.client('dynamodb',
                                  region_name='eu-north-1')  # , aws_access_key_id='your-access-key', aws_secret_access_key='your-secret-key')
    ddb_cache = DDBCache(aws_ddb_client, table_name='example_cache_table', cache_seconds=900)
    
    @Cache(ddb_cache)
    def ddb_cached_function(a, b):
        return a ** b
    
    result = ddb_cached_function(1, 2)
    print(f"ddb_cached_function(1, 2) = {result}")
    assert result == 1 ** 2
