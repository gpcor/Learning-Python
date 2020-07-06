import json
import pprint


def update():
    with open("data.json", "r+") as jsonfile:
        reader = json.load(jsonfile)

        print(reader)

update()
