import asyncio
from dataclasses import dataclass

try:
    from direct.showbase.ShowBase import ShowBase
    from direct.gui.OnscreenText import OnscreenText
    from panda3d.core import DirectionalLight, AmbientLight, Vec4
except ModuleNotFoundError:
    print(
        "Panda3D is required to run this demo."
        " Install it with `pip install panda3d==1.10.14` and re-run the script."
    )
    raise SystemExit(1)

@dataclass
class Race:
    name: str
    abilities: list[str]
    day_buff: str
    night_buff: str

RACES = {
    "vampire": Race(
        name="Vampire",
        abilities=["heal on hit", "bat dash"],
        day_buff="Sunlight weakness",
        night_buff="Life steal"),
    "werewolf": Race(
        name="Werewolf",
        abilities=["transform at night"],
        day_buff="Weakened by silver",
        night_buff="Enhanced strength"),
    "elf": Race(
        name="Elf",
        abilities=["quick movement", "elemental magic"],
        day_buff="None",
        night_buff="Improved vision"),
    "human": Race(
        name="Human",
        abilities=["advanced technology"],
        day_buff="Balanced stats",
        night_buff="Team tactics"),
}

@dataclass
class Player:
    race: Race
    health: int = 100

class SoultopiaDemo(ShowBase):
    def __init__(self, race_name: str):
        super().__init__()
        self.disableMouse()
        self.camera.set_pos(0, -50, 10)

        self.environ = self.loader.loadModel('models/environment')
        self.environ.reparent_to(self.render)
        self.environ.set_scale(0.25)
        self.environ.set_pos(-8, 42, 0)

        self.player = Player(RACES[race_name])
        self.info = OnscreenText(text=f"Race: {self.player.race.name}",
                                 pos=(-1.3, 0.9), fg=(1,1,1,1),
                                 align=0, scale=0.07)

        self.alight = AmbientLight('alight')
        self.alight.set_color(Vec4(0.2, 0.2, 0.2, 1))
        self.alnp = self.render.attach_new_node(self.alight)

        self.dlight = DirectionalLight('dlight')
        self.dlight.set_color(Vec4(1, 1, 0.9, 1))
        self.dlnp = self.render.attach_new_node(self.dlight)
        self.dlnp.set_hpr(0, -60, 0)

        self.render.set_light(self.alnp)
        self.render.set_light(self.dlnp)

        self.taskMgr.add(self.update_time, 'update_time')

    def update_time(self, task):
        time = int(task.time) % 20
        if time < 10:
            # Day
            self.dlight.set_color(Vec4(1, 1, 0.9, 1))
        else:
            # Night
            self.dlight.set_color(Vec4(0.2, 0.2, 0.5, 1))
        return task.cont

async def main(race_name='human'):
    game = SoultopiaDemo(race_name)
    game.run()

if __name__ == '__main__':
    import sys
    race = sys.argv[1] if len(sys.argv) > 1 else 'human'
    if race not in RACES:
        print(
            f"Unknown race '{race}'. Available races: {', '.join(RACES.keys())}"
        )
        sys.exit(1)
    asyncio.run(main(race))
