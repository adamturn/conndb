"""
Python 3.6
Authors: Liam Xiao, Adam Turner
"""

# python package index
import psycopg2
# standard library
import re


def connect_postgres(props_path):
    """Connects to Postgres and returns active psycopg2 connection object.

    Args:
        props_path: path to Java properties file
    """
    print("Parsing db properties...")
    with open(props_path, "r") as f:
        props = f.read().split("\n")
    delim = "="
    props = {kv.split(delim)[0]: kv.split(delim)[1] for kv in props if delim in kv}
    print(f"Property keys: {', '.join(props.keys())}")

    print("Matching property keys to db connection requirements...")
    reqs = ["dbhost", "dbport", "dbname", "dbuser", "dbpass"]
    config = {
        reqs[0]: r"(?i)host",
        reqs[1]: r"(?i)port",
        reqs[2]: r"(?i)(?<!user)(?<!user[-_\s])name",
        reqs[3]: r"(?i)user",
        reqs[4]: r"(?i)pass"
    }
    for prop in props:
        for req in reqs:
            pattern = config[req]
            if re.search(pattern, string=prop):
                config[req] = props[prop]
                reqs.remove(req)
            continue
        continue
    if reqs:
        raise ValueError(f"No match for required config key: {', '.join(reqs)}")
    else:
        reqs = list(config.keys())

    print("Connecting to db...")
    conn = psycopg2.connect(
        host=config[reqs[0]],
        port=config[reqs[1]],
        database=config[reqs[2]],
        user=config[reqs[3]],
        password=config[reqs[4]]
    )
    print("Connection established!")

    return conn
