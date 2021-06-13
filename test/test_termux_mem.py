from termux_hardware_stats.stats import termux_mem
import os

FILE_DATA = '''\
MemTotal:       11430728 kB
MemFree:         1444048 kB
MemAvailable:    3772232 kB
Buffers:            8972 kB
Cached:          2729768 kB
SwapCached:        26800 kB
Active:          4831040 kB
Inactive:        2159408 kB
Active(anon):    3856004 kB
Inactive(anon):   756392 kB
Active(file):     975036 kB
Inactive(file):  1403016 kB
Unevictable:      166040 kB
Mlocked:          164808 kB
SwapTotal:       4194300 kB
SwapFree:        3721160 kB
Dirty:               100 kB
Writeback:            12 kB
AnonPages:       4400704 kB
Mapped:          1387028 kB
Shmem:            197364 kB
KReclaimable:     543016 kB
Slab:             561292 kB
SReclaimable:     156980 kB
SUnreclaim:       404312 kB
KernelStack:       88988 kB
ShadowCallStack:   22248 kB
PageTables:       185200 kB
NFS_Unstable:          0 kB
Bounce:                0 kB
WritebackTmp:          0 kB
CommitLimit:     9909664 kB
Committed_AS:   213869628 kB
VmallocTotal:   262930368 kB
VmallocUsed:      224700 kB
VmallocChunk:          0 kB
Percpu:             8800 kB
IonTotalCache:         0 kB
IonTotalUsed:     357292 kB
CmaTotal:         495616 kB
CmaFree:             200 kB
FastRPCUsed:       66652 kB
KgslCache:         84008 kB
DefragPoolFree:     1456 kB
RealMemFree:     1442592 kB
'''

class TestTermuxMem:
    @classmethod
    def setup_class(cls):
        with open('test/meminfo.txt', 'w') as ostream:
            ostream.write(FILE_DATA)

    @classmethod
    def teardown_class(cls):
        if os.path.exists('test/meminfo.txt'):
            os.remove('test/meminfo.txt')

    def test_mem_load_all(self):
        expected = {
            'Active':          ['4831040', 'kB'],
            'Active_anon':     ['3856004', 'kB'],
            'Active_file':     ['975036', 'kB'],
            'AnonPages':       ['4400704', 'kB'],
            'Bounce':          ['0', 'kB'],
            'Buffers':         ['8972', 'kB'],
            'Cached':          ['2729768', 'kB'],
            'CmaFree':         ['200', 'kB'],
            'CmaTotal':        ['495616', 'kB'],
            'CommitLimit':     ['9909664', 'kB'],
            'Committed_AS':    ['213869628', 'kB'],
            'DefragPoolFree':  ['1456', 'kB'],
            'Dirty':           ['100', 'kB'],
            'FastRPCUsed':     ['66652', 'kB'],
            'Inactive':        ['2159408', 'kB'],
            'Inactive_anon':   ['756392', 'kB'],
            'Inactive_file':   ['1403016', 'kB'],
            'IonTotalCache':   ['0', 'kB'],
            'IonTotalUsed':    ['357292', 'kB'],
            'KReclaimable':    ['543016', 'kB'],
            'KernelStack':     ['88988', 'kB'],
            'KgslCache':       ['84008', 'kB'],
            'Mapped':          ['1387028', 'kB'],
            'MemAvailable':    ['3772232', 'kB'],
            'MemFree':         ['1444048', 'kB'],
            'MemTotal':        ['11430728', 'kB'],
            'Mlocked':         ['164808', 'kB'],
            'NFS_Unstable':    ['0', 'kB'],
            'PageTables':      ['185200', 'kB'],
            'Percpu':          ['8800', 'kB'],
            'RealMemFree':     ['1442592', 'kB'],
            'SReclaimable':    ['156980', 'kB'],
            'SUnreclaim':      ['404312', 'kB'],
            'ShadowCallStack': ['22248', 'kB'],
            'Shmem':           ['197364', 'kB'],
            'Slab':            ['561292', 'kB'],
            'SwapCached':      ['26800', 'kB'],
            'SwapFree':        ['3721160', 'kB'],
            'SwapTotal':       ['4194300', 'kB'],
            'Unevictable':     ['166040', 'kB'],
            'VmallocChunk':    ['0', 'kB'],
            'VmallocTotal':    ['262930368', 'kB'],
            'VmallocUsed':     ['224700', 'kB'],
            'Writeback':       ['12', 'kB'],
            'WritebackTmp':    ['0', 'kB']
        }
        result = termux_mem.MemInfoReader('test/meminfo.txt').load_all()
        assert result == expected

    def test_mem_load(self):
        expected = {
            'ram': {
                'available': 3772232,
                'used':      6686648, # TODO: check this value
                'free':      1444048,
                'total':     11430728,
                'shared':    197364,
            },
            'swap': {
                'cached': 26800,
                'free':   3721160,
                'total':  4194300,
            }
        }
        result = termux_mem.MemInfoReader('test/meminfo.txt').load()
        assert result == expected
