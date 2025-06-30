# Simple 3D MMO RPG Skeleton

This directory contains a minimal 3D multiplayer demo built with [Panda3D](https://www.panda3d.org/) and `websockets`.

## Setup

Install the shared dependencies from the repository root:

```zsh
python3 -m pip install -r ../requirements.txt
```

If Panda3D does not install automatically, run:

```zsh
python3 -m pip install panda3d==1.10.14
```

## Running

Start the websocket server:

```zsh
python3 server.py
```

Open another terminal in this directory and run the client:

```zsh
python3 main.py
```

The client simply loads Panda3D's sample environment and connects to the server. Use it as a starting point for your own MMO project.
