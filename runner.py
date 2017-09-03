from __future__ import print_function

import sys
from importlib import import_module

from gflags import FLAGS

NOTHING = object()


def run(agent, module_args=[], method="entry_point"):
    if not isinstance(module_args, list):
        module_args = module_args.split(" ")
    module = import_module(agent)
    func = getattr(module, method, NOTHING)

    sys.argv[0] = module.__file__
    sys.argv[1:] = module_args
    return func(NOTHING)

