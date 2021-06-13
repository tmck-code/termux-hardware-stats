#!/usr/bin/env python3

from dataclasses import dataclass
from collections import defaultdict, namedtuple
from itertools import takewhile, repeat
import multiprocessing
from functools import lru_cache

from termux_hardware_stats.stats import termux_cpu, termux_mem

FPATHS = {
    'global_state': '/sys/devices/system/cpu/cpu{:d}/core_ctl/global_state',
	'curr_freq': '/sys/devices/system/cpu/cpu{:d}/cpufreq/scaling_cur_freq',
	'min_freq': '/sys/devices/system/cpu/cpu{:d}/cpufreq/scaling_min_freq',
	'max_freq': '/sys/devices/system/cpu/cpu{:d}/cpufreq/scaling_max_freq',
    'mem_info': '/proc/meminfo',
}

@dataclass
class TermuxHardwareStats:
    @lru_cache
    def cpu_count(logical=False):
        return multiprocessing.cpu_count()

    def cpu_percent():
        values = []
        for cpu_stats in termux_cpu.CPUGlobalStateReader(FPATHS['global_state'].format(0), TermuxHardwareStats.cpu_count()).load_all():
            values.append(float(cpu_stats['BusyPercentage']))
        return values

    def cpu_freq():
        return list(termux_cpu.CPUFrequencyReader.load_all())

    def mem_info():
        info = termux_mem.MemInfoReader(FPATHS['mem_info']).load_all()
        pct = 100*(float(info['MemTotal'][0]) - float(info['MemFree'][0])) / float(info['MemTotal'][0])
        return {
            'UsedPercentage': round(pct, 2),
            'Total': info['MemTotal'],
        }

