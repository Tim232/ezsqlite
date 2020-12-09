# EZSQLITE

Use SQLite3 without knowing SQL

How to Install : 
```shell
$ pip install ezsqlite
```

How to Use : 
```python
from ezsqlite import Database
db = Database('File.db', 'users')

users = db.slctall()
user = db.select(id = 'test')
db.update({'id': 'test'}, {'id': 'example'})
db.insert('text', 'ex', 'ample')
db.delete(id = 'test')
```
