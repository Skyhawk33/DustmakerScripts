from dustmaker import *

map = Map()
dustblocks = ((TileSpriteSet.mansion, 21),
              (TileSpriteSet.forest, 13),
              (TileSpriteSet.city, 6),
              (TileSpriteSet.laboratory, 9),
              (TileSpriteSet.tutorial, 2))

y = 0
for set, type in dustblocks:
    for i in TileShape:
        t = Tile(i)
        t.sprite_set(set)
        t.sprite_tile(type)
        for j in range(4):
            t.edge_bits(j, 0)

        map.add_tile(19, y, 2 * i, t)
    y += 2

map_file = 'C:/Program Files (x86)/Steam/steamapps/common/Dustforce/user/level_src/edgeless'
map.name('edgeless')
with open(map_file, "wb") as f:
    f.write(write_map(map))
