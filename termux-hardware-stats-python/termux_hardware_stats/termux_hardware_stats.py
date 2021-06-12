#!/usr/bin/env python3

from dataclasses import dataclass
from collections import defaultdict, namedtuple
from itertools import takewhile, repeat
import multiprocessing
from functools import lru_cache


FPATHS = {
    'global_state': '/sys/devices/system/cpu/cpu{:d}/core_ctl/global_state',
	'curr_freq': '/sys/devices/system/cpu/cpu{:d}/cpufreq/scaling_cur_freq',
	'min_freq': '/sys/devices/system/cpu/cpu{:d}/cpufreq/scaling_min_freq',
	'max_freq': '/sys/devices/system/cpu/cpu{:d}/cpufreq/scaling_max_freq',
}

GlobalState = namedtuple(
    'GlobalState', [
        'CPU',
        'Online',
        'Isolated',
        'FirstCPU',
        'BusyPercentage',
        'IsBusy',
        'NotPreferred',
        'NrRunning',
        'ActiveCPUs',
        'NeedCPUs',
        'NrIsolatedCPUs',
        'Boost',
        'OPBoost',
    ]
)
CPUFrequency = namedtuple(
    'CPUFrequency', [
        'current',
        'min',
        'max',
    ]
)

@dataclass
class CPUGlobalStateReader:
    fpath: str
    n_cores: int

    def load_all(self):
        with open(self.fpath) as istream:
            next(istream)
            for i in range(self.n_cores):
                stats_chunk = list(takewhile(lambda x: not x.startswith('CPU'), istream))
                yield GlobalState(*list(map(lambda x: x.strip().split(': ')[1], stats_chunk)))._asdict()

FREQ_KEYS = ['curr_freq', 'min_freq', 'max_freq']

@dataclass
class CPUFrequencyReader:
    def load_for_core(n):
        return [int(next(open(FPATHS[k].format(n)))) for k in FREQ_KEYS]

    def load_all():
        for i in range(TermuxHardwareStats.cpu_count()):
            yield CPUFrequency(*CPUFrequencyReader.load_for_core(i))._asdict()

@dataclass
class TermuxHardwareStats:
    @lru_cache
    def cpu_count(logical=False):
        return multiprocessing.cpu_count()

    def cpu_percent():
        values = []
        for cpu_stats in CPUGlobalStateReader(FPATHS['global_state'].format(0), TermuxHardwareStats.cpu_count()).load_all():
            values.append(float(cpu_stats['BusyPercentage']))
        return values

    def cpu_freq():
        return list(CPUFrequencyReader.load_all())

