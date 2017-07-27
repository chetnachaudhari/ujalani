import json
file = open('sample.json').read()
print(file)
config = json.loads(file)
print(config)
print(config['region'])