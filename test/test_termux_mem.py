from termux_hardware_stats.stats import termux_mem
from dataclasses import asdict
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
            'Active':          4831040,
            'Active_anon':     3856004,
            'Active_file':     975036,
            'AnonPages':       4400704,
            'Bounce':          0,
            'Buffers':         8972,
            'Cached':          2729768,
            'CmaFree':         200,
            'CmaTotal':        495616,
            'CommitLimit':     9909664,
            'Committed_AS':    213869628,
            'DefragPoolFree':  1456,
            'Dirty':           100,
            'FastRPCUsed':     66652,
            'Inactive':        2159408,
            'Inactive_anon':   756392,
            'Inactive_file':   1403016,
            'IonTotalCache':   0,
            'IonTotalUsed':    357292,
            'KReclaimable':    543016,
            'KernelStack':     88988,
            'KgslCache':       84008,
            'Mapped':          1387028,
            'MemAvailable':    3772232,
            'MemFree':         1444048,
            'MemTotal':        11430728,
            'Mlocked':         164808,
            'NFS_Unstable':    0,
            'PageTables':      185200,
            'Percpu':          8800,
            'RealMemFree':     1442592,
            'SReclaimable':    156980,
            'SUnreclaim':      404312,
            'ShadowCallStack': 22248,
            'Shmem':           197364,
            'Slab':            561292,
            'SwapCached':      26800,
            'SwapFree':        3721160,
            'SwapTotal':       4194300,
            'Unevictable':     166040,
            'VmallocChunk':    0,
            'VmallocTotal':    262930368,
            'VmallocUsed':     224700,
            'Writeback':       12,
            'WritebackTmp':    0
        }
        result = termux_mem.MemInfoReader('test/meminfo.txt').load_all()
        assert isinstance(result, termux_mem.MemoryInfoComplete)
        assert asdict(result) == expected

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
        assert isinstance(result, termux_mem.MemoryInfo)
        assert asdict(result) == expected
