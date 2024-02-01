import json


def compareJson(name):
    filePath = name
    with open(filePath, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
    source = data['source']
    target = data['target']
    for app in source:
        try:
            if source[app] != target[app]:
                return False
        except Exception as e:
            print(f"Error: {e}")
            return False
    return True


if __name__ == '__main__':
    print(compareJson('json_file.json'))
