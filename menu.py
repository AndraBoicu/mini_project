import json


def default():
    with open('menu.json') as f:
        data = json.load(f)
        f.close()
    for i in data['default_menu']:
        print(data['default_menu'][i])


def manager():
    with open('menu.json') as f:
        data = json.load(f)
        f.close()
    for i in data['manager']:
        print(i + '. ' + data['manager'][i])


def magazioner():
    with open('menu.json') as f:
        data = json.load(f)
        f.close()
    for i in data['magazioner']:
        print(i + ". " + data['magazioner'][i])


def operator():
    with open('menu.json') as f:
        data = json.load(f)
        f.close()
    for i in data['operator']:
        print(i + ". " + data['operator'][i])
