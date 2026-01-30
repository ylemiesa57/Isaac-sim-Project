# Isaac Sim Project (Template)

Minimal Isaac Sim template that loads a basic scene (optional) and spawns a KUKA iiwa robot.

## Run
From your Isaac Sim install directory:

```
./python.sh /Users/yaphetlemiesa/yaphet-lemiesa/Isaac-sim-Project/scripts/basic_scene_iiwa.py
```

Optional: load a custom USD scene

```
./python.sh /Users/yaphetlemiesa/yaphet-lemiesa/Isaac-sim-Project/scripts/basic_scene_iiwa.py --scene /absolute/path/to/scene.usd
```

## Notes
- Requires a working Nucleus connection to resolve Isaac assets.
- The iiwa asset path used is `Isaac/Robots/KUKA/iiwa/iiwa.usd`.
