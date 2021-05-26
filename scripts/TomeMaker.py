import json
import re
from dustmaker import *

dest_dir = "C:/Program Files (x86)/Steam/steamapps/common/Dustforce/user/levels/%s"
index_file = '_level_index.json'

map_file = 'C:/Program Files (x86)/Steam/steamapps/common/Dustforce/user/level_src/Map_Pack_Gallery'

with open(dest_dir % index_file, 'r') as f:
    level_dict = json.load(f)

# takes atlas URLs and strips them to just their ID, then looks up the filename in the index
ids = []
line = input()
while line != "stop":
    if line:
        ids.append(line.split("/")[-2])
    line = input()

for id in ids:
    print(level_dict[id]["filename"])

with open(map_file, "rb") as f:
    map = read_map(f.read())

tome_list = None
for entity_id in map.entities:
    _, _, entity = map.entities[entity_id]
    if entity.type == "z_string_list":
        temp_list = entity.vars['list'].value[1]
        if temp_list and temp_list[0].value == "Replace":
            tome_list = temp_list
            break

if tome_list:
    new_list = [level_dict[id]["filename"] for id in ids]
    new_list.sort(key=lambda x: x.upper())
    # need to copy the new list into the existing array
    tome_list.clear()
    tome_list.extend(Var(VarType.STRING, filename) for filename in new_list)
else:
    print('no "Replace" tome found')

with open(map_file, "wb") as f:
    f.write(write_map(map))
