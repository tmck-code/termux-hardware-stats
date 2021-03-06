from collections import defaultdict, namedtuple
from itertools import takewhile
from dataclasses import dataclass, asdict, field
from os import strerror
import multiprocessing
from functools import lru_cache

DEFAULT_GLOBAL_STATE_FPATH = '/sys/devices/system/cpu/cpu0/core_ctl/global_state'

FREQ_KEYS = ['curr_freq', 'min_freq', 'max_freq']

FPATHS = {
	'curr_freq': '/sys/devices/system/cpu/cpu{:d}/cpufreq/scaling_cur_freq',
	'min_freq': '/sys/devices/system/cpu/cpu{:d}/cpufreq/scaling_min_freq',
	'max_freq': '/sys/devices/system/cpu/cpu{:d}/cpufreq/scaling_max_freq',
}

@dataclass
class GlobalState:
    CPU:            str
    Online:         str
    Isolated:       str
    FirstCPU:       str
    BusyPercentage: str
    IsBusy:         str
    NotPreferred:   str
    NrRunning:      str
    ActiveCPUs:     str
    NeedCPUs:       str
    NrIsolatedCPUs: str
    Boost:          str
    OPBoost:        str

@dataclass
class CPUFrequency:
    current: int
    min:     int
    max:     int

@lru_cache
def cpu_count():
    return multiprocessing.cpu_count()

@dataclass
class CPUGlobalStateReader:
    n_cores: int = cpu_count()
    fpath: str = DEFAULT_GLOBAL_STATE_FPATH

    def load_all(self):
        with open(self.fpath) as istream:
            next(istream)
            for i in range(self.n_cores):
                stats_chunk = list(takewhile(lambda x: not x.startswith('CPU'), istream))
                yield GlobalState(*list(map(lambda x: int(x.strip().split(': ')[1]), stats_chunk)))

    def load_percentages(self):
        return [core.BusyPercentage for core in self.load_all()]

@dataclass
class CPUFrequencyFpaths:
    current: str = FPATHS['curr_freq']
    min:     str = FPATHS['min_freq']
    max:     str = FPATHS['max_freq']

    def for_core(self, n):
        return [s.format(n) for s in [self.current, self.min, self.max]]

    def __iter__(self):
        yield from [self.current, self.min, self.max]

@dataclass
class CPUFrequencyReader:
    cpu_count: int
    fpaths:    CPUFrequencyFpaths = field(default_factory=CPUFrequencyFpaths)

    def load_for_core(self, n):
        return [int(next(open(fpath))) for fpath in self.fpaths.for_core(n)]

    def load_all(self):
        for i in range(self.cpu_count):
            yield CPUFrequency(*self.load_for_core(i))
