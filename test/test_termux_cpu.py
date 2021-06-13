from termux_hardware_stats.stats import termux_cpu
import os

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
CPU4
	CPU: 4
	Online: 1
	Isolated: 0
	First CPU: 4
	Busy%: 84
	Is busy: 1
	Not preferred: 0
	Nr running: 9
	Active CPUs: 3
	Need CPUs: 3
	Nr isolated CPUs: 0
	Boost: 0
	OPBoost: 0
CPU5
	CPU: 5
	Online: 1
	Isolated: 0
	First CPU: 4
	Busy%: 100
	Is busy: 1
	Not preferred: 0
	Nr running: 9
	Active CPUs: 3
	Need CPUs: 3
	Nr isolated CPUs: 0
	Boost: 0
	OPBoost: 0
CPU6
	CPU: 6
	Online: 1
	Isolated: 0
	First CPU: 4
	Busy%: 100
	Is busy: 1
	Not preferred: 0
	Nr running: 9
	Active CPUs: 3
	Need CPUs: 3
	Nr isolated CPUs: 0
	Boost: 0
	OPBoost: 0
CPU7
	CPU: 7
	Online: 1
	Isolated: 0
	First CPU: 7
	Busy%: 100
	Is busy: 1
	Not preferred: 0
	Nr running: 3
	Active CPUs: 1
	Need CPUs: 1
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

    def test_global_state(self):
        expected = [
            {
                'ActiveCPUs':     '4',
                'Boost':          '0',
                'BusyPercentage': '56',
                'CPU':            '0',
                'FirstCPU':       '0',
                'IsBusy':         '1',
                'Isolated':       '0',
                'NeedCPUs':       '4',
                'NotPreferred':   '0',
                'NrIsolatedCPUs': '0',
                'NrRunning':      '11',
                'OPBoost':        '0',
                'Online':         '1',
            },
        ]
        result = list(termux_cpu.CPUGlobalStateReader('test/global_state.txt', 1).load_all())
        assert result == expected
