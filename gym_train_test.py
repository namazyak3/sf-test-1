import sys
from typing import Optional

import gymnasium as gym

from sample_factory.cfg.arguments import parse_full_cfg, parse_sf_args
from sample_factory.envs.env_utils import register_env
from sample_factory.train import run_rl

from mlagents_envs.environment import UnityEnvironment
from mlagents_envs.envs.unity_gym_env import UnityToGymWrapper

def make_gym_env_func(full_env_name, cfg=None, env_config=None, render_mode: Optional[str] = None):
    file_name = cfg.env_args[0] if cfg.env_args else None
    worker_id = env_config.worker_index if env_config else 0
    unity_env = UnityEnvironment(file_name=full_env_name, base_port=5005, worker_id=worker_id)
    return UnityToGymWrapper(unity_env=unity_env, uint8_visual=False)

def register_custom_components():
    register_env("JetRacerTasks", make_gym_env_func)


def parse_custom_args(argv=None, evaluation=False):
    parser, cfg = parse_sf_args(argv=argv, evaluation=evaluation)
    cfg = parse_full_cfg(parser, argv)
    return cfg


def main():
    register_custom_components()
    cfg = parse_custom_args()
    status = run_rl(cfg)
    return status


if __name__ == "__main__":
    sys.exit(main())
