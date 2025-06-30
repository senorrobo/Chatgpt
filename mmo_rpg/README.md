# Simple 3D MMO RPG Skeleton

This directory contains a minimal skeleton of a 3D MMO RPG game using [Panda3D](https://www.panda3d.org/).

## Requirements
- Python 3.8+
- `panda3d`
- `websockets`

Install dependencies using the repository's requirements file (which will install Panda3D and websockets):

```zsh
pip install -r ../requirements.txt
```

If Panda3D fails to install automatically, run:

```zsh
pip install panda3d==1.10.14
```

## Running the Server

```zsh
python server.py
```

## Running the Client

```zsh
python main.py
```

The current implementation only loads a simple environment model and sets up a minimal websocket server for multiplayer communication. Use this as a starting point for building a full MMO RPG.

