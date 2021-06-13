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
    cpu_count: int

    def load_for_core(n):
        return [int(next(open(FPATHS[k].format(n)))) for k in FREQ_KEYS]

    def load_all():
        for i in range(TermuxHardwareStats.cpu_count()):
            yield CPUFrequency(*CPUFrequencyReader.load_for_core(i))._asdict()