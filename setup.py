#!/usr/bin/env python3

from setuptools import setup, find_packages
import os

def get_version():
    with open('VERSION') as istream:
        return istream.read().strip()

if __name__ == '__main__':
    setup(
        name='termux_hardware_stats',
        version=get_version(),
        description='The termux_hardware_stats joke in the world',
        url='http://github.com/tmck-code/termux-hardware-stats',
        author='Tom McKeesick',
        author_email='tmck01@gmail.com',
        license='MIT',
        packages=find_packages(),
        zip_safe=False,
        entry_points = {
            'console_scripts': ['termux-hardware-stats=termux_hardware_stats.cli:run'],
        },
    )
