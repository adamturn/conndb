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
    config = {
        "dbhost": r"(?i)host",
        "dbport": r"(?i)port",
        "dbname": r"(?i)(?<!user)(?<!user[-_\s])name",
        "dbuser": r"(?i)user",
        "dbpass": r"(?i)pass"
    }
    print("Matching property keys to db connection requirements...")
    reqs = list(config.keys())
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
    print("Connecting to db...")
    conn = psycopg2.connect(
        host=config["dbhost"],
        port=config["dbport"],
        database=config["dbname"],
        user=config["dbuser"],
        password=config["dbpass"]
    )
    print("Connection established!")

    return conn
