import argparse

from omni.isaac.kit import SimulationApp

CONFIG = {"headless": False}
simulation_app = SimulationApp(CONFIG)

from omni.isaac.core import World  # noqa: E402
from omni.isaac.core.utils.nucleus import get_assets_root_path  # noqa: E402
from omni.isaac.core.utils.stage import add_reference_to_stage  # noqa: E402


def build_scene(scene_path: str) -> None:
    world = World(stage_units_in_meters=1.0)
    world.scene.add_default_ground_plane()

    if scene_path:
        add_reference_to_stage(scene_path, "/World/Scene")

    assets_root = get_assets_root_path()
    if not assets_root:
        print("Could not find Isaac Sim assets root. Check Nucleus connection.")
        return

    iiwa_usd = assets_root + "/Isaac/Robots/KUKA/iiwa/iiwa.usd"
    add_reference_to_stage(iiwa_usd, "/World/IIWA")

    world.reset()
    for _ in range(300):
        world.step(render=True)


def main() -> None:
    parser = argparse.ArgumentParser(description="Basic scene + KUKA iiwa loader")
    parser.add_argument("--scene", default="", help="Absolute path to a USD scene")
    args = parser.parse_args()

    build_scene(args.scene)
    simulation_app.close()


if __name__ == "__main__":
    main()
