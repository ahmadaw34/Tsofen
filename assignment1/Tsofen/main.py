import json
import os

def compareVersions(name):
    try:
        filePath = os.path.abspath(name)
        with open(filePath, 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)
        source = None
        for d in data:
            if source is None:
                source = d
            else:
                for app in data[source]:
                    if app.find("version") != -1 and data[source][app] != data[d][app]:
                        return False
    except Exception as e:
        print(f"Error: {e}")
        return False
    return True


if __name__ == '__main__':
    print(compareVersions('json_file.json'))
