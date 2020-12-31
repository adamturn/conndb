# conndb
Connect Python to database using a Java properties file for configuration.

## Quickstart
Clone this repo somewhere and save the path.
```shell
$ cd ~/github/adamturn
$ git clone https://github.com/adamturn/conndb.git && cd conndb
$ pwd
```
Example path:
```
/home/adam/github/adamturn/conndb
```
Activate virtual environment and install dependencies.
```shell
$ conda activate hack
(hack)$ python -m pip install --upgrade -r requirements.txt
```
Example import:
```python
# standard library
import sys
# local modules
sys.path.append("/home/adam/github/adamturn/conndb")
from conndb import connect_postgres

conn = connect_postgres("/home/adam/config/test.properties")
```

## Notes
Your editor may flag the import with a warning and say that it is unable to import the module, but don't worry, it is wrong.

Your properties file must have a host, port, dbname, username, and password. For example, the parsing logic/regex expects something like this, but dropping the 'db' works too:
```properties
dbhost=127.0.0.1
dbport=5432
dbname=postgres
dbuser=postgres
dbpass=password
```
