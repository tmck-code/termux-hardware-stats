from __future__ import annotations
from dataclasses import dataclass, asdict
from collections import namedtuple
from os import stat

DEFAULT_MEMINFO_FPATH = '/proc/meminfo'

@dataclass
class MemoryInfoComplete:
    MemTotal:        int
    MemFree:         int # The amount of physical memory not used by the system
    MemAvailable:    int
    Buffers:         int
    Cached:          int
    SwapCached:      int
    Active:          int
    Inactive:        int
    Active_anon:     int
    Inactive_anon:   int
    Active_file:     int
    Inactive_file:   int
    Unevictable:     int
    Mlocked:         int
    SwapTotal:       int
    SwapFree:        int
    Dirty:           int
    Writeback:       int
    AnonPages:       int
    Mapped:          int
    Shmem:           int # Total used shared memory (shared between several processes, thus including RAM disks, SYS-V-IPC and BSD like SHMEM)
    KReclaimable:    int
    Slab:            int
    SReclaimable:    int
    SUnreclaim:      int
    KernelStack:     int
    ShadowCallStack: int
    PageTables:      int
    NFS_Unstable:    int
    Bounce:          int
    WritebackTmp:    int
    CommitLimit:     int
    Committed_AS:    int
    VmallocTotal:    int
    VmallocUsed:     int
    VmallocChunk:    int
    Percpu:          int
    IonTotalCache:   int
    IonTotalUsed:    int
    CmaTotal:        int
    CmaFree:         int
    FastRPCUsed:     int
    KgslCache:       int
    DefragPoolFree:  int
    RealMemFree:     int

    @staticmethod
    def from_file(istream) -> MemoryInfoComplete:
        return MemoryInfoComplete(*list(map(lambda x: int(x.strip().split(': ')[1].strip().split(' ')[0]), istream)))


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

    @staticmethod
    def from_complete_info(info: MemoryInfoComplete) -> MemoryInfo:
        return MemoryInfo(
            ram=RamInfo(
                available = info.MemAvailable,
                free      = info.MemFree,
                used      = info.MemTotal - info.MemFree - info.Buffers - info.Cached - info.Slab,
                total     = info.MemTotal,
                shared    = info.Shmem,
            ),
            swap=SwapInfo(
                cached = info.SwapCached,
                free   = info.SwapFree,
                total  = info.SwapTotal,
            )
        )


@dataclass
class MemInfoReader:
    fpath: str = DEFAULT_MEMINFO_FPATH

    def load_all(self) -> MemoryInfoComplete:
        with open(self.fpath) as istream:
            return MemoryInfoComplete.from_file(istream)

    def load(self):
        return MemoryInfo.from_complete_info(self.load_all())
