import sys
from typing import Optional

from sample_factory.cfg.arguments import parse_full_cfg, parse_sf_args

def parse_custom_args(argv=None, evaluation=False):
    parser, cfg = parse_sf_args(argv=argv, evaluation=evaluation)
    # cfg = parse_full_cfg(parser, argv)
    return cfg

cfg = parse_custom_args()

print(cfg)
