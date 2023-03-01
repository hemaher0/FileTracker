# Import modules
import os
import shutil
import threading
import time
import tkinter

# Define objects to expose
__all__ = []

# Initialize package-level state

# Register entry point
from setuptools import setup
setup(
    name='File_Tracker',
    entry_points={
        'console_scripts' : [
            'my_command=File_Tracker.command:main',
        ]
    }
)

# 1. File selection

# 2. Backup location

# 3. Incremental backup

# 4. Compression

# 5. Encryption

# 6. Verification
# 7. Scheduling
# 8. Error handling

__name__