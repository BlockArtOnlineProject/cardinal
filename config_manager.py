import json


def read(entry: str):
    """
    Chilling with the config
    """
    with open("config.json", "r") as f:
        config = json.loads(f.read())
        return config[entry]


def write(entry: str, value):
    """
    Writes to the config.
    """
    with open("config.json", "r") as f:
        config = json.loads(f.read())
        config[entry] = value

    with open("config.json", "w") as a:
        a.write(json.dumps(config))