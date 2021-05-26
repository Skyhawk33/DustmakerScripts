from dustmaker import *


def find_flags(map):
    flags = []
    for key in map.entities:
        if map.entities[key][2].type == 'level_end':
            flags.append(map.entities[key])
    return flags


if __name__ == '__main__':
    map_file = 'C:/Program Files (x86)/Steam/steamapps/common/Dustforce/user/level_src/test'

    with open(map_file, "rb") as f:
        map = read_map(f.read())
    flags = find_flags(map)
    entities = set()

    for f in flags:
        e = f[2].entities()
        print(e.arr)
        for i in range(e.size()):
            entities.add(e.get(i))

    var_array = EntityVarArray(Var(VarType.ARRAY, (VarType.UINT, [])), VarType.UINT)
    for e in entities:
        var_array.append(e)
    print(var_array.arr)

    for f in flags:
        f[2].vars['ent_list'] = var_array.arr

    with open(map_file, "wb") as f:
        f.write(write_map(map))
