import noise
import numpy as np

from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

SHAPE = 64
SCALE = 0.5
OCTAVES = 6
PERSISTENCE = 0.6
LACUNARITY = 2
SEED = np.random.randint(0, 100)

WORLD = np.zeros((SHAPE, SHAPE))

X_IDX = np.linspace(0, 1, SHAPE)
Y_IDX = np.linspace(0, 1, SHAPE)
WORLD_X, WORLD_Y = np.meshgrid(X_IDX, Y_IDX)

# apply perlin noise, instead of np.vectorize, consider using itertools.starmap()
WORLD = np.vectorize(noise.pnoise2)(WORLD_X / SCALE, WORLD_Y / SCALE, octaves=OCTAVES, persistence=PERSISTENCE,
                                    lacunarity=LACUNARITY, repeatx=SHAPE, repeaty=SHAPE, base=SEED)


class Block(Button):
    def __init__(self, position=(0, 0, 0)):
        super().__init__(
            parent=scene,
            position=position,
            model="cube",
            texture="white_cube",
            color=color.white,
            highlight_color=color.cyan
        )


cubes = []
app = Ursina()

for x in range(SHAPE):
    for z in range(SHAPE):
        y_max = int(10 * WORLD[z][x])
        for y in range(y_max - 2, y_max):
            cubes.append(Block((x, y, z)))

player = FirstPersonController()

app.run()
