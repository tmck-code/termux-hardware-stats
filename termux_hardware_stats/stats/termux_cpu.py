from collections import defaultdict, namedtuple
from itertools import takewhile
from dataclasses import dataclass, asdict, field
from os import strerror

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

@dataclass
class CPUGlobalStateReader:
    fpath: str
    n_cores: int

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

    @staticmethod
    def load_for_core(fpaths):
        return [int(next(open(fpath))) for fpath in fpaths]

    def load_all(self):
        for i in range(self.cpu_count):
            yield CPUFrequency(*CPUFrequencyReader.load_for_core(self.fpaths.for_core(i)))
