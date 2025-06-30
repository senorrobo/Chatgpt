import asyncio

try:
    from direct.showbase.ShowBase import ShowBase
    from panda3d.core import Vec3, WindowProperties
    from panda3d.bullet import (
        BulletWorld,
        BulletPlaneShape,
        BulletRigidBodyNode,
        BulletCapsuleShape,
        BulletCharacterControllerNode,
    )
except ModuleNotFoundError:
    print(
        "Panda3D is required to run this example."
        " Install it with `pip install panda3d==1.10.14` and re-run the script."
    )
    raise SystemExit(1)


class MMORPG(ShowBase):
    """Basic MMO client with FPS controls and Bullet physics."""

    def __init__(self):
        super().__init__()

        # FPS style mouse control
        self.disableMouse()
        props = WindowProperties()
        props.setCursorHidden(True)
        props.setMouseMode(WindowProperties.M_relative)
        self.win.requestProperties(props)
        self.cam_pitch = 0.0

        # Bullet physics world
        self.world = BulletWorld()
        self.world.setGravity(Vec3(0, 0, -9.81))

        # Ground plane
        ground_shape = BulletPlaneShape(Vec3(0, 0, 1), 0)
        ground_node = BulletRigidBodyNode("Ground")
        ground_node.addShape(ground_shape)
        ground_np = self.render.attachNewNode(ground_node)
        self.world.attachRigidBody(ground_node)

        # Player character
        capsule = BulletCapsuleShape(0.5, 1.0, 1)
        self.character = BulletCharacterControllerNode(capsule, 0.4, "Player")
        self.character.setGravity(9.81)
        self.character_np = self.render.attachNewNode(self.character)
        self.character_np.setPos(0, 0, 2)
        self.world.attachCharacter(self.character)

        # Camera follows the player
        self.camera.reparentTo(self.character_np)
        self.camera.setPos(0, 0, 1.5)

        self.set_background_color(0, 0, 0.2)

        # Load a simple environment model
        self.environ = self.loader.loadModel("models/environment")
        self.environ.reparent_to(self.render)
        self.environ.set_scale(0.25)
        self.environ.set_pos(-8, 42, 0)

        # Keyboard controls
        self.keys = {"forward": False, "back": False, "left": False, "right": False}
        for key, name in {
            "w": "forward",
            "s": "back",
            "a": "left",
            "d": "right",
        }.items():
            self.accept(key, self.set_key, [name, True])
            self.accept(f"{key}-up", self.set_key, [name, False])
        self.accept("space", self.do_jump)

        self.taskMgr.add(self.update, "update")

    def set_key(self, name: str, value: bool) -> None:
        self.keys[name] = value

    def do_jump(self) -> None:
        if self.character.canJump():
            self.character.setMaxJumpHeight(2.0)
            self.character.setJumpSpeed(8.0)
            self.character.doJump()

    def update(self, task):
        dt = globalClock.getDt()

        # Mouse look
        if self.mouseWatcherNode.hasMouse():
            md = self.win.getPointer(0)
            x = md.getX()
            y = md.getY()
            self.win.movePointer(0, self.win.getXSize() // 2, self.win.getYSize() // 2)
            self.character_np.setH(self.character_np.getH() - (x - self.win.getXSize() / 2) * 0.1)
            self.cam_pitch = max(-90.0, min(90.0, self.cam_pitch - (y - self.win.getYSize() / 2) * 0.1))
            self.camera.setP(self.cam_pitch)

        # Movement
        move = Vec3(0, 0, 0)
        speed = 5.0
        if self.keys["forward"]:
            move.y += speed
        if self.keys["back"]:
            move.y -= speed
        if self.keys["left"]:
            move.x -= speed
        if self.keys["right"]:
            move.x += speed
        self.character.setLinearMovement(move, True)
        self.character.setAngularMovement(0)

        # Step the physics world
        self.world.doPhysics(dt, 4, 1 / 240.0)
        return task.cont


async def main():
    game = MMORPG()
    game.run()


if __name__ == "__main__":
    asyncio.run(main())
