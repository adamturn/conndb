# conndb
Connect Python to database using a Java properties file for configuration.

## Container Quickstart
Add the following command to your Dockerfile:
```dockerfile
RUN cd /app/src &&
    mkdir github github/adamturn &&
    git clone https://github.com/adamturn/conndb.git github/adamturn &&
    pip install --no-cache-dir --upgrade -r github/adamturn/conndb/requirements.txt
```

Example import:
```python
from github.adamturn.conndb.main import connect_postgres

conn = connect_postgres("/app/cfg/pg-test.properties")
```

## Requirements
Your Java properties file must define a host, port, dbname, username, and password. For example, the parsing logic/regex expects something like this, but dropping the 'db' works too:
```properties
dbhost=127.0.0.1
dbport=5432
dbname=postgres
dbuser=postgres
dbpass=password
```
