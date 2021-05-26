from dustmaker import *

file = 'C:/Program Files (x86)/Steam/steamapps/common/Dustforce/user/level_src/testmain'

with open(file, 'rb') as f:
    level = read_map(f.read())

for name in level.vars:
    print(name, level.vars[name])

# p1_face 1
# p1_x -18
# p1_y 1

level.vars['p1_x'].value = -18
level.vars['p1_y'].value = 1

# with open(file, 'wb') as f:
#     f.write(write_map(level))
