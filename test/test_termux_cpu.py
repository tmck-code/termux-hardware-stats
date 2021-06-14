from termux_hardware_stats.stats import termux_cpu
from dataclasses import asdict
import os
from glob import glob

FILE_DATA = '''\
CPU0
    CPU: 0
    Online: 1
    Isolated: 0
    First CPU: 0
    Busy%: 56
    Is busy: 1
    Not preferred: 0
    Nr running: 11
    Active CPUs: 4
    Need CPUs: 4
    Nr isolated CPUs: 0
    Boost: 0
    OPBoost: 0
CPU1
    CPU: 1
    Online: 1
    Isolated: 0
    First CPU: 0
    Busy%: 78
    Is busy: 1
    Not preferred: 0
    Nr running: 11
    Active CPUs: 4
    Need CPUs: 4
    Nr isolated CPUs: 0
    Boost: 0
    OPBoost: 0
CPU2
    CPU: 2
    Online: 1
    Isolated: 0
    First CPU: 0
    Busy%: 100
    Is busy: 1
    Not preferred: 0
    Nr running: 11
    Active CPUs: 4
    Need CPUs: 4
    Nr isolated CPUs: 0
    Boost: 0
    OPBoost: 0
CPU3
    CPU: 3
    Online: 1
    Isolated: 0
    First CPU: 0
    Busy%: 43
    Is busy: 1
    Not preferred: 0
    Nr running: 11
    Active CPUs: 4
    Need CPUs: 4
    Nr isolated CPUs: 0
    Boost: 0
    OPBoost: 0
'''

class TestTermuxCPU:
    @classmethod
    def setup_class(cls):
        with open('test/global_state.txt', 'w') as ostream:
            ostream.write(FILE_DATA)

    @classmethod
    def teardown_class(cls):
        if os.path.exists('test/global_state.txt'):
            os.remove('test/global_state.txt')
        for fpath in glob('test/core_*'):
            os.remove(fpath)

    def test_global_state(self):
        expected = [
            {
                'ActiveCPUs':     4,
                'Boost':          0,
                'BusyPercentage': 56,
                'CPU':            0,
                'FirstCPU':       0,
                'IsBusy':         1,
                'Isolated':       0,
                'NeedCPUs':       4,
                'NotPreferred':   0,
                'NrIsolatedCPUs': 0,
                'NrRunning':      11,
                'OPBoost':        0,
                'Online':         1,
            },
        ]
        result = list(termux_cpu.CPUGlobalStateReader(fpath='test/global_state.txt', n_cores=1).load_all())
        assert all(isinstance(el, termux_cpu.GlobalState) for el in result)
        assert asdict(result[0]) == expected[0]

    def test_core_usage(self):
        expected = [56, 78, 100, 43]
        result = termux_cpu.CPUGlobalStateReader(fpath='test/global_state.txt', n_cores=4).load_percentages()
        assert result == expected

    def test_core_frequencies(self):
        fpaths = [
            'test/core_{:d}_current',
            'test/core_{:d}_min',
            'test/core_{:d}_max',
        ]
        freqs = [
            {'current': 3500000, 'min': 18000, 'max': 3700000},
            {'current': 3000000, 'min': 20000, 'max': 3800000},
        ]
        for i, f in enumerate(freqs):
            for j, (key, data) in enumerate(f.items()):
                with open(fpaths[j].format(i), 'w') as ostream:
                    ostream.write(f'{data}\n')
        result = list(termux_cpu.CPUFrequencyReader(2, termux_cpu.CPUFrequencyFpaths(*fpaths)).load_all())
        assert all(isinstance(el, termux_cpu.CPUFrequency) for el in result)
        for i, r in enumerate(result):
            assert r == termux_cpu.CPUFrequency(**freqs[i])