import asyncio
from direct.showbase.ShowBase import ShowBase

class MMORPG(ShowBase):
    def __init__(self):
        super().__init__()
        self.disableMouse()
        self.camera.set_pos(0, -50, 10)
        self.set_background_color(0, 0, 0.2)
        # Load a simple environment model
        self.environ = self.loader.loadModel('models/environment')
        self.environ.reparent_to(self.render)
        self.environ.set_scale(0.25, 0.25, 0.25)
        self.environ.set_pos(-8, 42, 0)

async def main():
    game = MMORPG()
    game.run()

if __name__ == '__main__':
    asyncio.run(main())
