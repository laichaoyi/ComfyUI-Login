from .password import *
import importlib.util
import glob
import os
import sys
import inspect

# For loading all custom js
WEB_DIRECTORY = "js"


NODE_CLASS_MAPPINGS = {}
NODE_DISPLAY_NAME_MAPPINGS = {}
DYNAMIC_INPUT_NODES = []

def init():
    py = os.path.dirname(__file__)
    files = glob.glob(os.path.join(py, "*.py"), recursive=False)
    for file in files:
        if(file == __file__):
            continue
        name = os.path.splitext(file)[0]
        spec = importlib.util.spec_from_file_location(name, file, submodule_search_locations=[])
        module = importlib.util.module_from_spec(spec)
        sys.modules[name] = module
        spec.loader.exec_module(module)
        if hasattr(module, "NODE_CLASS_MAPPINGS") and getattr(module, "NODE_CLASS_MAPPINGS") is not None:
            NODE_CLASS_MAPPINGS.update(module.NODE_CLASS_MAPPINGS)
            if hasattr(module, "NODE_DISPLAY_NAME_MAPPINGS") and getattr(module, "NODE_DISPLAY_NAME_MAPPINGS") is not None:
                NODE_DISPLAY_NAME_MAPPINGS.update(module.NODE_DISPLAY_NAME_MAPPINGS)
        
        
        clsmembers = inspect.getmembers(module, inspect.isclass)
        for clname, cl in clsmembers:
            if getattr(cl, "DYNAMIC_INPUT_NODES", False):
                if(clname not in DYNAMIC_INPUT_NODES):
                    DYNAMIC_INPUT_NODES.append(clname)
init()

__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS", "WEB_DIRECTORY"]