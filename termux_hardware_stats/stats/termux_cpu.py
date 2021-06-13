from collections import namedtuple
from itertools import takewhile
from dataclasses import dataclass

FREQ_KEYS = ['curr_freq', 'min_freq', 'max_freq']

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

@dataclass
class CPUFrequencyReader:
    cpu_count: int

    def load_for_core(n):
        return [int(next(open(FPATHS[k].format(n)))) for k in FREQ_KEYS]

    def load_all(self):
        for i in range(self.cpu_count):
            yield CPUFrequency(*CPUFrequencyReader.load_for_core(i))._asdict()