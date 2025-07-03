import sys, json

version = sys.argv[1]
filename = sys.argv[2]

try:
    with open(filename, 'r') as json_file:
        data = json.load(json_file)
except:
    print("Проблема с открытием файла!")
    
versions = list()

for key in data:
    versions.append((data[key]).replace('*', '1'))
    versions.append((data[key]).replace('*', '2'))

def version_key(v):
    return tuple(int(x) for x in v.split('.'))

versions = sorted(versions, key=version_key, reverse=True)

print('Отсортированный список версий:')
print(*versions, sep='\n')

base_version = version_key(version)

older_versions = list()

for v in versions:
    if version_key(v) < base_version:
        older_versions.append(v)

print('Старые версии:')
print(*older_versions, sep='\n')
