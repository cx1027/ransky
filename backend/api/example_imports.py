import sys
import os
from pathlib import Path

# Method 1: Using pathlib (Recommended)
current_file = Path(__file__)
parent_dir = current_file.parent.parent  # Go up to parent
sibling_dir = parent_dir / "app"  # Go to sibling folder "app"
sys.path.insert(0, str(parent_dir))

# Now you can import from sibling folder
from app.api.main import api_router
from app.core.config import settings

# Method 2: Using os.path
current_dir = os.path.dirname(__file__)
parent_dir_os = os.path.abspath(os.path.join(current_dir, '..'))
sibling_dir_os = os.path.join(parent_dir_os, 'app')
sys.path.insert(0, parent_dir_os)

# Method 3: Direct relative path calculation
def get_sibling_path(sibling_folder_name):
    """Get path to sibling folder"""
    current = Path(__file__)
    parent = current.parent.parent
    sibling = parent / sibling_folder_name
    return str(sibling)

# Usage:
app_path = get_sibling_path("app")
sys.path.insert(0, app_path)

# Method 4: Using environment variable
os.environ['PYTHONPATH'] = os.pathsep.join([
    os.environ.get('PYTHONPATH', ''),
    str(Path(__file__).parent.parent)
])

# Method 5: Dynamic import (if you know the exact path)
import importlib.util
def import_from_path(module_name, file_path):
    """Import a module from a specific file path"""
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

# Usage example:
# app_module = import_from_path("app", "/path/to/app/__init__.py") 