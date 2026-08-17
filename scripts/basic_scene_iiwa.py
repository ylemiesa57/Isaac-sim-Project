"""Basic Isaac Sim scene and KUKA iiwa robot loader.

This module provides a minimal template for loading a scene with a KUKA iiwa robot
in NVIDIA Isaac Sim. It demonstrates how to initialize the simulation, add a ground
plane, optionally load a custom scene, and load the robot asset.
"""
import argparse

from omni.isaac.kit import SimulationApp

CONFIG = {"headless": False}
simulation_app = SimulationApp(CONFIG)

from omni.isaac.core import World  # noqa: E402
from omni.isaac.core.utils.nucleus import get_assets_root_path  # noqa: E402
from omni.isaac.core.utils.stage import add_reference_to_stage  # noqa: E402


def build_scene(scene_path: str) -> bool:
    """Build the simulation scene with optional custom environment and KUKA iiwa robot.

    Args:
        scene_path: Absolute path to a custom USD scene file, or empty string for default.

    Returns:
        True if the scene was built successfully with the robot loaded, False otherwise.
        The function will complete scene setup (ground plane, custom scene) even if
        the robot asset cannot be loaded.

    Note:
        Requires a working Nucleus connection to resolve Isaac Sim assets.
        If the assets root path cannot be resolved, a warning is printed and the
        robot will not be loaded.
    """
    world = World(stage_units_in_meters=1.0)
    world.scene.add_default_ground_plane()

    if scene_path:
        add_reference_to_stage(scene_path, "/World/Scene")

    assets_root = get_assets_root_path()
    if not assets_root:
        print("Could not find Isaac Sim assets root. Check Nucleus connection.")
        world.reset()
        for _ in range(300):
            world.step(render=True)
        return False

    iiwa_usd = assets_root + "/Isaac/Robots/KUKA/iiwa/iiwa.usd"
    add_reference_to_stage(iiwa_usd, "/World/IIWA")

    world.reset()
    for _ in range(300):
        world.step(render=True)
    return True


def main() -> None:
    """Main entry point for the Isaac Sim scene loader.

    Parses command-line arguments and initializes the simulation scene.
    """
    parser = argparse.ArgumentParser(description="Basic scene + KUKA iiwa loader")
    parser.add_argument("--scene", default="", help="Absolute path to a USD scene")
    args = parser.parse_args()

    build_scene(args.scene)
    simulation_app.close()


if __name__ == "__main__":
    main()
