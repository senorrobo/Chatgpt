# Chatgpt Game Projects

This repository contains experimental game projects. The `mmo_rpg` directory includes a simple 3D MMO RPG skeleton built with Panda3D. A full game design document for a much larger concept, **Soultopia**, along with a small demo, can be found in the `soultopia` directory.

```
./mmo_rpg
./soultopia
```

These instructions work on macOS and Linux. Install dependencies (which include Panda3D) with:

```zsh
python3 -m pip install -r requirements.txt
```

If Panda3D fails to install automatically, install it manually with:

```zsh
python3 -m pip install panda3d==1.10.14
```

See the respective `README.md` files for details.

To try the Soultopia demo, run:

```zsh
cd soultopia
python3 main.py human
```
