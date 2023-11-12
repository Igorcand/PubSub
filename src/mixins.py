import os
import json

def save_publisher_key(key):
    path = f"db.json"
    if os.path.exists(path):
        with open(f"db.json", "r") as outfile:
            outfile = json.load(outfile)
        if not key in outfile.keys():
            key_dict = {key:{}}
            data = dict(outfile, **key_dict)
            with open(f"db.json", "w") as outfile:
                json.dump(data, outfile)
    else:
        with open(f"db.json", "w") as outfile:
            json.dump({key:{}}, outfile)

def save_publisher_messages(key, message):
    with open(f"db.json", "r") as outfile:
        outfile = json.load(outfile)
    queue = outfile[key]
    n = len(queue)
    outfile[key][n] = message

    data = dict(outfile)
    with open(f"db.json", "w") as outfile:
        json.dump(data, outfile)
