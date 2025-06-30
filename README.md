# Chatgpt Game Projects

This repository hosts two small game examples built with [Panda3D](https://www.panda3d.org/).

- `mmo_rpg` – a bare-bones 3D MMO RPG skeleton showing a simple Panda3D client and websocket server.
- `soultopia` – a demo and design document for a large scale MMORPG concept.

## Setup

These projects work on macOS and Linux. Install the dependencies into your Python environment:

```zsh
python3 -m pip install -r requirements.txt
```

If Panda3D fails to install automatically (which can happen on some systems), run:

```zsh
python3 -m pip install panda3d==1.10.14
```

## MMO RPG Skeleton

Run the websocket server:

```zsh
cd mmo_rpg
python3 server.py
```

In another terminal, launch the Panda3D client:

```zsh
python3 main.py
```
The client includes basic WASD movement, a first-person camera, and Bullet physics.
Terrain chunks load with collision meshes so you can walk on the scenery, and the
camera no longer snaps back when you move the mouse.

## Soultopia Demo

The Soultopia directory contains the design document and a small race selection demo. Start it with:

```zsh
cd soultopia
python3 main.py <race>
```

Replace `<race>` with `vampire`, `werewolf`, `elf`, or `human`.

See `soultopia/README.md` for lore and gameplay ideas.
