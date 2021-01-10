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
        props_path: path to Java properties file with db config
    """
    print("Parsing db config properties...")
    with open(props_path, "r") as f:
        props = f.read().split("\n")
    delim = "="
    props = {kv.split(delim)[0]: kv.split(delim)[1] for kv in props if delim in kv}
    print("Property keys:", ", ".join(props.keys()))

    print("Matching property keys to db connection requirements...")
    reqs = {
        "dbhost": r"(?i)host",
        "dbport": r"(?i)port",
        "dbname": r"(?i)(?<!user|host)(?<!(user|host)[-_\s])name",
        "dbuser": r"(?i)user", 
        "dbpass": r"(?i)pass"
    }
    cfgkeys = list(reqs.keys())
    cfg = dict.fromkeys(cfgkeys)
    for prop in props:
        for cfgkey in cfgkeys:
            pattern = reqs[cfgkey]
            if re.search(pattern, string=prop):
                cfg[cfgkey] = props[prop]
                cfgkeys.remove(cfgkey)
            continue
        continue
    if cfgkeys:
        raise ValueError("No match for required config key: " + ", ".join(cfgkeys))
    else:
        cfgkeys = tuple(cfg.keys())

    print("Connecting to db...")
    conn = psycopg2.connect(
        host=cfg[cfgkeys[0]],
        port=cfg[cfgkeys[1]],
        database=cfg[cfgkeys[2]],
        user=cfg[cfgkeys[3]],
        password=cfg[cfgkeys[4]]
    )
    print("Connection established!")

    return conn
