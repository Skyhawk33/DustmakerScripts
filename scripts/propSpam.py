from dustmaker import *
from itertools import product
from copy import deepcopy

map_file = "C:/Program Files (x86)/Steam/steamapps/common/Dustforce/user/level_src/prop_test"

with open(map_file, "rb") as f:
    map = read_map(f.read())

base_prop = Prop(0, 0, True, True, 1, 1, 11, 4, 0)

for x, y in product(range(-100, 150), repeat=2):
    prop = deepcopy(base_prop)
    map.add_prop(16, x / 24, y / 24, prop)

map.name(map.name() + '_modified')
with open(map_file + "_modified", "wb") as f:
    f.write(write_map(map))
