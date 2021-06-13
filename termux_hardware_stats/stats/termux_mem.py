from dataclasses import dataclass, asdict
from collections import namedtuple

MemoryInfoComplete = namedtuple(
    'MemoryInfoComplete', [
        'MemTotal',
        'MemFree', # The amount of physical memory not used by the system
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
        'Shmem', # Total used shared memory (shared between several processes, thus including RAM disks, SYS-V-IPC and BSD like SHMEM)
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
class RamInfo:
    available: int
    free:      int
    total:     int
    used:      int
    shared:    int

@dataclass
class SwapInfo:
    cached: int
    free:   int
    total:  int

@dataclass
class MemoryInfo:
    ram: RamInfo
    swap: SwapInfo

@dataclass
class MemInfoReader:
    fpath: str

    def load_all(self) -> MemoryInfoComplete:
        with open(self.fpath) as istream:
            return MemoryInfoComplete(*list(map(lambda x: x.strip().split(': ')[1].strip().split(' '), istream)))._asdict()

    def load(self):
        info = self.load_all()
        return asdict(MemoryInfo(
            ram=RamInfo(
                available = int(info['MemAvailable'][0]),
                free      = int(info['MemFree'][0]),
                used      = int(
                    int(info['MemTotal'][0]) \
                        - int(info['MemFree'][0])  \
                        - int(info['Buffers'][0])  \
                        - int(info['Cached'][0]) - int(info['Slab'][0])
                ),
                total     = int(info['MemTotal'][0]),
                shared    = int(info['Shmem'][0]),
            ),
            swap=SwapInfo(
                cached = int(info['SwapCached'][0]),
                free   = int(info['SwapFree'][0]),
                total  = int(info['SwapTotal'][0]),
            )
        ))
