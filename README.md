# FlexiCache

FlexiCache is a versatile and user-friendly cache decorator for Python functions that is compatible with various storage backends. This allows you to cache function results in memory, on a local file system, or in AWS DynamoDB. You can set up the cache expiration time, and if not set up, the cache will always be valid.
## Features

- Decorate functions to cache their results
- Compatible with memory, local file system, and AWS DynamoDB storage backends
- Set custom cache expiration times
- Easily expandable for other storage backends

## Local Test Setup

Follow these steps to build and install the package for local testing:

```bash
# Build the package
python setup.py bdist_wheel

# Install the package
pip install --force-reinstall dist/FlexiCache-0.0.1-py3-none-any.whl
```

## Examples

### Install FlexiCache

First, install the FlexiCache package:

```bash
pip install flexicache
```

### Import Classes

Import the required classes for the cache types you want to use:

```python
from flexicache import Cache, MemoryCache, FileCache, DDBCache
```

### Cache Storage Format

Cache data is stored in a readable format that includes the function name, arguments, keyword arguments, timestamp, and value:

```json
{
    "c7512aa16312c157ac8490dbdd00f999": {
        "function": "file_cached_function",
        "args": "(1, 2)",
        "kwargs": "{}",
        "timestamp": 1685835554.402383,
        "value": 2
    },
    "296849916ce184fe8419fb3b466bd233": {
        "function": "file_cached_function",
        "args": "(2, 2)",
        "kwargs": "{}",
        "timestamp": 1685837065.483979,
        "value": 4
    }
}
```

## Usage

### Memory Cache

```python
from flexicache import Cache, MemoryCache

memory_cache = MemoryCache()
@Cache(memory_cache)
def memory_cached_function(a, b):
    return a + b
```

### Local File System Cache

```python
from flexicache import Cache, FileCache

file_cache = FileCache('cache.json')
@Cache(file_cache)
def file_cached_function(a, b):
    return a * b
```

### AWS DynamoDB Cache

Ensure the `boto3` package is installed and AWS credentials are configured to use the `DDBCache` class.

```python
import boto3
from flexicache import Cache, DDBCache

aws_ddb_client = boto3.client('dynamodb', region_name='your-region', aws_access_key_id='your-access-key', aws_secret_access_key='your-secret-key')
ddb_cache = DDBCache(aws_ddb_client, table_name='my_ddb_table', cache_seconds=900)

@Cache(ddb_cache)
def ddb_cached_function(a, b):
    return a ** b
```

## Extending to Other Storage Backends

To support a new cache storage backend, create a new class that inherits from `CacheStrategy` and implements the `get` and `set` methods.

```python
from cache_strategy import CacheStrategy

class MyCache(CacheStrategy):
    def get(self, key):
        # Implement logic to get the value for the key from your storage backend
        pass

    def set(self, key, value, func, *args, **kwargs):
        # Implement logic to store the value for the key in your storage backend
        pass
```
## Next Version
To provide config file, which defines the default value e.g. default file path and file name, default AWS DDB Client, and default DDB table name.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.