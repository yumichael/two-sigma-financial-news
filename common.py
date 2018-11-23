import notebook_import_hook
notebook_import_hook.attach()
from notebook_import_hook import top_dir


'''
> from sys import path
> from os.path import dirname
> print('\n'.join(path))
# The above prints the list of paths. When a Jupyter notebook is run within this top-level package
# (which, note, is special (by hacks) because I manually added its directory to $PYTHONPATH in my .bashrc)
# and imports this module, the printed list of paths will have the directory from which the notebook is run
# be located at index 3 (index 0 has empty string, indices 1 and 2 have the directories I added in my .bashrc),
# unless the notebook is located in the top level package directory, because Python gets rid of the duplicated path.
# So a TODO is to figure out when I'm importing this module from a Jupyter notebook in a subdirectory
# and manually remove the local subdirectory path from the sys.path in order to enforce using absolute file names.
'''
from pathlib import Path
the_data = top_dir/'data/'
big_data = Path('/big/data/')

from globals import *
from helper import *