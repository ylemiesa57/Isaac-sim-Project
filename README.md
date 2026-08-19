# Isaac Sim Project (Extension of MIT Learning Project for Robotic Manipulation)

Minimal Isaac Sim template that loads a basic scene (optional) and spawns a KUKA iiwa robot.

## Run
From your Isaac Sim install directory, provide the absolute path to the script (or adjust the path relative to your checkout):

```
./python.sh <path-to-repo>/scripts/basic_scene_iiwa.py
```

For example, if you cloned this repo to your home directory:

```
./python.sh ~/Isaac-sim-Project/scripts/basic_scene_iiwa.py
```

Optional: load a custom USD scene

```
./python.sh <path-to-repo>/scripts/basic_scene_iiwa.py --scene /absolute/path/to/scene.usd
```

## Notes
- Requires a working Nucleus connection to resolve Isaac assets.
- The iiwa asset path used is `Isaac/Robots/KUKA/iiwa/iiwa.usd`.
