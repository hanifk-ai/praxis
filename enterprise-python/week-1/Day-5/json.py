import json

with open('/home/hanif/praxis-academy/enterprise-python/week-1/person.json', 'r') as f:
  data = json.load(f)

# Output: {'name': 'Bob', 'languages': ['English', 'French']}
print(data)
