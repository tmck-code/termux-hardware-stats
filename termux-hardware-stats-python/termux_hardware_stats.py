#!/usr/bin/env python3

import json


FPATHS = {
	'global_state': [
        '/sys/devices/system/cpu/cpu0/core_ctl/global_state',
        '/sys/devices/system/cpu/cpu4/core_ctl/global_state',
        '/sys/devices/system/cpu/cpu7/core_ctl/global_state',
    ]
}

from dataclasses import dataclass

@dataclass
class Grepper:
    fpath: str
    pattern: str

    def read(self):
        with open(self.fpath) as istream:
            for line in istream:
                if self.pattern in line:
                    yield line

@dataclass
class CPUStat:
    key: str
    n_cores: int


def parse_stats(grepper):
    for core, line in enumerate(grepper.read()):
        key, val = line.strip().split(': ')
        yield val

def read_stats(grepper):
    return list(parse_stats(grepper))

import psutil

import multiprocessing

@dataclass
class TermuxPSUtilHardwareStats:
    def cpu_count(logical=False):
        return multiprocessing.cpu_count()

    def cpu_times_percent(): pass
    def cpu_percent(): pass
    def cpu_freq(): pass

grepper = Grepper(FPATHS['global_state'][0], 'Busy%')
print(read_stats(grepper))
