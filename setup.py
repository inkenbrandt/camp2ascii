from setuptools import setup, Extension, find_packages
from setuptools.command.build_ext import build_ext
import subprocess

class CustomBuildExtCommand(build_ext):
    def run(self):
        subprocess.check_call(['make', '-C', 'camp2ascii/c_src'])
        super().run()

setup(
    name='camp2ascii',
    version='0.1',
    packages=find_packages(),
    ext_modules=[
        Extension(
            'camp2ascii',
            sources=[
                'camp2ascii/c_src/camp2ascii.c',
                'camp2ascii/c_src/files.c',
                'camp2ascii/c_src/frame_read.c',
                'camp2ascii/c_src/generic_functions.c',
                'camp2ascii/c_src/initializations.c',
                'camp2ascii/c_src/types_processing.c'
            ],
            include_dirs=['camp2ascii/c_src']
        )
    ],
    cmdclass={
        'build_ext': CustomBuildExtCommand,
    },
    install_requires=[
        # Add any dependencies your package requires
    ],
    entry_points={
        'console_scripts': [
            'camp2ascii = camp2ascii.converter:main',
        ],
    },
)
