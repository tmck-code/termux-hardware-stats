from dataclasses import dataclass
from collections import namedtuple

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
class MemInfoReader:
    fpath: str

    def load_all(self):
        with open(self.fpath) as istream:
            return MemoryInfo(*list(map(lambda x: x.strip().split(': ')[1].strip().split(' '), istream)))._asdict()
