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
    'mem_info': '/proc/meminfo',
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
MemoryInfo = namedtuple(
    'MemoryInfo', [
        'MemTotal',
        'MemFree',
        'MemAvailable',
        'Buffers',
        'Cached',
        'SwapCached',
        'Active',
        'Inactive',
        'Active_anon',
        'Inactive_anon',
        'Active_file',
        'Inactive_file',
        'Unevictable',
        'Mlocked',
        'SwapTotal',
        'SwapFree',
        'Dirty',
        'Writeback',
        'AnonPages',
        'Mapped',
        'Shmem',
        'KReclaimable',
        'Slab',
        'SReclaimable',
        'SUnreclaim',
        'KernelStack',
        'ShadowCallStack',
        'PageTables',
        'NFS_Unstable',
        'Bounce',
        'WritebackTmp',
        'CommitLimit',
        'Committed_AS',
        'VmallocTotal',
        'VmallocUsed',
        'VmallocChunk',
        'Percpu',
        'IonTotalCache',
        'IonTotalUsed',
        'CmaTotal',
        'CmaFree',
        'FastRPCUsed',
        'KgslCache',
        'DefragPoolFree',
        'RealMemFree',
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
class MemInfoReader:
    fpath: str

    def load_all(self):
        with open(self.fpath) as istream:
            return MemoryInfo(*list(map(lambda x: x.strip().split(': ')[1].strip().split(' '), istream)))._asdict()

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

    def mem_info():
        info = MemInfoReader(FPATHS['mem_info']).load_all()
        pct = 100*(float(info['MemTotal'][0]) - float(info['MemFree'][0])) / float(info['MemTotal'][0])
        return {
            'UsedPercentage': round(pct, 2),
            'Total': info['MemTotal'],
        }

